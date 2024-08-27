def main ():
    willPlay = input("Deseja iniciar o jogo (S, N)? ")
    while willPlay.lower() in ["s", "sim", "y", "yes"]:
        buildBoard()

        playerMove = nextMove()
        buildBoard(playerMove)
        willPlay = input("Deseja continuar jogando (S, N)? ")

def buildBoard(playerMove = ""):
    print("board")
    print(playerMove)

def nextMove():
    playerMove = input("Qual o proximo movimento? ")
    return playerMove

main()