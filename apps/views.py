from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "apps/index.html")


def cell_update(request, row, col):
    cell_value = request.POST.get("cell_value")
    return render(
        request,
        "apps/partials/cell.html",
        {"cell_value": cell_value, "row": row, "col": col},
    )


def lock_update(request, row, col):
    value = request.headers.get("X-Value")
    lock = request.headers.get("X-Lock")
    print(value)
    if lock == "LOCK":
        return render(
            request,
            "apps/partials/cell.html",
            {"cell_value": value, "lock": "UNLOCK", "row": row, "col": col},
        )
    return render(
        request,
        "apps/partials/cell.html",
        {"cell_value": value, "lock": "LOCK", "row": row, "col": col},
    )
