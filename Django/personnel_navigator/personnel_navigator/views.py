from django.http import HttpResponse


def view_playlist(request):
    return HttpResponse("""
    <h3> My favourite music playlist </h3>
    <a href="https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PL15B1E77BB5708555&index=2"> Shape Of You</a><br>
    <a href="https://www.youtube.com/watch?v=RgKAFK5djSk&list=PL15B1E77BB5708555&index=3 "> See you again</a><br>
    <a href="https://www.youtube.com/watch?v=60ItHLz5WEA&list=PL15B1E77BB5708555&index=15"> Faded</a><br>
    <a href="https://www.youtube.com/watch?v=YQHsXMglC9A&list=PL15B1E77BB5708555&index=19">Adele - Hello </a>
    """)
