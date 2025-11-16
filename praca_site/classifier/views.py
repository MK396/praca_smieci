from django.shortcuts import render
from .cnn_model.predict import predict_image
from PIL import Image
# konwersja obrazu do base64
import base64
import io

def classify_image(request):
    results = []

    if request.method == 'POST' and request.FILES.getlist('images'):
        model_choice = request.POST.get('model_choice')

        for image_file in request.FILES.getlist('images'):
            image = Image.open(image_file)
            image.thumbnail((256, 256))

            # Konwersja do base64
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()

            result, confidence = predict_image(image, model_choice)

            results.append({
                'result': result,
                'confidence': confidence,
                # dodaj pełne dane do <img src="...">
                'image_url': f"data:image/png;base64,{img_base64}",
                'model_name': "ResNet50" if model_choice == 'resnet' else "Model autorski"
            })

    return render(request, 'classifier/classify.html', {'results': results})
