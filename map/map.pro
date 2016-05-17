QT += core gui xml
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

deltarget.commands = $$QMAKE_DEL_FILE $$TARGET
QMAKE_EXTRA_TARGETS += deltarget
PRE_TARGETDEPS += deltarget

SOURCES += \
    main.cpp \
    mywindow.cpp \
    map.cpp

HEADERS += \
    mywindow.h \
    map.h


