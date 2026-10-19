"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.retrieve_error_code
    import capo_qconnect.types.uuid


class RetrieveError(TypedDict, closed=True):
    association_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the assistant association whose knowledge base retrieval failed.</p>"""
    code: "capo_qconnect.types.retrieve_error_code.RetrieveErrorCode"
    """<p>The error code that categorizes the retrieval failure for the assistant association.</p>"""
    message: "str"
    """<p>A human-readable description of the retrieval failure for the assistant association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveError) -> dict:
    out: dict = {}
    out["associationId"] = value["association_id"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RetrieveError:
    out: RetrieveError = {}  # type: ignore[typeddict-item]
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    else:
        out["association_id"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
