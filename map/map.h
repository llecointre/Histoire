#ifndef MAP
#define MAP

#include <QtGui>

class Map : public QPixmap
{
    Q_OBJECT

public:
    Map();

public slots:
    void draw();

private:

protected :
    virtual void paintEvent(QPaintEvent *);
};

#endif // MAP

