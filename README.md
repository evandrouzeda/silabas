# Separador de Silabas
Automato escrito em python para separar as silabas de palavras da lingua portuguesa

A máquina de estados possue estados de q1 a q11, sendo q1 o estado inicial e q5, q6, q7, q9 e q11 estados de aceitação. Nos estados de aceitação é onde ocorrera a separação das silabas. Usei como referência o artigo [Como separar sílabas](https://escolaeducacao.com.br/como-separar-silabas/) para pegar as regras.

## Imagem do automato
![Automato](/mermaid-diagram-20220604135826.svg?raw=true "M")

[Link do Mermaid Live Editor](https://mermaid.live/edit#pako:eNp9lE1uwyAQRq-CWFaxFPBvZtFVc4Is6y6QISlqMI2NI1VR7l4q0yo2Q72Cb0bvMYvxjXZWKgp0dMKpFy1OgzDZlbc98d_r0xvJsmdyYfP9wuZrDmRURi_DAsjVnsR5me6ASO2hR7ticCCd7UcreqdChWN0jtJ5is6T9HyulEBElDz4ctSXp3yhUMe-Apum-FM-0osUvUjSS4xeom8vU_QySa8weoXSQ9oAMUrbZRgrq6SyxpQ1qqwxZQgZi5yhUsXOBnM2qLNJTdQkJ9qFF22BTMtovSrbf2MEzVjMZqs9pBtq1GCEln69bz9NLXXvyqiWgj9KMXy0tO3vvm_6lH7791I7O1A4ivOoNlRMzh6--o6CGyb12xR-EaHr_g3lJi6P)

### A fazer
Algumas regras particulares, principalmente quanto tem 'ui', ele tem problemas em separar como deve ser.

Mais detalhes nos comentários do código
