from src.errors.http_exception import HttpException
from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpException):
        return HttpResponse(
            body={
                "errors": [
                    {
                        "detail": error.message,
                        "title": error.name,
                    }
                ]
            },
            status_code=error.status_code,
        )

    return HttpResponse(
        body={"errors": [{"detail": "Server Error", "title": str(error)}]},
        status_code=500,
    )
