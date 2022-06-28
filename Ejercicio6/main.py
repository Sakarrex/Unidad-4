from ClaseRepositorio import Repositorio
from vistaProvincias import ProvinciasView
from ClaseControlador import ControladorProvincias
from ClaseObjectEncoder import ObjectEncoder

def main():
    conn = ObjectEncoder("datos.json")
    repo = Repositorio(conn)
    vista = ProvinciasView()
    ctrl = ControladorProvincias(repo,vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()