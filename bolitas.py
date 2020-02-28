import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

frasco=20

class jugador(threading.Thread):
    def __init__(self,turno,cant):
        super().__init__()
        self.turno=turno
        self.cant=cant
        self.posesion=0
        
        
    
    def sacar(self) :
        global frasco
        frasco-=self.cant
        
    def poner(self) :
        global frasco
        frasco+=self.cant
        self.turno.notify()
    
    def run(self):
        while True:
            with self.turno:
                while self.cant<frasco:
                    self.turno.wait()
                
                self.sacar()
                self.poner()
                    
            
            

 
    

