Seção 1 - Para o usuário!

# Sobre

Olá! Bem-vindo ao Github do LivePub. O LivePub é um projeto Open Source que irá ajudá-lo a hospedar sua própria transmissão ao vivo. Com um painel amigável e uma forma simples de instalar! Então espero que vocês gostem e vamos começar!

# Vamos começar!

Ok, antes de começar, você precisa tentar usar nossa demonstração do LivePub (Você pode acessar por: [Clique aqui para abrir](http://livepub.ddns.net)).

Este site será executado localmente no seu computador e explicarei como.

# Requisitos:

Ram: 2gb

CPU: (Provavelmente funcionará com sua CPU)

Sistema operacional: Ubuntu 22.04 LTS (recomendo usar Ubuntu 22.04 LTS ou Ubuntu 20.04 LTS)

Aplicativos: ffmpeg, python3, python3-pip, nginx (o script fará isso por você!)


# O código!

Primeiro você precisará baixar nosso script
Código:
```
sudo su
```
```
apt update && apt upgrade -y
```
```
apt update wget curl -y
```
```
wget ​​https://raw.githubusercontent.com/op3ny/LivePub/main/script.sh
```
VERSÃO EM PORTUGUÊS ------^

```
wget ​​https://github.com/op3ny/LivePub/raw/main/script2.sh
```
VERSÃO EM INGLES ---------^
```
chmod 777 script.sh
```
```
./script.sh
```

Ao final você precisa reiniciar sua máquina, com este comando:
```
reboot
```

#Novos comandos!

No seu sistema, você terá três novos comandos (funciona apenas no root)
```
livepub-start
```
Inicie o LivePub
```
livepub-stop
```
Pare o LivePub
