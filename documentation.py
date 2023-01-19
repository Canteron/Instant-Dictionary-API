import justpy as jp

class Doc():

    @classmethod
    def serve(self):
        wp = jp.WebPage(tailwind=True)

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant Dictionary API", classes="text-4xl m-2")
        jp.Div(a=div, text="Get definition of words", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="http://127.0.0.1:8000/api?w=sun")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "sun", "definition": ["Any star, especially when seen as the centre of any single solar system.", 
        "The particular star at the centre of our solar system, from which the Earth gets light and heat."]}
        """)

        return wp
