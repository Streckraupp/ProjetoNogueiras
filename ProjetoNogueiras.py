import streamlit as st
import csv
from os import path

#import gspread
#from google.oauth2.service_account import Credentials
#from gspread_pandas import Spread, Client

#acessar google drive
#scope = ['https://spreadsheets.google.com/feeds',
#         'https://www.googleapis.com/auth/drive']
#credentials = Credentials.from_service_account_file('./projetonogueiras-a2ce8a460873.json', scopes=scope) #credencial pra acessar o google sheets
#client = Client(scope=scope, creds=credentials)
#spread = Spread("Testing", client=client) #nome da planilha aqui, entre aspas
#spread.df_to_sheet(stocks_df[cols_to_keep]) #como salvar pra google sheets
#df = spread.sheet_to_df(index = None, header_rows = None) #como carregar um google sheets pra pandas dataframe

#configurações da página
st.set_page_config(page_title = "Projeto Nogueiras", layout="centered")

st.title('Projeto Nogueiras')

encod = 'latin-1'

st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
query_params = st.experimental_get_query_params()
tabs = ["Gráficos", "Novo custo", "Nova entrada", "Nova opção de custo"] #quaisquer novas tabs vão entrar aqui
if "tab" in query_params:
    active_tab = query_params["tab"][3]
else:
    active_tab = "Gráficos"

if active_tab not in tabs:
    st.experimental_set_query_params(tab="Gráficos")
    active_tab = "Gráficos"

li_items = "".join(
    f"""
    <li class="nav-item">
        <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
    </li>
    """
    for t in tabs
)
tabs_html = f"""
    <ul class="nav nav-tabs">
    {li_items}
    </ul>
"""

st.markdown(tabs_html, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

#primeira tab
if active_tab == "Gráficos":
	st.error('Página em desenvolvimento')
	#st.write("# Welcome to my lovely page!")
	#st.write("## Feel free to *play* **with** ***this*** ephemeral slider!")
	#slider_element = st.empty()
	#if st.button('Reset'):
	#	st.session_state['key'] = 50
	#slider_element.slider(
	#	"Does this get preserved? You bet it doesn't!",
	#	min_value=0,
	#	max_value=100,
	#	value=50,
	#	key = 'key'
	#)

#segunda tab
elif active_tab == "Novo custo":
	container = st.beta_container() #coloquei tudo num container para poder criar o botão de reset logo em seguida. Depois preencho esse container
	
	if st.button('Resetar as opções'):
		st.session_state['categoria'] = '' #valor que a opção 'categoria' deve retornar ao clicar no botão resetar
		st.session_state['valor'] = '' #valor que a caixa de texto 'valor ' deve retornar ao clicar no botão resetar
		st.session_state['mes'] = 1 #valor que a opção 'mes' deve retornar ao clicar no botão resetar
		st.session_state['ano'] = 2015 #valor que a opção 'ano' deve retornar ao clicar no botão resetar
	
	with container: #preenchendo o container
		st.write('#### Adição de novos custos')
		st.write('Aba referente ao lançamento de quaisquer novos custos ao projeto')
		#ANO / MES / VALOR / CATEGORIA / TIPO-PRODUTO-OU-PESSOA / SUBTIPO / MARCA / TEMPO / QUANTIDADE
		new_data = [None, None, None, None, None, None, None, None, None] #inicializando um dado vazio
		with open('Categorias.csv', 'r', encoding = encod) as f:
			cathegory_options = f.read()
			cathegory_options = cathegory_options.split('\n')
			cathegory_options.sort()
		new_data[3] = st.selectbox('Selecione a categoria do custo:', options = cathegory_options, index = 0, key = 'categoria')
		if new_data[3] == 'Mão de Obra':
			with open(str(new_data[3]) + '.csv', 'r', encoding = encod) as f:
				opt = f.read()
				opt = opt.split('\n')
				opt.sort()
			esquerda, direita = st.beta_columns(2)
			new_data[4] = esquerda.selectbox('Selecione a pessoa:', options = opt, index = 0)
			new_data[7] = direita.text_input('Preencha o tempo de serviço')
		elif new_data[3] == 'Aluguel':
			with open(str(new_data[3]) + '.csv', 'r', encoding = encod) as f:
				opt = f.read()
				opt = opt.split('\n')
				opt.sort()
			esquerda, direita = st.beta_columns(2)
			new_data[4] = esquerda.selectbox('Selecione o tipo de equipamento alugado:', options = opt, index = 0)
			new_data[7] = direita.text_input('Preencha o tempo de aluguel, em horas:')
		elif new_data[3] == 'Consultoria':
			with open(str(new_data[3]) + '.csv', 'r', encoding = encod) as f:
				opt = f.read()
				opt = opt.split('\n')
				opt.sort()
			new_data[4] = st.selectbox('Selecione o tipo de consultoria:', options = opt, index = 0)
		elif new_data[3] == 'Manutenção':
			with open(str(new_data[3]) + '.csv', 'r', encoding = encod) as f:
				opt = f.read()
				opt = opt.split('\n')
				opt.sort()
			new_data[4] = st.selectbox('Selecione o que recebeu manutenção:', options = opt, index = 0)
		elif new_data[3] == 'EPI':
			with open(str(new_data[3]) + '.csv', 'r', encoding = encod) as f:
				opt = f.read()
				opt = opt.split('\n')
				opt.sort()
			esquerda, direita = st.beta_columns(2)
			new_data[4] = esquerda.selectbox('Selecione o tipo de EPI:', options = opt, index = 0)
			new_data[8] = direita.text_input('Preencha a quantidade de EPIs comprados:')
		elif new_data[3] == 'Sanidade':
			with open(str(new_data[3]) + '.csv', 'r', encoding = encod) as f:
				opt = f.read()
				opt = opt.split('\n')
				opt.sort()
			with open(str(new_data[3]) + '_Composição.csv', 'r', encoding = encod) as f:
				opt1 = f.read()
				opt1 = opt1.split('\n')
				opt1.sort()
			with open(str(new_data[3]) + '_Marca.csv', 'r', encoding = encod) as f:
				opt2 = f.read()
				opt2 = opt2.split('\n')
				opt2.sort()
			esquerda, centro, meio, direita = st.beta_columns(4)
			new_data[4] = esquerda.selectbox('Selecione o tipo:', options = opt, index = 0)
			new_data[5] = centro.selectbox('Selecione o subtipo:', options = opt1, index = 0)
			new_data[6] = meio.selectbox('Selecione a marca:', options = opt2, index = 0)
			new_data[8] = direita.text_input('Preencha a quantidade:')
		elif new_data[3] == 'Adubação':
			with open(str(new_data[3]) + '.csv', 'r', encoding = encod) as f:
				opt = f.read()
				opt = opt.split('\n')
				opt.sort()
			with open(str(new_data[3]) + '_Marca.csv', 'r', encoding = encod) as f:
				opt2 = f.read()
				opt2 = opt2.split('\n')
				opt2.sort()
			esquerda, meio, direita = st.beta_columns(3)
			new_data[4] = esquerda.selectbox('Selecione o tipo:', options = opt, index = 0)
			new_data[6] = meio.selectbox('Selecione a marca:', options = opt2, index = 0)
			new_data[8] = direita.text_input('Preencha a quantidade:')
			if new_data[4] == 'Adubo inorgânico':
				with open(str(new_data[3]) + '_Composição.csv', 'r', encoding = encod) as f:
					opt1 = f.read()
					opt1 = opt1.split('\n')
					opt1.sort()
				new_data[5] = st.selectbox('Selecione a composição do adubo:', options = opt1, index = 0)
		elif new_data[3] == 'Gastos Únicos':
			with open(str(new_data[3]) + '.csv', 'r', encoding = encod) as f:
				opt = f.read()
				opt = opt.split('\n')
				opt.sort()
			esquerda, direita = st.beta_columns(2)
			new_data[4] = esquerda.selectbox('Selecione o tipo de gasto único:', options = opt, index = 0)
			if new_data[4] == 'Aquisição de maquinário':
				opt2 = ['', 'Máquina 1', 'Máquina 2']
				new_data[5] = direita.selectbox('Selecione o tipo de maquinário adquirido:', options = opt2, index = 0)
			if new_data[4] == 'Aquisição de ferramenta':
				opt2 = ['', 'Ferramenta1']
				new_data[5] = direita.selectbox('Selecione o tipo de ferramenta adquirida:', options = opt2, index = 0)
			elif new_data[4] == 'Benfeitoria':
				opt2 = ['', 'Estrada', 'Açude']
				new_data[5] = direita.selectbox('Selecione o tipo de benfeitoria:', options = opt2, index = 0)
			elif new_data[4] == 'Aquisição de mudas':
				new_data[8] = direita.text_input('Preencha o número de mudas adquiridas:')
		mes, ano = st.beta_columns(2)
		new_data[1] = mes.selectbox('Selecione o mês referente à esse custo:', options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], index = 0, key = 'mes')
		new_data[0] = ano.selectbox('Selecione o ano referente à esse custo:', options = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025], index = 0, key = 'ano')
		if new_data[3] != '':
			new_data[2] = st.text_input('Preencha o valor total desse custo:', key = 'valor')
			#convertendo os dados de custo, tempo e quantidade de texto para números
			if (new_data[2] != '') and (new_data[2] != None):
				new_data[2] = float(new_data[2].replace(',', '.'))
			if (new_data[7] != '') and (new_data[7] != None):
				new_data[7] = float(new_data[7].replace(',', '.'))
			if (new_data[8] != '') and (new_data[8] != None):
				new_data[8] = float(new_data[8].replace(',', '.'))
			if new_data[2]:
				st.write('Por favor, verifique novamente se os dados inseridos estão corretos')
				st.write('Deseja inserir o custo acima na planilha?')
				esq, dir, _, _, _, _, _, _, _, _ = st.beta_columns(10)
				dir.button('Não')
				if esq.button('Sim'):
					with open('Dados.csv', 'a+', newline = '', encoding = encod) as f:
						writer = csv.writer(f, delimiter = ';')
						writer.writerow(new_data)
					st.write('Custo adicionado à planilha com sucesso!')
					st.write('Resete as opções através do botão abaixo para inserir um novo custo.')

#terceira tab
elif active_tab == "Nova entrada":
    st.error('Página em desenvolvimento')
	#st.write("If you'd like to contact me, then please don't.")
	#st.write("""
	# Simple stock price APP

	#Shown are the stock closing price and volume of Google! OMG!

	#""")

	#tickerSymbol = 'GOOGL'

	#tickerData = yf.Ticker(tickerSymbol)

	#tickerDf = tickerData.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

	#st.line_chart(tickerDf.Close)
	#st.line_chart(tickerDf.Volume)

elif active_tab == "Nova opção de custo":
	container = st.beta_container()

	if st.button('Resetar as opções'):
		st.session_state['categoria'] = '' #valor que a opção 'categoria' deve retornar ao clicar no botão resetar
			
	with container:
		st.write('#### Criar uma nova opção de custo.')
		#st.write('Aba referente à criação de uma nova opção de custo, que poderá ser utilizada na aba "Novo custo"')
		#spread = Spread("Categorias", client=client)
		#cathegory_options = spread.sheet_to_df(index = None, header_rows = None)
		#cathegory_options.append(pd.DataFrame(['']), ignore_index = True)
		#cathegory_options = cathegory_options.sort_values(by = 0).reset_index().iloc[:,1]
		#st.write(cathegory_options)
		with open('Categorias.csv', 'r', encoding = encod) as f:
			cathegory_options = f.read()
			cathegory_options = cathegory_options.split('\n')
			cathegory_options.sort()
		categoria = st.selectbox('Selecione a categoria do custo:', options = cathegory_options, index = 0, key = 'categoria')
		#verificar se a categoria têm a possibilidade de adicionar uma nova opção de custo
		if categoria != '' and categoria != 'Combustível' and categoria != 'Frete':
			if categoria != 'Adubação' and categoria != 'Sanidade' and categoria != 'Gastos Únicos':
				if path.isfile(str(categoria) + '.csv'):
					with open(str(categoria) + '.csv', 'r', encoding = encod) as f:
						content = f.read()
						content = content.split('\n')
					if len(content) > 1:
						st.write('Opções já existentes na categoria:')
						st.write(content)
					else:
						st.write('Essa categoria ainda não dispõe de opções.')
				else:
					st.write('Essa categoria ainda não dispõe de opções.')
				new_data = st.text_input('Por favor, preencha a nova opção a ser adicionada:')
				if new_data:
					st.write('Deseja realmente adicionar a opção \"' + new_data + '\" à lista de opções da categoria \"' + categoria + '\"?')
					esq, dir, _, _, _, _, _, _, _, _ = st.beta_columns(10)
					dir.button("Não")
					if esq.button('Sim'):
						with open(str(categoria) + '.csv', 'a+', newline = '', encoding = encod) as f:
							writer = csv.writer(f, delimiter = ';')
							writer.writerow([new_data])
						st.write('Opção de custo adicionada com sucesso!')
						st.write('Resete as opções através do botão abaixo para inserir uma nova opção de custo.')
			elif categoria == 'Adubação':
				opcao = st.selectbox('Selecione o que você deseja adicionar à categoria Adubação:', options = ['Produto', 'Composição', 'Marca'], index = 0)
				artigo = 'a'
				opcao2 = '_' + opcao
				if opcao == 'Produto':
					opcao2 = ''
					artigo = 'o'
				if path.isfile(str(categoria) + str(opcao2) + '.csv'):
					with open(str(categoria) + str(opcao2) + '.csv', 'r', encoding = encod) as f:
						content = f.read()
						content = content.split('\n')
					if len(content) > 1:
						st.write('Opções já existentes nessa opção dessa categoria:')
						st.write(content)
					else:
						st.write('Essa opção dessa categoria ainda não dispõe de opções.')
				else:
					st.write('Essa opção dessa categoria ainda não dispõe de opções.')
				new_data = st.text_input('Por favor, preencha ' + artigo + ' nov' + artigo + ' ' + opcao + ' a ser adicionad' + artigo + ':')
				if new_data:
					st.write('Deseja realmente adicionar a opção \"' + new_data + '\" à lista de tipos de ' + opcao + ' da categoria \"' + categoria + '\"?')
					esq, dir, _, _, _, _, _, _, _, _ = st.beta_columns(10)
					dir.button('Não')
					if esq.button('Sim'):
						with open(str(categoria) + str(opcao2) + '.csv', 'a+', newline = '', encoding = encod) as f:
							writer = csv.writer(f, delimiter = ';')
							writer.writerow([new_data])
						st.write('Opção de custo adicionada com sucesso!')
						st.write('Resete as opções através do botão abaixo para inserir uma nova opção de custo.')
			elif categoria == 'Sanidade':
				opcao = st.selectbox('Selecione o que você deseja adicionar à categoria Sanidade:', options = ['Produto', 'Composição', 'Marca'], index = 0)
				artigo = 'a'
				opcao2 = '_' + opcao
				if opcao == 'Produto':
					opcao2 = ''
					artigo = 'o'
				if path.isfile(str(categoria) + str(opcao2) + '.csv'):
					with open(str(categoria) + str(opcao2) + '.csv', 'r', encoding = encod) as f:
						content = f.read()
						content = content.split('\n')
					if len(content) > 1:
						st.write('Opções já existentes nessa opção dessa categoria:')
						st.write(content)
					else:
						st.write('Essa opção dessa categoria ainda não dispõe de opções.')
				else:
					st.write('Essa opção dessa categoria ainda não dispõe de opções.')
				new_data = st.text_input('Por favor, preencha ' + artigo + ' nov' + artigo + ' ' + opcao + ' a ser adicionad' + artigo + ':')
				if new_data:
					st.write('Deseja realmente adicionar a opção \"' + new_data + '\" à lista de tipos de ' + opcao + ' da categoria \"' + categoria + '\"?')
					esq, dir, _, _, _, _, _, _, _, _ = st.beta_columns(10)
					dir.button('Não')
					if esq.button('Sim'):
						with open(str(categoria) + str(opcao2) + '.csv', 'a+', newline = '', encoding = encod) as f:
							writer = csv.writer(f, delimiter = ';')
							writer.writerow([new_data])
						st.write('Opção de custo adicionada com sucesso!')
						st.write('Resete as opções através do botão abaixo para inserir uma nova opção de custo.')
			elif categoria == 'Gastos Únicos':
				opcao = st.selectbox('Selecione o que você deseja adicionar à categoria Gastos Únicos:', options = ['Tipo', 'Subtipo'], index = 0)
				if opcao == 'Tipo':
					artigo = 'o'
					opcao2 = ''
					if path.isfile(str(categoria) + str(opcao2) + '.csv'):
						with open(str(categoria) + str(opcao2) + '.csv', 'r', encoding = encod) as f:
							content = f.read()
							content = content.split('\n')
						if len(content) > 1:
							st.write('Opções já existentes nessa opção dessa categoria:')
							st.write(content)
						else:
							st.write('Essa opção dessa categoria ainda não dispõe de opções.')
					else:
						st.write('Essa opção dessa categoria ainda não dispõe de opções.')
					new_data = st.text_input('Por favor, preencha ' + artigo + ' nov' + artigo + ' ' + opcao + ' a ser adicionad' + artigo + ':')
					if new_data:
						st.write('Deseja realmente adicionar a opção \"' + new_data + '\" à lista de tipos de ' + opcao + ' da categoria \"' + categoria + '\"?')
						esq, dir, _, _, _, _, _, _, _, _ = st.beta_columns(10)
						dir.button('Não')
						if esq.button('Sim'):
							with open(str(categoria) + str(opcao2) + '.csv', 'a+', newline = '', encoding = encod) as f:
								writer = csv.writer(f, delimiter = ';')
								writer.writerow([new_data])
							st.write('Opção de custo adicionada com sucesso!')
							st.write('Resete as opções através do botão abaixo para inserir uma nova opção de custo.')
				else:
					with open(str(categoria) + '.csv', 'r', encoding = encod) as f:
						opt = f.read()
						opt = opt.split('\n')
						opt.sort()
					tipo = st.selectbox('Selecione o tipo de Gasto Único para o qual você deseja adicionar um novo subtipo:', options = opt, index = 0)
					if tipo == 'Aquisição de terra' or tipo == 'Aquisição de mudas':
						st.write('Esse tipo não requer um subtipo.')
					elif tipo != '':
						artigo = 'a'
						opcao2 = '_' + tipo
						if path.isfile(str(categoria) + str(opcao2) + '.csv'):
							with open(str(categoria) + str(opcao2) + '.csv', 'r', encoding = encod) as f:
								content = f.read()
								content = content.split('\n')
							if len(content) > 1:
								st.write('Opções já existentes nessa opção dessa categoria:')
								st.write(content)
							else:
								st.write('Essa opção dessa categoria ainda não dispõe de opções.')
						else:
							st.write('Essa opção dessa categoria ainda não dispõe de opções.')
						new_data = st.text_input('Por favor, preencha ' + artigo + ' nov' + artigo + ' ' + tipo + ' a ser adicionad' + artigo + ':')
						if new_data:
							st.write('Deseja realmente adicionar a opção \"' + new_data + '\" à lista de tipos de ' + tipo + ' da categoria \"' + categoria + '\"?')
							esq, dir, _, _, _, _, _, _, _, _ = st.beta_columns(10)
							dir.button('Não')
							if esq.button('Sim'):
								with open(str(categoria) + str(opcao2) + '.csv', 'a+', newline = '', encoding = encod) as f:
									writer = csv.writer(f, delimiter = ';')
									writer.writerow([new_data])
								st.write('Opção de custo adicionada com sucesso!')
								st.write('Resete as opções através do botão abaixo para inserir uma nova opção de custo.')
			else:
				st.error("Algo de errado ocorreu.")
		elif categoria != '':
			st.write('Essa categoria não necessita de opções.')
			st.write('Não há necessidade de criar uma nova opção de custo.')

else:
    st.error("Algo de errado ocorreu.")
