#include "map.h"

Map::Map() : QPixmap()
{

}

void Map::paintEvent(QPaintEvent *)
{
    QPainter p(this);
    QPen pointpen (Qt::red);
    pointpen.setWidth(6);
    p.setPen(pointpen);
    p.drawPoint(QCursor::pos());
}
