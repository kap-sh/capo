"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.function_id


class GetFunctionRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.function_id.FunctionId"
    """<p>The ID of the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFunctionRequest:
    out: GetFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
