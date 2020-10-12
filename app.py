from ordenes import Orden, Permiso, Usuario

peticion = Orden(ip="8.8.8.8", usuario= "Jesús Hincapié", permiso= "admin")
peticion.enviar()


