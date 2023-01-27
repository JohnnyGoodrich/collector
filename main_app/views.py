from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Whale
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView



# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
# class Home(View):

#     # Here we are adding a method that will be ran when we are dealing with a GET request
#     def get(self, request):
#         # Here we are returning a generic response
#         # This is similar to response.send() in express
#         return HttpResponse("Whale Watching")

class About(TemplateView):
    template_name = "about.html"

# class About(View):

#     def get(self, request):
#         return HttpResponse("Spotify About")

 #adds artist class for mock database data
class WhaleList(TemplateView):
    template_name = "whales_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["whales"] = Whale.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["whales"] = Whale.objects.all()
            # default header for not searching 
            context["header"] = "Whales"
        return context

class WhaleCreate(CreateView):
    model = Whale
    fields = ['name', 'img', 'bio', 'verified_whale']
    template_name = "whales_create.html"
    success_url = "/whales/"

class WhaleDetail(DetailView):
    model = Whale
    template_name = "whale_detail.html"

class WhaleUpdate(UpdateView):
    model = Whale
    fields = ['name', 'img', 'bio', 'verified_whale']
    template_name = "whale_update.html"
    success_url = "/whales/"

class WhaleDelete(DeleteView):
    model = Whale
    template_name = "whale_delete_confirmation.html"
    success_url = "/whales/"


# class Whale:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio


# whales = [
#   Whale("Orca Whale", "https://a-z-animals.com/media/killer-whale-1.jpg",
#           "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around."),
#   Whale("Humpback Whale",
#           "https://media.fisheries.noaa.gov/styles/original/s3/2021-08/640x427-Whale-Humpback-watermark.jpg?itok=3RBJ1uQq", "Welcome 👋 The Amazing Beebo was working on a new bio but now he's too busy taking over the world."),
#   Whale("Blue Whale", "data:image/jpeg;base64,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",
#           "Joji is one of the most enthralling Whales of the digital age. New album Nectar arrives as an eagerly anticipated follow-up to Joji's RIAA Gold-certified first full-length album BALLADS 1, which topped the Billboard R&B / Hip-Hop Charts and has amassed 3.6B+ streams to date."),
#   Whale("Beluga Whale",
#           "https://s.hdnux.com/photos/01/26/26/25/22635855/4/1200x0.jpg", "Metallica formed in 1981 by drummer Lars Ulrich and guitarist and vocalist James Hetfield and has become one of the most influential and commercially successful rock bands in history, having sold 110 million albums worldwide while playing to millions of fans on literally all seven continents."),
#   Whale("Narwhal",
#           "http://ocean.si.edu/sites/default/files/styles/article_main_image/public/%28GW%29-narwhal-tusk.jpg.webp?itok=GQrGvXsE", "Benito Antonio Martínez Ocasio, known by his stage name Bad Bunny, is a Puerto Rican rapper, singer, and songwriter. His music is often defined as Latin trap and reggaeton, but he has incorporated various other genres into his music, including rock, bachata, and soul"),
#   Whale("Sperm Whale",
#           "https://static01.nyt.com/images/2022/10/02/books/review/02Backpage_upclose-06/02Backpage_upclose-06-articleLarge.jpg?quality=75&auto=webp&disable=upscale", "Ryan Gary Raddon, better known by his stage name Kaskade, is an American DJ, record producer, and remixer."),
# ]
