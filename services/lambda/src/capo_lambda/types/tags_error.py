"""Generated from Smithy shape ``com.amazonaws.lambda#TagsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.tags_error_code
    import capo_lambda.types.tags_error_message


class TagsError(TypedDict, closed=True):
    error_code: "capo_lambda.types.tags_error_code.TagsErrorCode"
    """<p>The error code.</p>"""
    message: "capo_lambda.types.tags_error_message.TagsErrorMessage"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagsError) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TagsError:
    out: TagsError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        out["error_code"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
