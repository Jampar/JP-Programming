#include "Gene_Analysis_UI.h"
#include <QtWidgets/QApplication>
#include <QtWidgets/QPushButton>
#include <QtGui>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Gene_Analysis_UI w;

	w.show();
	return a.exec();
}

