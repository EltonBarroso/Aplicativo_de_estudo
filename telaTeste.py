import PySimpleGUI as sg;

class TelaPython:
	def __init__(self):
		# Layout
		layout = [
			[sg.Text('Nome'),sg.Input()],
			[sg.Text('Idade'),sg.Input()],
			[sg.Button("Pegar Informações")],
		]
		# Janela
		janela = sg.Window("Dados do Usuário").layout(layout);
		# Extrair os dados da tela
		self.button, self.values = janela.Read();

	def iniciar(self):
		print(self.values)




