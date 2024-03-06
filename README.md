# Poetry - Midterm

## Authors
- Justin Stone
- Owen Guglielmino

## About Poetry

[Poetry](https://python-poetry.org/docs/) is a tool designed to help developers manage project dependencies efficiently. It ensures that all team members have the correct versions of libraries installed to run the code, facilitating a uniform development environment across different machines. 

### Key Features
- **Dependency Management:** Simplifies the process of managing project dependencies.
- **Environment Consistency:** Guarantees that all contributors work in the same environment.
- **Easy Installation:** Streamlines the installation of project dependencies and tools.

### Installation

To install Poetry, you can use `pipx` which is a tool for installing and running Python applications in isolated environments. If you don't have `pipx` installed, you can install it via pip:

### Poetry Demo 
[![Watch the video](https://img.youtube.com/vi/3ypYZ_wsTW8/hqdefault.jpg)](https://youtu.be/3ypYZ_wsTW8?si=IsoUMy1sQHqLyscY)

### Installation

```sh
pip install pipx
pipx ensurepath
pipx install poetry
```
### Usage 

```sh
poetry new project_name
cd project_name
```

### New Environment

```sh
poetry shell
```

### Add Dependencies

```sh
poetry add pandas
poetry add numpy
```

### Run Code

```sh
poetry run python example.py
```
