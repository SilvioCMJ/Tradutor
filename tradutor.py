from translate import Translator

# digite o texto

texto = 'example text'
# configurando
config = Translator(from_lang='english', to_lang='pt-br')

# traduzindo
tradutor = config.translate(texto)

print(tradutor)
