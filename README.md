# Sphinx documentation with Docker

## Quickstart

Build an image from the Dockerfile

```
$ docker build -t "suttang/sphinx-rtd-theme" .
```

Create basic configuration

```
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd-theme sphinx-quickstart
```

http://docs.readthedocs.io/en/latest/getting_started.html

Build your documents

```
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd-theme
```

http://docs.readthedocs.io/en/latest/builds.html

or Use autobuild

```
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd-theme make livehtml
```

https://pypi.python.org/pypi/sphinx-autobuild

Thank you.