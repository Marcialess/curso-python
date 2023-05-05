class Artefacto:
    def __init__(self,_director,_gerente,_empleado) :
        self.__director = _director
        self.__gerente = _gerente
        self.__empleado = _empleado

    @property
    def director(self) -> str:
        return self.__director

    @director.setter
    def director(self,director: str) -> None:
        self.__director = director        

    @property
    def gerente(self) -> str:
        return self.__gerente

    @gerente.setter
    def director(self,gerente: str) -> None:
        self.__gerente = gerente    

    @property
    def empleado(self) -> str:
        return self.__empleado

    @gerente.setter
    def empleado(self,empleado: str) -> None:
        self.__empleado = empleado  