from pathlib import Path
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'output/pdf'; OUT.mkdir(parents=True,exist_ok=True)
PHOTO=ROOT/'src/assets/victor.jpeg'; CROP=OUT/'portrait.jpg'; PDF=OUT/'CV-Victor-Perez-Sosa.pdf'
pdfmetrics.registerFont(TTFont('R','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')); pdfmetrics.registerFont(TTFont('B','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
INK=HexColor('#162234'); NAVY=HexColor('#203A5F'); TEAL=HexColor('#1C7C7C'); PALE=HexColor('#EDF4F5'); GREY=HexColor('#52616B')

def t(c,s,x,y,size=9,b=False,color=INK): c.setFont('B' if b else 'R',size); c.setFillColor(color); c.drawString(x,y,s)
def lines(c,s,x,y,w,size=8.5,lead=11,b=False,color=INK):
    f='B' if b else 'R'; c.setFont(f,size); words=s.split(); row=''
    for word in words:
        test=(row+' '+word).strip()
        if c.stringWidth(test,f,size)<=w: row=test
        else: t(c,row,x,y,size,b,color); y-=lead; row=word
    if row: t(c,row,x,y,size,b,color); y-=lead
    return y
def heading(c,s,x,y,w):
    t(c,s.upper(),x,y,10,b=True,color=TEAL); c.setStrokeColor(TEAL); c.setLineWidth(.8); c.line(x,y-5,x+w,y-5); return y-20
def bullet(c,s,x,y,w):
    c.setFillColor(TEAL); c.circle(x+2,y+2,1.7,fill=1,stroke=0); return lines(c,s,x+10,y,w-10,8.2,10)
def main():
    im=Image.open(PHOTO).convert('RGB'); w,h=im.size; side=min(w,int(h*.61)); left=(w-side)//2; top=int(h*.13); im.crop((left,top,left+side,top+side)).save(CROP,quality=92)
    c=Canvas(str(PDF),pagesize=A4); W,H=A4; sidew=164
    c.setFillColor(NAVY); c.rect(0,0,sidew,H,fill=1,stroke=0)
    c.drawImage(ImageReader(str(CROP)),25,H-168,114,114,mask='auto')
    t(c,'VICTOR PEREZ',25,H-193,14,True,white); t(c,'SOSA',25,H-210,14,True,white); t(c,'Junior Full-Stack Developer',25,H-227,8,False,HexColor('#BDE9E7'))
    c.setStrokeColor(HexColor('#6FA5A4')); c.line(25,H-241,139,H-241)
    t(c,'CONTACTO',25,H-261,8,True,white)
    for i,s in enumerate(['victorperezsosa2001@gmail.com','637 699 258','Gran Canaria, Espana','github.com/vititoOX','LinkedIn: Victor Perez Sosa']): t(c,s,25,H-278-i*15,7.2,False,white)
    t(c,'TECNOLOGIAS',25,H-365,8,True,white)
    for i,s in enumerate(['Angular · React · TypeScript','Python · Flask · PostgreSQL','Docker · Java · Git · REST APIs']): t(c,s,25,H-382-i*15,7.2,False,white)
    t(c,'FORMACION',25,H-447,8,True,white); t(c,'CFGS Desarrollo de',25,H-465,7.5,True,white); t(c,'Aplicaciones Multiplataforma',25,H-477,7.5,True,white); t(c,'DAM finalizado',25,H-492,7.2,False,HexColor('#BDE9E7'))
    x=190; w=W-x-30; y=H-54
    t(c,'Perfil profesional',x,y,25,True); y-=27
    y=lines(c,'Tecnico Superior en Desarrollo de Aplicaciones Multiplataforma. Desarrollo aplicaciones web full-stack con especial interes en APIs, bases de datos y productos que resuelven necesidades reales. Busco una primera oportunidad como desarrollador junior en Gran Canaria, hibrido o remoto.',x,y,w,9.4,13,color=GREY)-10
    y=heading(c,'Proyectos destacados',x,y,w)
    t(c,'NominaHub',x,y,12,True); t(c,'Angular 18 · Flask · PostgreSQL · Docker',x,y-13,8,True,color=TEAL); y-=30
    for s in ['API REST con PostgreSQL, autenticacion JWT y control de acceso por roles.','Calculo de nominas con Decimal y generacion de documentos PDF con WeasyPrint.','Repositorio: github.com/vititoOX/NominaHub']: y=bullet(c,s,x,y,w)-3
    y-=8; t(c,'Cafeteria Escolar',x,y,12,True); t(c,'React · Vite · JavaScript · Material UI',x,y-13,8,True,color=TEAL); y-=30
    for s in ['Interfaz web para gestionar pedidos en una cafeteria escolar.','Componentes reutilizables y navegacion entre vistas enfocada al flujo de usuario.']: y=bullet(c,s,x,y,w)-3
    y-=8; y=heading(c,'Experiencia',x,y,w)
    t(c,'Practicas profesionales Full-Stack Developer',x,y,11,True); t(c,'Edosoft Factory · 2023 - 2024',x,y-13,8,True,color=TEAL); y-=30
    for s in ['Practicas profesionales de desarrollo full-stack.']: y=bullet(c,s,x,y,w)-3
    y-=6; t(c,'Recepcionista de hotel',x,y,11,True); t(c,'Actualidad · Gran Canaria, Espana',x,y-13,8,True,color=TEAL); y-=30
    for s in ['Atencion a clientes y gestion de incidencias en un entorno de turnos.','Actualizacion precisa de reservas y datos de huespedes; organizacion y priorizacion de tareas.']: y=bullet(c,s,x,y,w)-3
    c.save(); print(PDF)
if __name__=='__main__': main()
