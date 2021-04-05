import web
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

urls = (
    '/datos?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros:
  json_file = {}
  
  def GET(self):
      parametros = web.input()
      action = parametros.action
      if action == "get":
        return self.read()
      elif action == "put":
        nombre = parametros.nombre
        fecha_naci = parametros.fecha_naci
        return self.write(nombre, fecha_naci)
  
  def write (self, nombre,fecha_naci):
    try:
      fecha_nacimiento = datetime.strptime(fecha_naci, "%d-%m-%Y") #//fecha
      edad = relativedelta(datetime.now(), fecha_nacimiento) #Almacene valores en edad
      edad = (f"{edad.years} years.")
      datos = {
      "nombre" : nombre,
      "fecha_naci" : fecha_naci,
      "edad" : edad
      }
      try:
        with open("datos.json") as file:
          self.json_file = json.load(file)
          self.json_file["datospersona"].append(datos)
          with open("datos.json","w") as file:
            json.dump(self.json_file, file)
            return json.dumps(datos)

      except  Exception as error:
        print("Error {}".format(error.args[0]))
            
    except  Exception as error:
      print("Error {}".format(error.args[0]))
  

  def read(self):
        with open("datos.json") as file:
            self.json_file = json.load(file)
            return json.dumps(self.json_file)
        

if __name__ == "__main__":
    app.run()