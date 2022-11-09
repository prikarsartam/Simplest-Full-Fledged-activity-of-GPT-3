# -*- coding: utf-8 -*-
"""hands on GPT-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VS87LB4VU-Vk_zIcHLAasstFzYJgIjcO
"""

!pip install openai --quiet
import openai
openai.api_key = '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'



"""# Example 1:**generating an article about how GPT-3 can interprete and understand human language**"""

prompt="write an article of more than 800 words on how GPT-3 can understand human language"
output = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1000)


print(output.choices[0].text)



"""# Example 2: **Generating a Python Code for parsing paragraphs for HTML**"""

prompt="give me a python code to parse a given document file into paragraphs with html <p></p> tag in between each paragraph"

output = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1000)


print(output.choices[0].text)

"""# Example 3: **Generating a JavaScript code to design a responsive sliding menubar**"""

prompt="write me a javascript and css code to a device sensitive and responsive minimally designed sliding menubar"

output = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1000)


print(output.choices[0].text)

"""# Example 4:"""

prompt="given the map of the city in matrix format (a*b) where a represents number of rows 1,...,a and b represents number of columns 1,....,b. All the buses in the city operates within a row, that is, the start and end of every row are within the same row. Given the city map and routes of all the buses r in the city generate a python program to obtain the number of cells the bus don't operate in the city, noting that there might be overlaps between routes. 4"

output = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1000)


print(output.choices[0].text)

prompt="""Write a conclusion for business email compromise attacks of 200 words"""
output = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1000)


print(output.choices[0].text)

prompt="write a summarised conclusion of about 200 words on how data resillienec shapes the society see today"
output = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=2000)


print(output.choices[0].text)

