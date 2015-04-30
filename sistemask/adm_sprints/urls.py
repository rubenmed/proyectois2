from django.conf.urls import patterns, include, url
from .views import SprintView, CrearSprint, CrearSprintConfirm, EliminarSprint, ModificarSprint, ModificarSprintConfirm, ActivarSprint, AsignarHistorias, AsignarHistoriasConfirm, AsignarUsuarioFlujo, AsignarUsuarioFlujo1, AsignarUsuarioFlujo2, DesasignarHistorias, DesasignarHistoriasConfirm, VerInformacionSprint

urlpatterns= patterns('',
    url(r'^$', SprintView.as_view(), name="sprint"),
    url(r'^crear/$', CrearSprint.as_view(), name="crear_sprint"),
    url(r'^crear/confirmar/$', CrearSprintConfirm.as_view(), name="confirmar_crear_sprint"),
    url(r'^eliminar/$', EliminarSprint.as_view(), name="eliminar_sprint"),
    url(r'^modificar/$', ModificarSprint.as_view(), name= "modificar_sprint"),
    url(r'^modificar/confirmar/$', ModificarSprintConfirm.as_view(), name= "modificar_sprint"),
    url(r'^activar/$', ActivarSprint.as_view(), name= "activar_sprint"),
    url(r'^asignar/$', AsignarHistorias.as_view(), name="asignar_historias"),
    url(r'^asignar/confirmar/$', AsignarHistoriasConfirm.as_view(), name="asignar_historias_confirm"),
    url(r'^asignarUF/$', AsignarUsuarioFlujo.as_view(), name="asignar_usuario_flujo"),
    url(r'^asignarUF/paso1/$', AsignarUsuarioFlujo1.as_view(), name="asignar_usuario_flujo1"),
    url(r'^asignarUF/paso2/$', AsignarUsuarioFlujo2.as_view(), name="asignar_usuario_flujo2"),
    url(r'^desasignar/$', DesasignarHistorias.as_view(), name="desasignar_historias"),
    url(r'^desasignar/confirmar/$', DesasignarHistoriasConfirm.as_view(), name="desasignar_historias"),
    url(r'^informacion/$', VerInformacionSprint.as_view(), name="informacion"),
)
