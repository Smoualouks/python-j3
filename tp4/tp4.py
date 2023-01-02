import csv, os

# définition de la classe PageMaker:

class PageMaker:

     #propritées:

     __entry_file = "deniro.csv"

    # définition du contsructeur qui prend une entree csv au format de deniro:
     def __init__(self, entry_file = "deniro.csv"):
         self.__entry_file = entry_file
         
     # guetteur :

     def get_entry_file(self, __entry_file):
       return self.__entry_file
        

    #la méthdode generate-html pour générer les pages htmls pour chaque film:    

     def generate_html(self, file_destination):
        
        file_path = self.__entry_file()
    
        with open(file_path, 'r') as f:
             # je lis le contenu du fichier csv.
    
             rows = csv.reader(f, delimiter=',')
            # j'invoque la méthode next() pour sauter la première ligne contenant le nom des colonnes.
             next(rows)

             for r in rows:
                f2 = open("template.html", "r")
                content = f2.read()
                f2.close()
                newcontent = content.replace("[Title]", "r[2]" )
                newcontent = content.replace("[Year]", "r[0]" )
                newcontent = content.replace("[Score]", "r[1]" )

                f3 = open("file_destination"+ "/" + r[2][2:-1],"w")
                f3.write(newcontent)
                f3.close()


              
pm = PageMaker("deniro.csv")
pm.generate_html("/tmp")




                
            
       

       

