"""Generated from Smithy shape ``com.amazonaws.lambdaweb#DeleteWebFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.function_name


class DeleteWebFunctionRequest(TypedDict, closed=True):
    function_name: "capo_lambda_web.types.function_name.FunctionName"
    """<p>The name of the web function to delete. You can specify the function name or the function ARN. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWebFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWebFunctionRequest:
    out: DeleteWebFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
