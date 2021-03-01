# Variables auxiliares #
# Lista con los jugadores de las partidas
jugadores = ["ANA", "JOSE", "JUAN"]
# Número de partidas a jugar según los partidos jugados por cada uno
num_partidas = int((17 + 15 + 10) / 2)
# Lista que contendrá las patidas jugadas
partidas = []
# Variable que contendrá el perdedor solicitado
perdedor = ""

# Función que encuentra el jugador de la próxima partida
# jugadores_partida_actual: Lista que contiene los jugadores de la partida actual
def nuevoJugador(jugadores_partida_actual):
    return list(set(jugadores) - set(jugadores_partida_actual))[0]

# Función que realiza el desarrollo de las partidas a jugar
# Se parte de la regla que cada que juegue Juan debe ser perdedor.
# Esta regla es debido a que si Juan pierde simpre que juega, juagaría solo 10 partidas, 
# que son justo las patidas que nos dan en los datos del problema
def jugarPartidas():
    for x in range(5, num_partidas + 1):
        if x == 5:
            jugador1 = "ANA"
            jugador2 = "JOSE"
            ganador = "JOSE"
        else:
            jugador1 = ganador
            jugador2 = nuevoJugador([jugador1, jugador2])
            ganador = jugador1 if jugador2 == "JUAN" else jugador2

        global partidas
        partidas.append({"Partida": x, "Jugador1": jugador1, "Jugador2": jugador2, "Ganador": ganador})

# Función que encuentra el perdedor de una partida en particular
# partida: Número de la partida en la que se requiere encontrar al perdedor
def obtenerPerdedor(partida):
    global perdedor
    perdedor = next((list(set([x["Jugador1"], x["Jugador2"]]) - set([x["Ganador"]]))[0]) for x in partidas if x["Partida"] == partida)

# Función que permite buscar las partidas perdidas de un jugador en particular
# jugador_partidas_perdidas: Jugador del que se buscarán las partidas perdidas
def listarPartidasPerdidas(jugador_partidas_perdidas):
    for partida in partidas:
        if jugador_partidas_perdidas in [partida["Jugador1"], partida["Jugador2"]] and partida["Ganador"] != jugador_partidas_perdidas:
            print(partida)

if __name__ == "__main__":
    # Semillas para la partida
    # Estas semillas se implantan para poder completar el número de partidas por jugador, según los datos dados
    partidas.append({"Partida": 1, "Jugador1": "ANA", "Jugador2": "JOSE", "Ganador": "ANA"})
    partidas.append({"Partida": 2, "Jugador1": "ANA", "Jugador2": "JUAN", "Ganador": "ANA"})
    partidas.append({"Partida": 3, "Jugador1": "ANA", "Jugador2": "JOSE", "Ganador": "ANA"})
    partidas.append({"Partida": 4, "Jugador1": "ANA", "Jugador2": "JUAN", "Ganador": "ANA"})

    jugarPartidas()
    obtenerPerdedor(2)

    print("El perdedor del segundo partido es: {perdedor}".format(perdedor = perdedor))
    print("los partidos perdidos por {perdedor} son:".format(perdedor = perdedor))
    listarPartidasPerdidas(perdedor)