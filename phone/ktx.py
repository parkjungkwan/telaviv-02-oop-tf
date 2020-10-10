class Ktx(object):
    """description of class"""
    def __init__(self, station, fee):
        self.station = station
        self.fee = fee
        print('KTX __init__')
    def __del__(self):
        print('KTX __del__')
    def __str__(self):
        return '{} ==> {} 원' .format(self.station, self.fee)
    def Disp(self):
        print('{} ==> {} 원' .format(self.station, self.fee))
        print('self ==> {}' .format(id(self))
    def getStation(self):
        return self.station
    def getFee(self):
        return self.fee
    def setStation():
        print('{} ==> {}로 변경' .format(self.station, station))
        self.station = station
    def setFee(self, fee):
        print('{} ==> {}원으로 변경' .format(selif.fee, fee))
      