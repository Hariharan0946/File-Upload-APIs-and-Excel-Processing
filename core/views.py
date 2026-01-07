import os
import uuid
import logging
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import UserRecord
from .utils import process_excel

logger = logging.getLogger('core')

@csrf_exempt
def upload_file(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    file = request.FILES.get('file')
    if not file:
        return JsonResponse({'error': 'File required'}, status=400)

    if not file.name.lower().endswith(('.xls', '.xlsx', '.csv')):
        return JsonResponse({'error': 'Only xls, xlsx or csv allowed'}, status=400)

    if file.size > 5 * 1024 * 1024:
        return JsonResponse({'error': 'Max file size 5MB'}, status=400)

    filename = f"{uuid.uuid4()}_{file.name}"
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    with open(file_path, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

    logger.info(f"File uploaded: {file_path}")

    return JsonResponse({'file_path': file_path})


@csrf_exempt
def process_excel_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    file_path = request.POST.get('file_path')
    if not file_path or not os.path.exists(file_path):
        return JsonResponse({'error': 'Invalid file_path'}, status=400)

    inserted, skipped = process_excel(file_path)

    return JsonResponse({
        'inserted': inserted,
        'skipped': skipped
    })


def get_all_records(request):
    page = max(int(request.GET.get('page', 1)), 1)
    limit = max(int(request.GET.get('limit', 10)), 1)
    education = request.GET.get('education')

    qs = UserRecord.objects.all()
    if education:
        qs = qs.filter(education=education)

    paginator = Paginator(qs, limit)
    page_obj = paginator.get_page(page)

    return JsonResponse({
        'page': page,
        'limit': limit,
        'total': paginator.count,
        'data': list(page_obj.object_list.values())
    })