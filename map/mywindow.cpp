#include "mywindow.h"
#include <QtGui>
#include <QPalette>


MyWindow::MyWindow()
{
    zoneCentrale = new QWidget;
    setCentralWidget(zoneCentrale);

    QAction *actionQuitter = new QAction("&Quitter", this);
    actionQuitter->setShortcut(QKeySequence("Ctrl+Q"));
    actionQuitter->setIcon(QIcon(QCoreApplication::applicationDirPath() + "/quitter.png"));

    //QAction *chooseColor = new QAction("&Color", this);

    QToolBar *toolBarFichier = addToolBar("Fichier");
    toolBarFichier->addAction(actionQuitter);
    //toolBarFichier->addAction(chooseColor);
    //m_boutonDialogue = new QPushButton("Couleur", this);
    //m_boutonDialogue->move(40,50);

    QObject::connect(actionQuitter, SIGNAL(triggered()), qApp, SLOT(quit()));
    //QObject::connect(chooseColor, SIGNAL(clicked()), this, SLOT(openColorDialog()));
    //QObject::connect(m_boutonDialogue, SIGNAL(clicked()), this, SLOT(openColorDialog()));

    //map

    map = new QLabel(zoneCentrale);
    pixMap = QPixmap("map.svg");
    labelSize = new QSize(800,450);
    pixMap = pixMap.scaled(*labelSize);
    map->setPixmap(pixMap);

    //QObject::connect(map, SIGNAL(), zoneCentrale, SLOT(draw()));
    //display options

    QGridLayout *options = new QGridLayout;
    QVBoxLayout *date = new QVBoxLayout;

    QLCDNumber *dateDisplay = new QLCDNumber(zoneCentrale);
    dateDisplay->setSegmentStyle(QLCDNumber::Flat);

    QSlider *dateSlider  = new QSlider(Qt::Horizontal, zoneCentrale);
    dateSlider->setGeometry(10, 60, 150, 20);
    dateSlider->setRange(0,2016);

    date->addWidget(dateDisplay);
    date->addWidget(dateSlider);

    QObject::connect(dateSlider, SIGNAL(valueChanged(int)),dateDisplay, SLOT(display(int)));

    QGroupBox *choice = new QGroupBox("Events", zoneCentrale);

    QRadioButton *peoples = new QRadioButton("Peoples");
    QRadioButton *flux = new QRadioButton("Flux");
    QRadioButton *bigEvents = new QRadioButton("Events");

    peoples->setChecked(true);

    QHBoxLayout *boxEvents = new QHBoxLayout;
    boxEvents->addWidget(peoples);
    boxEvents->addWidget(flux);
    boxEvents->addWidget(bigEvents);

    choice->setLayout(boxEvents);

    options->addLayout(date, 0, 0, 1, 3);
    options->addWidget(choice, 0, 4, 1, 2);

    //Layouts

    QGridLayout *layout = new QGridLayout;
    layout->addWidget(map, 0, 0, 4, 5);
    layout->addLayout(options, 5, 1, 1, 5);

    zoneCentrale->setLayout(layout);
}

void MyWindow::openColorDialog()

{
    QColor couleur = QColorDialog::getColor(Qt::white, this);

    QPalette palette;
    palette.setColor(QPalette::ButtonText, couleur);

    //QMessageBox::information(this, "Titre de la fenêtre", "Bonjour et bienvenue a tous les Zéros !");
}

void MyWindow::draw()
{
    //QImage img = map->pixmap()->toImage();
    QPainter pointer(&pixMap);

    pointer.drawPoint(QCursor::pos());
}

/*void MyWindow::paintEvent(QPaintEvent *)
{
    QPainter p();
    QPen pointpen (Qt::red);
    pointpen.setWidth(6);
    p.setPen(pointpen);
    p.drawPoint(QCursor::pos());

    /*if(flagModify == 1){

        p.begin(map);
        p.drawPoint(QCursor::pos());
        p.end();

        flagModify = 0;
    }
}*/

/*void MyWindow::mousePressEvent(QMouseEvent *)
{
    flagModify = 1;
    map->update(map->rect());
}*/
