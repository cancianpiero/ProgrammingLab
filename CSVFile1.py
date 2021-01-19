#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#venga inizializzato sul nome del file csv, e
#abbia un attributo “name” che ne contenga il nome
#abbia un metodo “get_data” che torni i dati dal file CSV come
#numeri di una lista (come abbiamo già visto).

# oggetto CSVFile
#   - init(filename)
#   - name
#   - get_data
#     return get_data

class CSVFile
    
    def __init__(self, name):
        self.name = name

    def get_data(self):
        return [1,2,3,4]    

mio_file = CSVFile(name='shampoo_sales.csv')

print(mio_file.filename)
print(mio_file.get_data())
