"""Generated from Smithy shape ``com.amazonaws.lambdaweb#GetWebFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.function_name


class GetWebFunctionRequest(TypedDict, closed=True):
    function_name: "capo_lambda_web.types.function_name.FunctionName"
    """<p>The web function to retrieve.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWebFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWebFunctionRequest:
    out: GetWebFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
