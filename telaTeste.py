import PySimpleGUI as sg;


class TelaPython:
	def __init__(self):
		# Layout
		layout = [
			[sg.Text('Name:',size=(5,0)),sg.Input(size=(40,0), key='name')],
			[sg.Text('Age:',size =(5,0)),sg.Input(size=(40,0), key='age')],
			#Testando checkbox
			[sg.Checkbox('one',size=(13,0)), sg.Checkbox('two', size=(13,0)),sg.Checkbox('three')],
			#Testando radio
			[sg.Radio('oneR', 'radio', size=(13, 13)), sg.Radio('twoR', 'radio', size=(13, 13)), sg.Radio('threeR', 'radio')],
			[sg.Button("Send informations", border_width=3, button_color=('white', 'green'))],
			#[sg.Quit(button_color=('black', 'orange'))],
		]
		# Janela
		self.janela = sg.Window("Dados do Usuário").layout(layout);
		# Extrair os dados da tela


	def iniciar(self):
		print(self.values)

	def printOutData(self):
		while True:
			self.button, self.values = self.janela.Read();		
			print("Nome: " + self.values['name']);
			print("Idade: " + self.values['age']);
#Documentação: https://pysimplegui.readthedocs.io/en/latest/