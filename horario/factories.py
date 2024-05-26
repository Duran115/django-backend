from abc import ABC, abstractmethod
from horario.models import Horario

class HorarioFactory(ABC):
    @abstractmethod
    def crear_horario(self, curso, dia, hora_inicio, hora_fin):
        pass

class HorarioConcreteFactory(HorarioFactory):
    def crear_horario(self, curso, dia, hora_inicio, hora_fin):
        horario = Horario.objects.create(curso=curso, dia=dia, hora_inicio=hora_inicio, hora_fin=hora_fin)
        return horario
