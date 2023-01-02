import os

# définition de la classe PageMaker:

class PageMaker:

     #attributs:

     __entry_file = ""

    # définition du contsructeur qui prend une entree csv au format de deniro:
    def __init__(self, entry_file= "deniro.csv"):
        self.__entry_file = entry_file
         
        

    #la méthdode generate-html pour générer les pages htmls pour chaque film:    

    def generate_html(self, file_destination):
        
        file_path = self.__entry_file

        with open(file_path, 'r') as f:
             # je lis le contenu du fichier csv.
    
             rows = csv.reader(f, delimiter=',')
            # j'invoque la méthode next() pour sauter la première ligne contenant le nom des colonnes.
             next(rows)

            for r in rows:
                with open("template.html", "w") as f2:
                    content = f2.read()
                    f2.close()
                    newcontent = content.teplace("[Title]", "r[2]" )
                    newcontent = content.teplace("[Year]", "r[0]" )
                    newcontent = content.teplace("[Score]", "r[1]" )

                    f3 = open("file_destination"+ "/" + r[2][2:-1],"w")
                    f3.write(newcontent)
                    f3.close()





              

                
            
       

       

