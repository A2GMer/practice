# React Practice Repository

Welcome to my React practice repository! In this repository, I'm working through the Microsoft Learn module on getting started with React. You can find the original module [here](https://learn.microsoft.com/ja-jp/training/modules/react-get-started/1-introduction).

## About

This repository contains my code and exercises as I learn and practice React. The module covers the fundamentals of React, including setting up a development environment, creating components, managing state, and more.

## Table of Contents

- [Getting Started](#getting-started)
- [Topics Covered](#topics-covered)
- [Running with Docker](#running-with-docker)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this project:

1. Clone the repository to your local machine.
2. Follow along with the Microsoft Learn module linked above.
3. Explore the different folders corresponding to each module section.

## Topics Covered

Throughout this practice, I'll be covering various topics, including:

- Setting up a React development environment
- Creating and using components
- Managing state and props
- Working with forms and user input
- Implementing basic routing
- ...and more!

## Running with Docker
This project includes a Dockerfile that allows you to easily set up and run the React application. Follow these steps to get started:
1. Ensure you have Docker installed on your machine. You can download it from [here](https://www.docker.com/get-started).
2. Clone this repository to your local machine: 
``` sh
git clone https://github.com/your-username/react-practice.git
cd react-practice
```
1. Build and start the Docker containers using docker-compose:``` shdocker-compose up -d ```
2. Once the containers are up, you can access a bash shell within the app container using the following command:``` shdocker-compose exec app bash ```
3. Inside the container's shell, navigate to the React app's directory:``` shcd /linux-study/mslearn-react/code/0-starter/public ```
4. Start the React development server:``` shnpm start ```
		
You can now access the React app by visiting http://localhost:8080 in your browser.
Please note that this Docker setup is intended for local development and learning purposes. If you encounter any issues or have questions, feel free to reach out or consult the Docker documentation.

## Contributing

I'm currently using this repository for personal practice and learning purposes, so I'm not actively seeking contributions. However, if you have any suggestions or improvements, feel free to open an issue in this repository.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding!

