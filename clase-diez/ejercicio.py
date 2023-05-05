from datetime import datetime
fecha = datetime.today().strftime('%Y-%m-%d')

class Bank:
    def __init__(self):
        self.cuentas = [] # guardar las cuentas y correlativos
        self.movimientos = [] #gurdar los movimientos

    def agregar_cuenta(self, _nombre, _cuenta, _rut):
            self.cuentas.append({
                'nombre': _nombre,
                'cuenta': _cuenta,
                'rut': _rut,
                'correlativo_movimiento': 1,
                'saldo': 0
            })

    def agregar_movimiento(self,_cliente, _cuenta,fecha,_tipo,_monto):
        for cuenta in self.cuentas:
            if cuenta['cuenta'] == _cuenta:
                if _tipo == 'Retiro':
                    if cuenta['saldo'] - _monto < 0:
                        print("excede maximo")
                    else:
                        self.movimientos.append({
                            'numero_cuenta': _cuenta,
                            'correlativo_movimiento': cuenta['correlativo_movimiento'],

                        })    
                


banco_santander = Bank()

banco_santander.agregar_cuenta("Marcial Abad", 75102321, "25.322.322-6")
banco_santander.agregar_cuenta("Marcial Abad", 75102323, "23.322.322-6")
banco_santander.agregar_cuenta("Marcial Abad", 75102327, "24.322.322-6")
