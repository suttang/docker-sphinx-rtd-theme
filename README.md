# Sphinx documentation with Docker

## Quickstart

Build an image from the Dockerfile

```
$ docker build -t "suttang/sphinx-rtd" .
```

Make default `conf.py`

```
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd /scripts/init.sh
```

Build your documents

```
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd
```

Thank you.