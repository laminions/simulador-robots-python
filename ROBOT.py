class Robot:
    def __init__(self, nombre, bateria, escudo):
        self.nombre = nombre
        self.bateria = bateria
        self.escudo = escudo

    def mostrar_estado(self):
        print(f"{self.nombre} -> Batería: {self.bateria}, Escudo: {self.escudo}")


class RobotAtaque(Robot):
    def atacar(self, objetivo):
        if self.bateria >= 10:
            daño = 15
            print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
            
            # Reducir escudo del objetivo
            objetivo.escudo -= daño
            self.bateria -= 10

            if objetivo.escudo < 0:
                objetivo.escudo = 0

        else:
            print(f"{self.nombre} no tiene suficiente batería para atacar.")


class RobotDefensa(Robot):
    def recargar(self):
        if self.bateria >= 5:
            aumento = 10
            self.escudo += aumento
            self.bateria -= 5
            print(f"{self.nombre} recarga su escudo en {aumento} puntos.")
        else:
            print(f"{self.nombre} no tiene suficiente batería para recargar.")


# Simulación del juego
if __name__ == "__main__":
    robot1 = RobotAtaque("Destructor", 50, 40)
    robot2 = RobotDefensa("Protector", 50, 60)

    robot1.mostrar_estado()
    robot2.mostrar_estado()

    print("\n--- Turno de ataque ---")
    robot1.atacar(robot2)

    robot1.mostrar_estado()
    robot2.mostrar_estado()

    print("\n--- Turno de defensa ---")
    robot2.recargar()

    robot1.mostrar_estado()
    robot2.mostrar_estado()