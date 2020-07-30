# wiki-disambiguator
Python script that uses [expert.ai](https://expert.ai) API to disambiguate text and generate an HTML with Wikipedia links

Instructions:
1. Install [nlapi-python](https://github.com/therealexpertai/nlapi-python)
2. Copy the [wiki-disambiguator.py](./wiki-disambiguator.py) script into the nlapi-python folder.
3. Set your [API Credentials](https://developer.expert.ai/ui/login) as environment variables:
  ```bash
  export EAI_USERNAME=YOUR_USER
  export EAI_PASSWORD=YOUR_PASSWORD
  ```
4. Run the [wiki-disambiguator.py](./wiki-disambiguator.py) script as:
  ```bash
  python wiki-disambiguator.py TEXT LANGUAGE_CODE
  ```
  as an example (text extracted from https://en.wikipedia.org/wiki/Alan_Turing):
  ```bash
  python wiki-disambiguator.py 'Alan Mathison Turing OBE FRS (/ˈtjʊərɪŋ/; 23 June 1912 – 7 June 1954) was an English[6] mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist.[7] Turing was highly influential in the development of theoretical computer science, providing a formalisation of the concepts of algorithm and computation with the Turing machine, which can be considered a model of a general-purpose computer.[8][9][10] Turing is widely considered to be the father of theoretical computer science and artificial intelligence.[11] Despite these accomplishments, he was never fully recognised in his home country during his lifetime due to his homosexuality and because much of his work was covered by the Official Secrets Act.' 'en'
  ```
  A browser tab will be opened with the HTML output:
  ```html
  <!DOCTYPE html>
  <html>
  <body>Alan Mathison Turing <a href="https://en.wikipedia.org/wiki/Order_of_the_British_Empire">OBE</a> FRS (/ˈtjʊərɪŋ/; 23 June 1912 – 7 June 1954) was an English[6] <a href="https://en.wikipedia.org/wiki/Mathematician">mathematician</a>, <a href="https://en.wikipedia.org/wiki/Computer_scientist">computer scientist</a>, logician, cryptanalyst, <a href="https://en.wikipedia.org/wiki/Philosopher">philosopher</a>, and theoretical <a href="https://en.wikipedia.org/wiki/Biologist">biologist</a>.[7] Turing was highly influential in the development of theoretical <a href="https://en.wikipedia.org/wiki/Computer_science">computer science</a>, providing a formalisation of the concepts of <a href="https://en.wikipedia.org/wiki/Algorithm">algorithm</a> and <a href="https://en.wikipedia.org/wiki/Computation">computation</a> with the <a href="https://en.wikipedia.org/wiki/Turing_machine">Turing machine</a>, which can be considered a model of a general-purpose computer.[8][9][10] Turing is widely considered to be the father of theoretical <a href="https://en.wikipedia.org/wiki/Computer_science">computer science</a> and <a href="https://en.wikipedia.org/wiki/Artificial_intelligence">artificial intelligence</a>.[11] Despite these accomplishments, he was never fully recognised in his home country during his lifetime due to his <a href="https://en.wikipedia.org/wiki/Homosexuality">homosexuality</a> and because much of his work was covered by the <a href="https://en.wikipedia.org/wiki/Official_Secrets_Act">Official Secrets Act</a>.
  </body>
  </html>
  ```
Alan Mathison Turing <a href="https://en.wikipedia.org/wiki/Order_of_the_British_Empire">OBE</a> FRS (/ˈtjʊərɪŋ/; 23 June 1912 – 7 June 1954) was an English[6] <a href="https://en.wikipedia.org/wiki/Mathematician">mathematician</a>, <a href="https://en.wikipedia.org/wiki/Computer_scientist">computer scientist</a>, logician, cryptanalyst, <a href="https://en.wikipedia.org/wiki/Philosopher">philosopher</a>, and theoretical <a href="https://en.wikipedia.org/wiki/Biologist">biologist</a>.[7] Turing was highly influential in the development of theoretical <a href="https://en.wikipedia.org/wiki/Computer_science">computer science</a>, providing a formalisation of the concepts of <a href="https://en.wikipedia.org/wiki/Algorithm">algorithm</a> and <a href="https://en.wikipedia.org/wiki/Computation">computation</a> with the <a href="https://en.wikipedia.org/wiki/Turing_machine">Turing machine</a>, which can be considered a model of a general-purpose computer.[8][9][10] Turing is widely considered to be the father of theoretical <a href="https://en.wikipedia.org/wiki/Computer_science">computer science</a> and <a href="https://en.wikipedia.org/wiki/Artificial_intelligence">artificial intelligence</a>.[11] Despite these accomplishments, he was never fully recognised in his home country during his lifetime due to his <a href="https://en.wikipedia.org/wiki/Homosexuality">homosexuality</a> and because much of his work was covered by the <a href="https://en.wikipedia.org/wiki/Official_Secrets_Act">Official Secrets Act</a>.

We can process text in other languages, let's take for example a text (text extracted from https://es.wikipedia.org/wiki/Espa%C3%B1a) in Spanish:
  ```bash
  python wiki-disambiguator.py "España, también denominado Reino de España,nota 1​ es un país transcontinental, miembro de la Unión Europea, constituido en Estado social y democrático de derecho y cuya forma de gobierno es la monarquía parlamentaria. Su territorio, con capital en Madrid,31​ está organizado en diecisiete comunidades autónomas, formadas a su vez por cincuenta provincias; y dos ciudades autónomas." es
  ```
  The output contains links to Wikipedia in Spanish :
  ```html
  <!DOCTYPE html>
<html>
<body><a href="https://es.wikipedia.org/wiki/España">España</a>, también denominado <a href="https://es.wikipedia.org/wiki/España">Reino de España</a>,nota 1​ es un <a href="https://es.wikipedia.org/wiki/Estado_soberano">país</a> transcontinental, miembro de la <a href="https://es.wikipedia.org/wiki/Unión_Europea">Unión Europea</a>, constituido en Estado social y democrático de derecho y cuya <a href="https://es.wikipedia.org/wiki/Gobierno">forma de gobierno</a> es la <a href="https://es.wikipedia.org/wiki/Monarquía_parlamentaria">monarquía parlamentaria</a>. Su <a href="https://es.wikipedia.org/wiki/Región">territorio</a>, con <a href="https://es.wikipedia.org/wiki/Capital_(política)">capital</a> en <a href="https://es.wikipedia.org/wiki/Madrid">Madrid</a>,31​ está organizado en diecisiete comunidades autónomas, formadas a su vez por cincuenta <a href="https://es.wikipedia.org/wiki/Provincia">provincias</a>; y dos <a href="https://es.wikipedia.org/wiki/Ciudad_autónoma">ciudades autónomas</a>.
</body>
</html>
  ```
  
  <a href="https://es.wikipedia.org/wiki/España">España</a>, también denominado <a href="https://es.wikipedia.org/wiki/España">Reino de España</a>,nota 1​ es un <a href="https://es.wikipedia.org/wiki/Estado_soberano">país</a> transcontinental, miembro de la <a href="https://es.wikipedia.org/wiki/Unión_Europea">Unión Europea</a>, constituido en Estado social y democrático de derecho y cuya <a href="https://es.wikipedia.org/wiki/Gobierno">forma de gobierno</a> es la <a href="https://es.wikipedia.org/wiki/Monarquía_parlamentaria">monarquía parlamentaria</a>. Su <a href="https://es.wikipedia.org/wiki/Región">territorio</a>, con <a href="https://es.wikipedia.org/wiki/Capital_(política)">capital</a> en <a href="https://es.wikipedia.org/wiki/Madrid">Madrid</a>,31​ está organizado en diecisiete comunidades autónomas, formadas a su vez por cincuenta <a href="https://es.wikipedia.org/wiki/Provincia">provincias</a>; y dos <a href="https://es.wikipedia.org/wiki/Ciudad_autónoma">ciudades autónomas</a>.

The API currently supports five languages: English(en), Spanish(es), German(de), French(fr) and Italian(it).
