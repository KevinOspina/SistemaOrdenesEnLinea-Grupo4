from ordenes import Orden, Permiso, Usuario

#Se realiza el envío de la orden para generar las verificaciones

orden = Orden(ip="8.8.8.8", usuario= "Jesús Hincapié", permiso= "admin")
orden.enviar()


