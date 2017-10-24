# Sphinx documentation with Docker

## Quickstart

To start `suttang/sphinx-rtd-theme`, You can use `sphinx-quickstart`

http://docs.readthedocs.io/en/latest/getting_started.html

```
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd-theme sphinx-quickstart
```

```
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd-theme sphinx-quickstart -q -p "YourProjectName" -a "suttang <suttang@gmail.com>" -v 1.0.0 --sep --no-batchfile
```


## Build your documents

The default `CMD` of `suttang/sphinx-rtd-theme` is `make html`.

``` 
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd-theme
```

Your can use your favorite build commands.

```
# make html
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd-theme make html

# sphinx-build
docker run --rm -it -v $(pwd)/documents:/documents suttang/sphinx-rtd-theme sphinx-build -b html source build
```

This dockerfile include [sphinx-autobuild](https://github.com/GaretJax/sphinx-autobuild)

```
# use autobuild with make
docker run --rm -it -v $(pwd)/documents:/documents -p 8000:8000 suttang/sphinx-rtd-theme make livehtml

# use autobuild with sphinx-autobuild
docker run --rm -it -v $(pwd)/documents:/documents -p 8000:8000 suttang/sphinx-rtd-theme sphinx-autobuild -b html $SOURCE $OUTPUT -H 0.0.0.0
```


## Build dockerfile

```
docker build -t "suttang/sphinx-rtd-theme" .
```


Thank you.