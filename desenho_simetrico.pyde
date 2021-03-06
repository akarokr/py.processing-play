'''
Prova de conceito, programa de desenho com simetria radial
Alexandre B A Villares - http://abav.lugaralgum.com
Para rodar, instale o Processing Python Mode:
http://abav.lugaralgum.com/como-instalar-o-processing-modo-python/
'''

def setup():
    size(500, 500)
    background(255)
    strokeWeight(5)
    
def draw():
    with pushMatrix():
        translate(width/2, height/2)
        for _ in range(12):
            rotate(TWO_PI/12)
            if mousePressed:
                with pushMatrix():
                    translate(-width/2, -height/2)
                    line(pmouseX, pmouseY, mouseX, mouseY)
    if keyPressed:
        background(255)

