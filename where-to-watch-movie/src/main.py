import os
import re
from time import sleep, time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tqdm import tqdm

CONNECTION_RETRY = 5

class ScrapMovie():
  def __init__(self, path):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')    
    self.driver = webdriver.Chrome(options=options)
    self.driver.get(path)
  
  def task_with_retry(self, elem):
    for i in range(1, CONNECTION_RETRY + 1):
      try:
        result = elem.get_attribute(('src'))
      except Exception as e:
        print("error:{e} retry:{i}/{max}".format(e=e, i=i, max=CONNECTION_RETRY))
        sleep(3)
      else:
        return result
    return False
  
  def select_item(self):
    movie_elems = self.driver.find_elements(by=By.CLASS_NAME, value="title-list-grid__item")
    movie_length = len(movie_elems)
    movie_path_list = []
    i = 0
    
    # get movie title list
    while (i <= 100):
      movie_item = movie_elems[i]
      movie_item = movie_item.find_element(by=By.CLASS_NAME, value="title-list-grid__item--link")
      page_path = movie_item.get_attribute(('href'))
      movie_path_list.append(page_path)
      
      i += 1
      print(i, '/', movie_length)
      if movie_length == i:
        self.page_scroll_by_offset(movie_item)
        movie_elems = self.driver.find_elements(by=By.CLASS_NAME, value="title-list-grid__item")
        movie_length = len(movie_elems)
        
        # 全ての映画をリストに入れたら終了
        if movie_length == i:
          break
    return movie_path_list
      
  def page_scroll_by_offset(self, element):
    self.driver.execute_script("arguments[0].scrollIntoView();", element)
    script = "window.scrollTo(0, window.pageYOffset + " + str(-100) + ");"
    self.driver.execute_script(script)
    sleep(7)
    
  def get_movie_details(self, path):
    self.driver.get(path)
    sleep(3) #読み込み安定
    
    try:
      # basepath
      basename = os.path.basename(path)
      # imgpath
      img_elems = self.driver.find_elements(by=By.CSS_SELECTOR, value=".picture-comp__img.lazyautosizes.ls-is-cached.lazyloaded")
      img_path = self.task_with_retry(img_elems[0])
      # title, year
      title_elems = self.driver.find_elements(by=By.CLASS_NAME, value="title-block")
      title_and_year = title_elems[0].text.rsplit(' ', 1)
      title = title_and_year[0]
      year = re.sub(r"\D", "", title_and_year[1])
      # details
      detail_elems = self.driver.find_elements(by=By.CLASS_NAME, value="detail-infos__value")
      rate_watch = detail_elems[0].text
      category = detail_elems[1].text
      time = detail_elems[2].text
      director = detail_elems[3].text
      # abst
      abst_elems = self.driver.find_elements(by=By.CSS_SELECTOR, value=".text-wrap-pre-line.mt-0")
      abst = abst_elems[0].text
      
      self.save_to_csv(basename, title, year, img_path, rate_watch, category, time, director, abst)
    except:
      print(path)

  def save_to_csv(self, basename, title, year, 
                  img_path, rate_watch, category, time, director, abst):
    savepath = './film.csv'
    if not os.path.exists(savepath):
      with open(savepath, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(['uid', 'title', 'year', 'image_path', 'rate', 'categories', 'time', 'director', 'abst'])
        writer.writerow([basename, title, year, img_path, rate_watch, category, time, director, abst])
      
    else:
      with open(savepath, 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow([basename, title, year, img_path, rate_watch, category, time, director, abst])
      
    
if __name__ == '__main__':
  main_path = 'https://www.justwatch.com/jp/%E5%8B%95%E7%94%BB%E9%85%8D%E4%BF%A1%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9/netflix?content_type=movie'
  scrap_movie = ScrapMovie(main_path)
  movie_paths = scrap_movie.select_item()
  
  for movie_path in tqdm(movie_paths):
    scrap_movie.get_movie_details(movie_path)
