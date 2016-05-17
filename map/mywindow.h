#ifndef MYWINDOW_H
#define MYWINDOW_H

#include <QMainWindow>
#include <QMessageBox>
#include <QPushButton>

class MyWindow : public QMainWindow
{
    Q_OBJECT

public:
    MyWindow();

public slots:
    void openColorDialog();
    void draw();

private:
    QWidget *zoneCentrale;
    QLabel *map;
    QPixmap pixMap;
    QSize *labelSize;

protected :
    //int flagModify;
    //void mousePressEvent(QMouseEvent *);
    void paintEvent(QPaintEvent *);
};

#endif // MYWINDOW_H

