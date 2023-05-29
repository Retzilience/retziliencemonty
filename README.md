# Retzilience's Quantum Monty Hall Playground

## Language

## [For English, click here.](#english-version)
## [Em Português, clique aqui.](#versao-em-portugues)

# <a name="english-version"></a>Quantum Choices and the Monty Hall Problem: A Study in Probabilistic Decision Making

![Retzchoice](https://github.com/Retzilience/retziliencemonty/blob/main/retzchoice.png)

Welcome to the _Monty Hall Retzilience Simulator_! This is not just another Monty Hall problem simulator, it is an adventure in the quantum landscape of choices and probabilities. Let's unravel the Monty Hall problem, but this time with a flavor of quantum mechanics.

## The Classic Monty Hall Problem

Here's the classic setup: you're on a game show with three doors. Behind one door is a car; behind the other two, goats. You pick a door, say, Door #1. Now, the host, who knows what's behind the doors, opens another door, say, Door #3, which has a goat. Now he gives you a choice: do you want to stick with your original choice (Door #1) or switch to the remaining unopened door (Door #2)?

As counter-intuitive as it may seem, the best strategy is to **always switch**. By switching, your probability of winning the car goes up to 2/3, as opposed to sticking with your original choice which has a probability of 1/3.

## The Quantum Choice Perspective

Much like the quantum world, where particles exist in multiple states until observed, the car is behind all the doors until Monty opens a door. In other words, the Monty Hall problem exhibits a form of _quantum superposition_ - multiple potential realities existing simultaneously. The act of Monty opening a door is akin to the observation that 'collapses' this superposition, leaving us with a new set of probabilities.

## But What if We Increase the Number of Doors?

If three doors make you scratch your head, how about a hundred? Or a thousand? The core idea behind this simulator is to take the Monty Hall problem to the extreme. When you increase the number of doors, the benefit of switching becomes exponentially apparent and confirms what was once counter-intuitive as something fundamentally intuitive. And this is precisely what our _Monty Hall Retzilience Simulator_ does - it allows you to simulate the game with as many doors and trials as you'd like.

## The Power of Simulation

The _Monty Hall Retzilience Simulator_ combines the power of Python's random module with the intuitive graphical user interface of tkinter, providing an engaging and insightful way to explore this problem. The program simulates thousands of Monty Hall games in a matter of seconds, collecting data on the outcomes based on whether you stick or switch. This way, you can see the surprising power of the switching strategy in action.

Remember, probability isn't just theory - it's reality playing out. And our simulator is a sandbox where this reality unfolds. The Monty Hall problem is a beautiful demonstration of how our intuition can often lead us astray in the face of hard probabilistic truth. By simulating the problem, we don't just understand it - we experience it.

## Wrapping Up

The Monty Hall problem is a fascinating journey into the world of probability, and our simulator serves as your tour guide. By allowing for an arbitrary number of doors and trials, it illuminates the counter-intuitive reality of the problem. It is not just a program; it's a digital playground to experience the whimsical world of quantum choices. So go ahead, step into the quantum landscape of doors, and remember, sometimes it's wiser to switch!

![GUI](https://github.com/Retzilience/retziliencemonty/blob/main/GUI.png)

# Setting Up and Running the Monty Hall Retzilience Simulator: A Friendly Guide

Welcome to the fun part! Let's get the Monty Hall Retzilience Simulator up and running on your machine. Don't worry if you're a newbie to coding, this is a no-jargon zone! Follow these steps, and you'll have it running in no time.

## Step 1: Installing Python

First things first, we need to make sure Python is installed on your system. Here's how:

### Windows:

1. Visit the [Python downloads page](https://www.python.org/downloads/windows/).
2. Click on the latest Python release.
3. Download and run the installation package.
4. Make sure to tick the box that says "Add Python to PATH" before clicking on Install.

### MacOS:

1. Open Terminal (you can find it in Applications -> Utilities).
2. Type in `brew install python3` and hit Enter (you need to have Homebrew installed, a handy package manager for MacOS. If you don't, head over to the [Homebrew site](https://brew.sh/) and follow the instructions there).
3. Wait for the magic to happen!

### Linux:

1. Open Terminal.
2. Type `sudo apt-get install python3.8` and hit Enter.
3. Type in your password when prompted and wait for Python to be installed.

## Step 2: Installing Anaconda Navigator

Anaconda Navigator is a great tool that simplifies the management of Python packages and environments. It also comes with Tkinter, a library needed for our script to run. Here's how to install it:

1. Visit the [Anaconda distribution page](https://www.anaconda.com/distribution/).
2. Download the installer for your operating system and follow the installation instructions provided there.

## Step 3: Cloning the Repository

We've stored the Monty Hall Retzilience Simulator script in a GitHub repository. To copy this repository to your local machine, follow these steps:

1. Navigate to the GitHub repository page ( https://github.com/Retzilience/retziliencemonty ).
2. Click on the 'Code' button and copy the URL shown.
3. Open Terminal (or Command Prompt for Windows users).
4. Navigate to the location where you want to clone the repository by typing `cd path_to_your_directory`. 
5. Type `git clone ` and paste the URL you copied from the GitHub page.
6. Press Enter to clone the repository.

## Step 4: Setting up the Log File

Our simulator keeps track of each simulation in a log file. You need to set the path to where this file will be created:

1. Open the cloned `retziliencemonty.py` file in a text editor.
2. Look for the line `LOG_FILE = '/your_path/montylog.txt'`.
3. Replace `'/your_path/montylog.txt'` with the path where you want the log file to be created, e.g., `'/Users/YourName/Documents/montylog.txt'` for MacOS or `'C:/Users/YourName/Documents/montylog.txt'` for Windows.
4. Save and close the file.

## Step 5: Running the Simulator

Now, it's time to bring our simulator to life!

1. Open Anaconda Navigator.
2. Click on the 'Environments' tab.
3. Find 'base(root)' in the list and click on the play button on the right.
4. Select 'Open Terminal'.
5. In the Terminal, navigate to the location of the `retziliencemonty.py` file using the `cd` command.
6. Type `python3 retziliencemonty.py` and hit Enter.

Congratulations! You're now running

 the Monty Hall Retzilience Simulator! Enter the number of doors and trials, and witness the magic of probability unfold!

Remember, there are no goats or cars behind the doors, just quantum probabilities waiting to be unraveled. Happy exploring!

## Code Overview

The script defines a `MontyHallApp` class, which is responsible for setting up the GUI and running the simulation. The GUI is composed of a few labels and input fields for the user to specify the parameters of the simulation (i.e., the number of doors and trials), and a button to run the simulation.

The simulation itself is implemented in the `run_simulation` method, which reads the input parameters, performs the specified number of trials, and calculates the probabilities of winning if the contestant decides to stick with their initial choice or always switch doors.

Each trial is performed by the `simulate_game` method, which randomly places the prize behind one of the doors and simulates the contestant's choices and the host's actions according to the rules of the game. The method returns a pair of boolean values indicating whether the contestant would win if they stuck with their initial choice and if they switched doors, respectively.

Finally, the simulation results are displayed in a message box and, if logging is enabled, appended to a log file.

## Logging

The script supports optional logging of the simulation results. To enable logging, set the `LOGGING_ENABLED` variable to `True` and specify the path to the log file in the `LOG_FILE` variable. With logging enabled, the script will append the results of each simulation to the log file in addition to displaying them in the GUI.

# <a name="versao-em-portugues"></a>Escolhas Quânticas e o Problema de Monty Hall: Um Estudo em Tomada de Decisão Probabilística

![Retzchoice](https://github.com/Retzilience/retziliencemonty/blob/main/retzchoice.png)

Bem-vindo ao _Simulador de Retzilience de Monty Hall_! Este não é apenas mais um simulador do problema de Monty Hall, é uma aventura na paisagem quântica de escolhas e probabilidades. Vamos desvendar o problema de Monty Hall, mas desta vez com um sabor de mecânica quântica.

## O Clássico Problema de Monty Hall

Aqui está a configuração clássica: você está em um programa de jogos com três portas. Atrás de uma porta há um carro; atrás das outras duas, cabras. Você escolhe uma porta, digamos, a porta #1. Agora, o apresentador, que sabe o que está por trás das portas, abre outra porta, digamos, a porta #3, que tem uma cabra. Agora ele te dá uma escolha: você quer ficar com sua escolha original (Porta #1) ou mudar para a porta restante não aberta (Porta #2)?

Por mais contra-intuitivo que possa parecer, a melhor estratégia é **sempre mudar**. Ao mudar, sua probabilidade de ganhar o carro sobe para 2/3, ao contrário de ficar com sua escolha original que tem uma probabilidade de 1/3.

## A Perspectiva da Escolha Quântica

Assim como o mundo quântico, onde partículas existem em múltiplos estados até serem observadas, o carro está atrás de todas as portas até que Monty abra uma porta. Em outras palavras, o problema de Monty Hall exibe uma forma de _superposição quântica_ - múltiplas realidades potenciais existindo simultaneamente. O ato de Monty abrir uma porta é semelhante à observação que 'colapsa' essa superposição, deixando-nos com um novo conjunto de probabilidades.

## E se Aumentarmos o Número de Portas?

Se três portas te deixam confuso, que tal cem? Ou mil? A ideia principal por trás deste simulador é levar o problema de Monty Hall ao extremo. Quando você aumenta o número de portas, a vantagem de mudar se torna exponencialmente aparente e confirma o que era uma vez contra-intuitivo como algo fundamentalmente intuitivo. E é precisamente isso que nosso _Simulador de Retzilience de Monty Hall_ faz - permite que você simule o jogo com quantas portas e tentativas você quiser.

## O Poder da Simulação

O _Simulador de Retzilience de Monty Hall_ combina o poder do módulo random do Python com a interface gráfica intuitiva do tkinter, fornecendo uma maneira envolvente e perspicaz de explorar este problema. O programa simula milhares de jogos de Monty Hall em questão de segundos, coletando dados sobre os resultados com base em se você permanece ou muda. Desta forma, você pode ver o surpreendente poder da estratégia de mudança em ação

.

Lembre-se, a probabilidade não é apenas teoria - é a realidade acontecendo. E nosso simulador é uma caixa de areia onde essa realidade se desenrola. O problema de Monty Hall é uma bela demonstração de como nossa intuição pode muitas vezes nos levar a erros diante da dura verdade probabilística. Ao simular o problema, não apenas entendemos - nós o vivenciamos.

## Conclusão

O problema de Monty Hall é uma viagem fascinante ao mundo da probabilidade, e nosso simulador serve como seu guia turístico. Ao permitir um número arbitrário de portas e tentativas, ilumina a realidade contra-intuitiva do problema. Não é apenas um programa; é um playground digital para experimentar o mundo caprichoso das escolhas quânticas. Então, vá em frente, entre na paisagem quântica de portas, e lembre-se, às vezes é mais sábio mudar!

![GUI](https://github.com/Retzilience/retziliencemonty/blob/main/GUI.png)

# Configurando e Executando o Simulador de Retzilience de Monty Hall: Um Guia Amigável

Bem-vindo à parte divertida! Vamos colocar o Simulador de Retzilience de Monty Hall em funcionamento em sua máquina. Não se preocupe se você é um novato em codificação, esta é uma zona livre de jargões! Siga estas etapas e você terá o simulador funcionando em pouco tempo.

## Passo 1: Instalando o Python

Primeiramente, precisamos ter certeza de que o Python está instalado em seu sistema. Aqui está como:

### Windows:

1. Visite a [página de downloads do Python](https://www.python.org/downloads/windows/).
2. Clique na última versão do Python.
3. Baixe e execute o pacote de instalação.
4. Certifique-se de marcar a caixa que diz "Adicionar Python ao PATH" antes de clicar em Instalar.

### MacOS:

1. Abra o Terminal (você pode encontrá-lo em Aplicativos -> Utilitários).
2. Digite `brew install python3` e pressione Enter (você precisa ter o Homebrew instalado, um gerenciador de pacotes útil para MacOS. Se você não tem, vá para o [site do Homebrew](https://brew.sh/) e siga as instruções lá).
3. Aguarde a mágica acontecer!

### Linux:

1. Abra o Terminal.
2. Digite `sudo apt-get install python3.8` e pressione Enter.
3. Digite sua senha quando solicitado e aguarde a instalação do Python.

## Passo 2: Instalando o Anaconda Navigator

O Anaconda Navigator é uma ótima ferramenta que simplifica o gerenciamento de pacotes e ambientes Python. Ele também vem com Tkinter, uma biblioteca necessária para a execução do nosso script. Aqui está como instalá-lo:

1. Visite a [página de distribuição do Anaconda](https://www.anaconda.com/distribution/).
2. Baixe o instalador para o seu sistema operacional e siga as instruções de instalação fornecidas lá.

## Passo 3: Clonando o Repositório

Nós armazenamos o script do Simulador de Retzilience de Monty Hall em um repositório do GitHub. Para copiar este repositório para a sua máquina local, siga estes passos:

1. Navegue até a página do repositório no GitHub ( https://github.com/Retzilience/retziliencemonty ).
2. Clique no botão 'Código' e copie a URL mostrada.
3. Abra o Terminal (ou Prompt de Comando para usuários do Windows).
4. Navegue até o local onde você deseja clonar o repositório digitando `cd caminho_para_seu_diretório`.
5. Digite `git clone ` e cole a URL que você copiou da página do GitHub.
6. Pressione Enter para clonar o repositório.

## Passo 4: Configurando o Arquivo de Log

Nosso simulador registra cada simulação em um arquivo de log. Você precisa definir o caminho onde este arquivo será criado:

1. Abra o arquivo `retziliencemonty.py` clonado em um editor de texto.
2. Procure pela linha `LOG_FILE = '/seu_caminho/montylog.txt'`.
3. Substitua `'/seu_caminho/montylog.txt'` pelo caminho onde você deseja que o arquivo de log seja criado, por exemplo, `'/Users/SeuNome/Documents/montylog.txt'` para MacOS ou `'C:/Users/SeuNome/Documents/montylog.txt'` para Windows.
4. Salve e feche o arquivo.

## Passo 5: Executando o Simulador

Agora, é hora de dar vida ao nosso simulador!

1. Abra o Anaconda Navigator.
2. Clique na aba 'Ambientes'.
3. Encontre 'base(root)' na lista e clique no botão de play à direita.
4. Selecione 'Abrir Terminal'.
5. No Terminal, navegue até a localização do arquivo `retziliencemonty.py` usando o comando `cd`.
6. Digite `python3 retziliencemonty.py` e pressione Enter.

Parabéns! Agora você está executando o Simulador de Retzilience de Monty Hall! Insira o número de portas e tentativas, e testemunhe a magia da probabilidade se desdobrar!

Lembre-se, não há cabras ou carros atrás das portas, apenas probabilidades quânticas esperando para serem desvendadas. Divirta-se explorando!
