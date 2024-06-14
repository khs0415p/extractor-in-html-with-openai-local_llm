HTML_PROMPT =  """
# PREREQUISITES
- Extract content in the same order as HTML.
- Include only texts, tables and images in the content.
- date will follow YYYY.MM.DD format.
- EXAMPLE-1 is an incorrect response and groups successive txts like EXAMPLE-2.


# EXAMPLE-1
{{
    title : "NEWS ...",
    date : "2024.05.28,
    content : [
        {{
            "type" : "txt",
            "data" : "Recommended Plant-Based Brand Now ..."
        }},
        {{
            "type" : "txt",
            "data" : "Altasciences announced today that ..."
        }},
        {{
            "type" : "image"
            "source" : "https://image-source..."
        }},
        {{
            "type" : "table"
            "data" : "+---------------+---------------+\n| Conference: ...|"
        }},
        ...
    ]
}}


# EXAMPLE-2
{{
    title : "NEWS ...",
    date : "2024.05.28,
    content : [
        {{
            "type" : "txt",
            "data" : "Recommended Plant-Based Brand Now ...Altasciences announced today that ..."
        }},
        {{
            "type" : "image"
            "source" : "https://image-source..."
        }},
        {{
            "type" : "table"
            "data" : "+---------------+---------------+\n| Conference: ...|"
        }},
        ...
    ]
}}


# HTML
{}


# OUTPUT
```json
"""

CSS_PROMPT = """
1. Extract the css selector for title, date and content from HTML.
2. Generate in the format of the EXAMPLE below.

## EXAMPLE
# HTML
Your HTML


# OUTPUT
```json
Your OUTPUT
```


# HTML
{}

# OUTPUT
```json
"""