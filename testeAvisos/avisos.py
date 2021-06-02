def atencao():
	#teste
	print("\nQuer acessar esta merda antes de estudar FDP\n");

class TesteClasse:
	"""docstring for TesteClasse"""
	def __init__(self, frase:"Posso pressentir o perigo e o caos"):
		self.frase = frase;
		
	def verificarSeAFrasesContemA(self):
		#print("Digite uma frase:");
		if 'a' in self.frase:
			print("\nYeah, the caracter 'A' is into the pharse");
			return "Yeah";
		
		else:
			print("\nNo, the caracter 'A' isn't into the pharse");
			return "No";

#Herança:
class testeHeranca(TesteClasse):
	pass
		