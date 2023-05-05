from datetime import datetime
fecha = datetime.today().strftime('%Y-%m-%d')


class Transporte:
    def __init__(self):
        self.patentes = []
        self.movimientos = []
        self.tarifa = 730
        self.valores = {
            'hombre': self.tarifa,
            'mujer': self.tarifa,
            'niños': 0,
            'adulto_mayor': self.tarifa/2
        }

    def registrar_micro(self, _patente, _chofer):
        patente = list(
            filter(lambda element: element['patente'] == _patente, self.patentes))
        if len(patente) > 0:
            print(
                f'La patente {_patente} con el chofer {_chofer} ya se encuentra registrada')
        else:
            self.patentes.append({
                'patente': _patente,
                'chofer': _chofer,
            })

    def pay_method(self, _patente, _tipo_persona, fecha=None):
        if fecha is None:
            fecha = datetime.now()
        self.movimientos.append({
            'patente': _patente,
            'tipo_persona': _tipo_persona,
            'fecha': fecha,
            'valor': self.valores[_tipo_persona]
        })

    def reporte_transporte(self, _tipo_reporte, _valor):
        movimientos = list(
            filter(lambda elemento: elemento[_tipo_reporte] == _valor, self.movimientos))
        total_cobrado = 0
        for pasaje in movimientos:
            total_cobrado += pasaje['valor']
            print(pasaje['fecha'], pasaje['tipo_persona'], pasaje['valor'])

        print("----------------")
        print(f'Total cobrado es: {total_cobrado}')


Empire = Transporte()
Empire.registrar_micro('ABC-321', 'juan')
Empire.registrar_micro('ABC-451', 'Luis')
Empire.registrar_micro('ABC-567', 'Camacho')

Empire.pay_method("ABC-321", "mujer")
Empire.pay_method("ABC-451", 'niños')
Empire.pay_method("ABC-567", "hombre")

Empire.reporte_transporte('tipo_persona', 'niños')
