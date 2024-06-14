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
                                "description" : "Find body content if type is txt or table"
                            },
                            "source" : {
                                "type": "string",
                                "description" : "Find image url if type is image"
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
                            }
                        }
                    }
                },
                "date" : {
                    "type": "array",
                    "items" : {
                        "type": "object",
                        "properties": {
                            "path" : {
                                "type" : "string",
                                "description" : "Find the css selector of date"
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
                            }
                        }
                    }
                },
            },
            "required" : ["title", "date", "content"]
        },
    },
}