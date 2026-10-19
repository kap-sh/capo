"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExecutionErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.non_empty_string


class ExecutionErrorDetails(TypedDict, closed=True):
    error_code: "capo_lex_models_v2.types.non_empty_string.NonEmptyString"
    """<p>The error code for the error.</p>"""
    error_message: "capo_lex_models_v2.types.non_empty_string.NonEmptyString"
    """<p>The message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionErrorDetails) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ExecutionErrorDetails:
    out: ExecutionErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
