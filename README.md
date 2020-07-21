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
  python TEXT LANGUAGE_CODE
  ```
  as an example:
  ```bash
  python wiki-disambiguator.py 'Alan Mathison Turing OBE FRS (/ˈtjʊərɪŋ/; 23 June 1912 – 7 June 1954) was an English[6] mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist.[7] Turing was highly influential in the development of theoretical computer science, providing a formalisation of the concepts of algorithm and computation with the Turing machine, which can be considered a model of a general-purpose computer.[8][9][10] Turing is widely considered to be the father of theoretical computer science and artificial intelligence.[11] Despite these accomplishments, he was never fully recognised in his home country during his lifetime due to his homosexuality and because much of his work was covered by the Official Secrets Act.' 'en'
  ```
  A browser tab will be open with the [output](./output.html)
