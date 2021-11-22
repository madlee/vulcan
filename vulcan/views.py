from os.path import join as join_path, isdir as is_dir
from os import listdir as list_dir
from posixpath import join
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings



def index(request):
    print (settings.VULCAN_INDEX_FILE)
    return HttpResponseRedirect(settings.VULCAN_INDEX_FILE)


def list_file(request):
    path = request.GET.get('path', '')
    fullpath = join_path(settings.VULCAN_BASE_FOLDER, path)
    folders = []
    files = []
    for row in list_dir(fullpath):
        filename = join_path(fullpath, row)
        if is_dir(filename):
            folders.append(
                {'name': row}
            )
        else:
            ext = row.rsplit('.', 1)[1].lower()
            if ext in ('jpg', 'png', 'gif', 'jpeg', 'pdf'):
                files.append(
                    {'name': row}
                )

    result = {
        'path': path,
        'folders': folders,
        'images': files
    }
    return JsonResponse(result)
