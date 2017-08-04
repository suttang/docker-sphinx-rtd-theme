#!/bin/sh

function resert_source_dir() {
    if [ -d /documents/source ]; then
        rm /documents/source
        echo "delete documents/source/"
    fi

    if [ ! -e /documents/source ]; then
        mkdir /documents/source
        echo "create documents/source/"
    fi

    if [ ! -e /documents/source/_static ]; then
        mkdir /documents/source/_static
        echo "create documents/source/_static/"
    fi

    cp /scripts/files/conf.py /documents/source/conf.py
    echo "created documents/source/conf.py"

    echo "index.rst" > /documents/source/index.rst
    echo "created documents/source/index.rst"
}

if [ -d /documents/source ]; then
    while true; do
        read -p 'Do you want to reset documents/source/? [Y/n]' Answer
        case $Answer in
            '' | [Yy]* )
                resert_source_dir
                break;
                ;;
            [Nn*] )
                break;
                ;;
            * )
                echo Please answer Y or n
        esac
    done
else
    resert_source_dir
fi
