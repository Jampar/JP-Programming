/********************************************************************************
** Form generated from reading UI file 'Gene_Analysis_UI.ui'
**
** Created by: Qt User Interface Compiler version 5.12.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_GENE_ANALYSIS_UI_H
#define UI_GENE_ANALYSIS_UI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Gene_Analysis_UIClass
{
public:
    QWidget *centralWidget;
    QPushButton *pushButton;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *Gene_Analysis_UIClass)
    {
        if (Gene_Analysis_UIClass->objectName().isEmpty())
            Gene_Analysis_UIClass->setObjectName(QString::fromUtf8("Gene_Analysis_UIClass"));
        Gene_Analysis_UIClass->resize(624, 400);
        centralWidget = new QWidget(Gene_Analysis_UIClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(260, 180, 75, 23));
        Gene_Analysis_UIClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(Gene_Analysis_UIClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        Gene_Analysis_UIClass->setStatusBar(statusBar);

        retranslateUi(Gene_Analysis_UIClass);

        QMetaObject::connectSlotsByName(Gene_Analysis_UIClass);
    } // setupUi

    void retranslateUi(QMainWindow *Gene_Analysis_UIClass)
    {
        Gene_Analysis_UIClass->setWindowTitle(QApplication::translate("Gene_Analysis_UIClass", "Gene_Analysis_UI", nullptr));
        pushButton->setText(QApplication::translate("Gene_Analysis_UIClass", "PushButton", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Gene_Analysis_UIClass: public Ui_Gene_Analysis_UIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GENE_ANALYSIS_UI_H
