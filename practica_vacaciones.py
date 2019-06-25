nombre =input("Ingrese su nombre: ")

#print("Bienvenido ", nombre, ".\n")
deseo = input("Desea trabajar o ir de vacaciones: ")


if deseo == "vacaciones":

	print ("Le ofrecemos los siguientes destinos: 1. Cancun, 2. Costa Rica. 3. México\n")
	preferencia = int(input("Elija la opción de su preferencia: "))
24/6/19
19:20	No R interpreter defined: Many R related features like completion, code checking and help won't be available. You can set an interpreter under Preferences->Languages->R

19:20	Сannot Run Git
				File not found: git
				Download Configure...24/6/19
19:20	No R interpreter defined: Many R related features like completion, code checking and help won't be available. You can set an interpreter under Preferences->Languages->R

19:20	Сannot Run Git
				File not found: git
				Download Configure...


	if preferencia == 1:
		print("El precio de su destino es $800 ")
	if preferencia == 2:
		print("El precio de su destino es $500"24/6/19
19:20	No R interpreter defined: Many R related features like completion, code checking and help won't be available. You can set an interpreter under Preferences->Languages->R

19:20	Сannot Run Git
				File not found: git
				Download Configure...
)
	if preferencia==3:
		print("El precio de su destino es $100")
	
elif deseo == "trabajar":
	print ("Le ofrecemos los siguientes tipos de café: 1. Expreso, 2. Capuchino. 3. Café con leche\n")
	cafe = int(input("Elija la opción de su preferencia: "))

	if cafe == 1:
		print("El precio de su café es $800 ")
	if cafe == 2:
		print("El precio de su café es $500")
	if cafe==3:
		print("El precio de su café es $100")





