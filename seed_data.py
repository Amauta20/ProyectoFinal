from AppModel.models import Familiar

Familiar(nombres="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123, nacimiento="12/10/2008").save()
Familiar(nombres="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890, nacimiento="11/10/2001").save()
Familiar(nombres="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345, nacimiento="02/01/1979").save()
Familiar(nombres="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567, nacimiento="12/10/2001").save()
Familiar(nombres="Juan", direccion="Rio Plata 745", numero_pasaporte=101023, nacimiento="12/10/2002").save()
Familiar(nombres="Lucio", direccion="Rio Plata 745", numero_pasaporte=823490, nacimiento="12/10/2003").save()
Familiar(nombres="Anabell", direccion="Rio Plata 745", numero_pasaporte=345266, nacimiento="12/10/2004").save()
Familiar(nombres="Pedro", direccion="Rio Plata 745", numero_pasaporte=567135, nacimiento="12/10/2000").save()

print("Se cargo con éxito los usuarios de pruebas")