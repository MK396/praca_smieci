from django.shortcuts import render
from .cnn_model.predict import predict_image
import os

# Create your views here.

def classify_image(request):
    result = None
    confidence = None
    # sprawdzenie czy metoda to POST i czy plik został przesłany
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        # utworzenie tymczasowego katalogu na przesłane pliki
        temp_dir = "temp_uploads"
        os.makedirs(temp_dir, exist_ok=True)

        file_path = os.path.join(temp_dir, image_file.name)
        # zapisanie pliku podzielonego na chunki, bo jeśli jest duży to będzie problem z pamięcią i błąd zapsisu
        with open(file_path, 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)
        result, confidence = predict_image(file_path)


    return render(request, 'classifier/classify.html', {'result': result, 'confidence': confidence})