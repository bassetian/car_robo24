from time import sleep_ms

#frente
def frente(A1, A2, B1, B2, t):
    A1.on()
    A2.off()
    B1.on()
    B2.off()
    sleep_ms(t)
#reversa
def rev (A1, A2, B1, B2, t):
    A1.off()
    A2.on()
    B1.off()
    B2.on()
    sleep_ms(t)
#alto
def alto(A1, A2, B1, B2, t):
    A1.off()
    A2.off()
    B1.off()
    B2.off()
    sleep_ms(t)
#derecha
def izquierda (A1, A2, B1, B2, t):
    A1.on()
    B1.off()
    A2.off()
    B2.on()
    sleep_ms(t)
#izquierda
def derecha (A1, A2, B1, B2, t):
    A1.off()
    A2.on()
    B1.on()
    B2.off()
    sleep_ms(t)
