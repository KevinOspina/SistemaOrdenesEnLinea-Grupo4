from abc import ABCMeta, abstractmethod


class Usuario(object):
    def __init__(self, name: str = ""):
        self.name = name

class Permiso(object):
    def __init__(self, type: str = ""):
        self.type = type

#Clase Orden se encarga de probar que sean correctas las verificaciones, usuario y el permiso necesario

class Orden:
    def __init__(self, ip: str = "", usuario: Usuario = None, permiso: Permiso = None):
        self.ip: str = ip
        self.usuario = usuario
        self.permiso = permiso

    def __enviar(self):
        print(f"Petición enviada de {self.usuario} con permiso {self.permiso}")

    def enviar(self):
        creador = CreadorVerificaciones()
        verificadores = creador.crearVerificaciones()
        chech = []
        for v in verificadores:
            orden = Orden(self.ip, self.usuario, self.permiso)
            if v.verificar(self, orden):
                chech.append(True)
            else:
                print("false")
                chech.append(False)
                break

        if False in chech:
            print("Las verificaciones fallaron")
        else:
            self.__enviar()   


#Creación de clases de verificaciones 

class Verificacion:
    class Mensaje(metaclass=ABCMeta):
       @abstractmethod
       def verificar(self, orden: Orden) -> bool:
           pass


class Autenticacion(Verificacion):
    def verificar(self, orden: Orden) -> bool:
        print("Verificando la autenticación")
        return True


class SanearDatos(Verificacion):
    def verificar(self, orden: Orden) -> bool:
        print("Verificando el saneador de los datos")
        return True
    

class FiltrarIP(Verificacion):
    def verificar(self, orden: Orden) -> bool:
        print("Verificando la IP")
        return True


class RespuestaCache(Verificacion):
    def verificar(self, orden: Orden) -> bool:
        print("Verificando la respuesta cache")
        return True

#Clase creadora para los diferentes tipos de verificaciones

class CreadorVerificaciones:

    @staticmethod
    def crearVerificaciones():    
        verificadores = [Autenticacion, SanearDatos, FiltrarIP, RespuestaCache]
        verificadoresCreados = []
        for val in verificadores:
            verificadoresCreados.append(val)

        return verificadoresCreados


