# Just Watch Movie Scraper

This tool allows you to scrape movie information from the Just Watch website and export it to a CSV file.

## Usage

### Docker Setup

1. Build and start the Docker containers using `docker-compose`:
   ```bash
   docker-compose up -d
   ```

2. Once the containers are up, you can access a bash shell within the app container using the following command:
   ```bash
   docker-compose exec app bash
   ```

3. Run the Python script to start scraping:
   ```bash
   python main.py
   ```

This will launch the tool and begin scraping movie information from Just Watch. The data will be saved in a CSV file for further analysis or use.

## Requirements

- Docker

## Configuration

You may need to configure the scraping parameters within the `main.py` script, such as specifying the search query or modifying the scraping logic.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README further to include additional details or instructions specific to your project.
