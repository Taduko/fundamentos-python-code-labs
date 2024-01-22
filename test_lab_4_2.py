from solution import almacenar_orden, db


def test_almacenar_orden_nueva():
    orden_nueva = ("Cliente A", "Pizza", "Refresco", "Helado")
    assert almacenar_orden(orden_nueva) == True


def test_almacenar_orden_existente():
    orden_existente = ("Cliente B", "Hamburguesa", "Papas Fritas")
    db.add(orden_existente)
    assert almacenar_orden(orden_existente) == False


def test_almacenar_orden_misma_persona():
    orden_misma_persona = ("Cliente A", "Hamburguesa", "Refresco")
    db.add(orden_misma_persona)
    assert almacenar_orden(orden_misma_persona) == False
