HTML_TOOL = {
    "type" : "function",
    "function" : {
        "name" : "get_html_content",
        "description": "Find title, date, content, and image url in html",
        "parameters" : {
            "type": "object",
            "properties" : {
                "title" : {
                    "type": "string",
                    "description" : "Find the title text"
                },
                "date" : {
                    "type": "string",
                    "description" : "Find the date in YYYY.MM.DD format"
                },
                "content" : {
                    "type": "array",
                    "items" : {
                        "type" : "object",
                        "properties" : {
                            "type" : {
                                "type" : "string",
                                "enum" : ["txt", "image", "table"],
                                "description" : "Type that must be found in html"
                            },
                            "data" : {
                                "type": "string",
                                "description" : "If type is txt or table, find body content"
                            },
                            "source" : {
                                "type": "string",
                                "description" : "If type is image, find image's url"
                            }
                        }
                    }
                },
            },
            "required" : ["title", "date", "content"]
        },
    },
}

CSS_TOOL = {
    "type" : "function",
    "function" : {
        "name" : "get_css_selector",
        "description": "Find css selector for title, date and content in html",
        "parameters" : {
            "type": "object",
            "properties" : {
                "title" : {
                    "type" : "array",
                    "items" : {
                        "type" : "object",
                        "properties" : {
                            "path" : {
                                "type" : "string",
                                "description" : "Find the css selector of title"
                            },
                            "index" : {
                                "type" : "number",
                                "description" : "Find the starting index of css selector for the title."
                            }
                        }
                    }
                },
                "date" : {
                    "type": "array",
                    "items" : {
                        "type": "object",
                        "properties": {
                            "type" : {
                                "type" : "string",
                                "description" : "The default is normal. if you don't know, leave it blank."
                            },
                            "path" : {
                                "type" : "string",
                                "description" : "Find the css selector of date"
                            },
                            "index" : {
                                "type" : "number",
                                "description" : "Find the starting index of css selector for the date."
                            },
                            "format" : {
                                "type" : "string",
                                "description" : "Fine the format of the date. if you don't know, leave it blank."
                            },
                            "lang" : {
                                "type" : "string",
                                "description" : "Fine the language of the date. if you don't know, fill it null."
                            }
                        }
                    }
                },
                "content" : {
                    "type": "array",
                    "items" : {
                        "type": "object",
                        "properties": {
                            "path" : {
                                "type" : "string",
                                "description" : "Find the css selector of content"
                            },
                            "start_index" : {
                                "type" : "number",
                                "description" : "Find the starting index of css selector for the content."
                            },
                            "end_index" : {
                                "type" : "number",
                                "description" : "Find the end index of css selector for the content. if you don't know, leave it null."
                            }
                        }
                    }
                },
            },
            "required" : ["title", "date", "content"]
        },
    },
}