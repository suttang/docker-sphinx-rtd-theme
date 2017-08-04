#!/bin/sh

function create_default_config() {
    cp /scripts/files/conf.py /documents/conf.py
    echo "created documents/conf.py"
}

if [ -e /documents/conf.py ]; then
    while true; do
        read -p 'Overwrite documents/conf.py? [Y/n]' Answer
        case $Answer in
            '' | [Yy]* )
                create_default_config
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
    create_default_config
fi


