# Roman Converter

## Processo

Desenvolvimento de dois métodos para conversão de numeros romanos utilizando a linguagem Python.

A conversão é feita somente com números maiores que 0 e menores que 4000, caso seja informado um valor fora desse range o sistema retornará uma exceção.

Para os testes utilizei o framework de testes do Python chamado unittest.

## Executar local
- Instalar Python 3.7.3 - https://www.python.org/downloads/release/python-373/
- Clone do repositório
- Executar
```
python source.py
```

## Executar com Docker
 - Clone do repositório
 - Docker build
 ```
 docker build -t roman-converter . 
 ```

- Docker run
 ```
 docker run -i roman-converter
 ```