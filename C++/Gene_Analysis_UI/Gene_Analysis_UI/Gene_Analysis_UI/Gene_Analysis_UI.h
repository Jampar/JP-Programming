#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_Gene_Analysis_UI.h"

#include <QtGui>

class Gene_Analysis_UI : public QMainWindow
{
	Q_OBJECT

public:
	Gene_Analysis_UI(QWidget *parent = Q_NULLPTR);

private:
	Ui::Gene_Analysis_UIClass ui;

public slots:
	void Analyse();
};

