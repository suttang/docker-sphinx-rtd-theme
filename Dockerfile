FROM python:alpine3.6

RUN apk add --update --no-cache \
        build-base \
        zlib-dev \
        libjpeg-turbo-dev \
        freetype \
        freetype-dev \
    && pip install \
        sphinx \
        sphinx_rtd_theme \
        sphinx-autobuild \
        sphinxcontrib-blockdiag \
        sphinxcontrib-seqdiag \
        sphinxcontrib-actdiag \
        sphinxcontrib-nwdiag \
    && wget -O ipag00303.zip http://ipafont.ipa.go.jp/old/ipafont/ipag00303.php \
    && unzip ipag00303.zip \
    && mkdir /fonts \
    && mv ipag00303 /fonts/ipag00303 \
    && rm ipag00303.zip \
    && apk del build-base

# Copy initialize scripts
COPY scripts scripts

# Create workspace
RUN mkdir documents

WORKDIR /documents
VOLUME /documents

CMD sphinx-build -b html source build
