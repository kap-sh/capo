"""Generated from Smithy shape ``com.amazonaws.lambdaweb#DeleteWebFunctionRevisionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.revision_id


class DeleteWebFunctionRevisionRequest(TypedDict, closed=True):
    function_name: "capo_lambda_web.types.function_name.FunctionName"
    """<p>The name of the web function. You can specify the function name or the function ARN. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    revision_id: "capo_lambda_web.types.revision_id.RevisionId"
    """<p>The identifier of the revision to delete. You can specify the revision identifier or the revision ARN. The length constraint applies only to the full ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWebFunctionRevisionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWebFunctionRevisionRequest:
    out: DeleteWebFunctionRevisionRequest = {}  # type: ignore[typeddict-item]
    return out
