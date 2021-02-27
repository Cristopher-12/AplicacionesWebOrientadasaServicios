import web
import json
urls = (
    '/personas?', 'Personas'
)
app = web.application(urls, globals())

class Personas:


    def __init__(self):
      pass
        
     
    def GET(self):
        try:
            parametros = web.input() 
            nombre = parametros.nombre
            dia = int(parametros.dia)
            mes = parametros.mes
            año_nac = int(parametros.año_nac)
            edad = 2021 - año_nac
            data={}
            data["Nombre"] = nombre
            data["Día"] = dia
            data["Mes"] = mes
            data["Año de nacimiento"] = año_nac
            data["Edad"] = edad
            archivo = open("static/","a")
            archivo.write("\n")
            archivo.write(str(data))
            archivo.close()
            return json.dumps(data)

        except:
          data = {}
          data["mensaje"] = "Revisa tus datos ingresados"
          return json.dumps(data)
       
            

if __name__ == "__main__":
  app.run()

