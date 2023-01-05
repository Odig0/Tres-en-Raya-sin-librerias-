contador_x = 0
contador_o = 0
class persona:
    
    def __init__(self,nombre,ci):
        self.nombre=nombre
        self.ci=ci
    

class jugador(persona):
    ganador= None

    def __init__(self, nombre, ci,nick):
        super().__init__(nombre, ci)
        self.nick = nick
        self.pintar = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

        
    def ver_tablero(self):
        print("\n")
        print(self.pintar[0] + " | " + self.pintar[1] + " | " +  self.pintar[2]  +"       1 | 2 | 3")
        print(self.pintar[3] + " | " + self.pintar[4] + " | " +  self.pintar[5]  +"       4 | 5 | 6")
        print(self.pintar[6] + " | " + self.pintar[7] + " | " +  self.pintar[8]  +"       7 | 8 | 9")
        print("\n")
    
    def jugar(self):
        global contador_x
        global contador_o
        global ganador
        print("\n")
        print("Empieza el juego!")
        self.ver_tablero()
        for i in range(5):
            print(f"Turno de {n} - X")
            valor="X"
            #empiezan a jugar - Jugador1
            self.turno(valor)
            self.mostrarganador()
            if ganador != "X" and i < 4 :
                for j in range(3):
                    print(f"Turno de {n1} - O")
                    valor="O"
                    self.turno(valor)
                    self.mostrarganador()
                    if ganador == "O":
                            print(f"{n1} GANASTE")
                            print("\n")
                            contador_o += 1
                    break
            elif ganador=="X":
                print(f"{n} GANASTE")
                print("\n")
                contador_x += 1
                break
            else:
                print("Empataron")
                print("\n")
    def mostrarganador(self):
        global ganador
        self.controlLinea()
        self.controlVertical()
        self.controlDiagonal()
    def controlLinea(self):
        global ganador
        if self.pintar[0]== self.pintar[1]==self.pintar[2] !="-":
            ganador = self.pintar[0]
        elif self.pintar[3] ==  self.pintar[4] == self.pintar[5] != "-":
            ganador = self.pintar[3]
        elif self.pintar[6] ==  self.pintar[7] == self.pintar[8] != "-":
            ganador = self.pintar[6]
    def controlVertical(self):
        global ganador
        if self.pintar[0] ==  self.pintar[3] == self.pintar[6] != "-":
            ganador = self.pintar[0]
        elif self.pintar[1] ==  self.pintar[4] == self.pintar[7] != "-":
            ganador = self.pintar[1]
        elif self.pintar[2] ==  self.pintar[5] == self.pintar[8] != "-":
            ganador = self.pintar[2]
    def controlDiagonal(self):
        global ganador
        if self.pintar[0] ==  self.pintar[4] == self.pintar[8] != "-":
            ganador = self.pintar[0]
        elif self.pintar[2] ==  self.pintar[4] == self.pintar[6] != "-":
            ganador = self.pintar[2]
    def turno(self,valor):
        anoto = False
        while anoto == False:
            p = int(input("Elegi una posicion del 1 al 9: "))
            p -= 1
            if self.pintar[p] == "_":
                anoto = True
            else:
                print("Esa posicion ya esta ocupada")
        self.pintar[p] = valor
        self.ver_tablero()
        
n=input("Ingrese el jugador #1: ")
n1=input("Ingrese el jugador #2: ")

jugador1 = jugador(n,6294639,'Baldi')
jugador2 = jugador(n1,3438394,'Wess')
jugador1.jugar()

def run():
    global contador_x
    global contador_o
    for i in range(2):
        n=input("Ingrese el jugador #1: ")
        n1=input("Ingrese el jugador #2: ")

        jugador1 = jugador(n,6294639,'Baldi')
        jugador2 = jugador(n1,3438394,'Wess')
        jugador1.jugar()
    print("El jugador X gano veces: ",contador_x)
    print("El jugador O gano veces: ",contador_o)

if __name__ == '__main__':
    run()