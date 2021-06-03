import PySimpleGUI as sg;

class TelaPython:
	def __init__(self):
		# Layout
		layout = [
			[sg.Text('Name:',size=(5,0)),sg.Input(size=(40,0))],
			[sg.Text('Age:',size =(5,0)),sg.Input(size=(40,0))],
			[sg.Checkbox('one',size=(13,0)), sg.Checkbox('two', size=(13,0)),sg.Checkbox('three')],
			#[sg.Radio('oneR'), sg.Radio('twoR'), sg.Radio('threeT')],
			[sg.Button("Send informations", border_width=3, button_color=('white', 'green'))],
			#[sg.Quit(button_color=('black', 'orange'))],
		]
		# Janela
		janela = sg.Window("Dados do Usuário").layout(layout);
		# Extrair os dados da tela
		self.button, self.values = janela.Read();

	def iniciar(self):
		print(self.values)


#Documentação: https://pysimplegui.readthedocs.io/en/latest/

