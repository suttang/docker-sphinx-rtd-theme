FROM python:alpine3.6

RUN apk add --update alpine-sdk zlib-dev libjpeg-turbo-dev freetype freetype-dev

# Setup sphinx
RUN pip install sphinx
RUN pip install sphinx_rtd_theme
RUN pip install sphinxcontrib-blockdiag

# Download IPA font
RUN wget -O ipag00303.zip http://ipafont.ipa.go.jp/old/ipafont/ipag00303.php
RUN unzip ipag00303.zip
RUN mkdir /fonts
RUN mv ipag00303 /fonts/ipag00303
RUN rm ipag00303.zip

# Copy initialize scripts
COPY scripts scripts

# Create workspace
RUN mkdir documents

WORKDIR /documents
VOLUME /documents

CMD sphinx-build -b html source build
