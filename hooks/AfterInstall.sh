if [ -L /ubuntu/${APPLICATION_NAME} ]; then
    OLD=`readlink /ubuntu/${APPLICATION_NAME}`;
fi

mv -T /ubuntu/${APPLICATION_NAME}-tmp /ubuntu/${APPLICATION_NAME}

if [ ! -z ${OLD+x} ]; then
    rm -r ${OLD};
fi
