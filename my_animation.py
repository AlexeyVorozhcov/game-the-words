from PyQt5.QtCore import QTimer


class Animation():
    """
    Запускает таймер-эффект анимации, выполняет переданный в объект метод script, 
    передавая в него объекты из переданного списка listscroll
    через указанный интервал delay
    """
    def __init__(self, listscroll, script, delay) -> None:
        self._listscroll = listscroll
        self._external_script = script
        self.delay = delay
        self._frame = 0
        self._len = len(listscroll)
        self._timer = QTimer()
        self._timer.timeout.connect(self._internal_script)
        self._timer.start(self.delay)        

    def _internal_script(self):
        self._external_script(self._listscroll[self._frame])
        self._frame += 1
        if self._frame > self._len-1:
            self._timer.stop()        




 