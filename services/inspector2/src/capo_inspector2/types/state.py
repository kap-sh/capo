"""Generated from Smithy shape ``com.amazonaws.inspector2#State``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.error_code
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.status


class State(TypedDict, closed=True):
    status: "capo_inspector2.types.status.Status"
    """<p>The status of Amazon Inspector for the account.</p>"""
    error_code: "capo_inspector2.types.error_code.ErrorCode"
    """<p>The error code explaining why the account failed to enable Amazon Inspector.</p>"""
    error_message: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The error message received when the account failed to enable Amazon Inspector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: State) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> State:
    out: State = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
