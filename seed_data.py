from AppModel.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
Familiar(nombre="Juan", direccion="Rio Plata 745", numero_pasaporte=101023).save()
Familiar(nombre="Lucio", direccion="Rio Plata 745", numero_pasaporte=823490).save()
Familiar(nombre="Anabell", direccion="Rio Plata 745", numero_pasaporte=345266).save()
Familiar(nombre="Pedro", direccion="Rio Plata 745", numero_pasaporte=567135).save()

print("Se cargo con éxito los usuarios de pruebas")