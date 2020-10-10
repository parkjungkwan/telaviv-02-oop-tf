from view import  Ui_Dialog, QtCore, QtGui, QtWidgets
from model import Model
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    '''
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181114'
    model = Model()
    model.exec(url)
    '''
    sys.exit(app.exec())
 
if __name__=='__main__':
    main()
