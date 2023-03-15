from django.shortcuts import render, redirect
from .models import SmartCalculator


# Create your views here.

# Views for home page
def siteHome(request):
    return render(request, 'siteHome.html')

# Views for calculator page
def calculator(request):
    calculators = SmartCalculator.objects.all()
    return render(request, 'calculator.html', {'calculators': calculators})

def smartCalc(request, pk):
    calculators = SmartCalculator.objects.get(id=pk)
    return render(request, 'smartCalc.html', {'calculators': calculators})

def volume(request):
    if request.method == 'POST':
        length = float(request.POST.get('length'))
        breadth = float(request.POST.get('breadth'))
        height = float(request.POST.get('height'))
        volumeOfCuboid = float(length) * float(breadth) * float(height)
        return render(request, 'results.html', {'volume_of_cuboid': volumeOfCuboid})
    

    return render(request, 'smartCalc.html')



# Views for weather page
def weatherDetector(request):
    return render(request, 'weatherDetector.html' )

# Views for Youtube Downloader page
def youtubeDownloader(request):
    return render(request, 'youtubeDownloader.html')


