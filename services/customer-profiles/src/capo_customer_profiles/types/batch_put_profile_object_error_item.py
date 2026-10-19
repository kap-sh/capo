"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchPutProfileObjectErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.response_code
    import capo_customer_profiles.types.text


class BatchPutProfileObjectErrorItem(TypedDict, closed=True):
    id: "capo_customer_profiles.types.name.name"
    """<p>The unique identifier of the item in the batch request that failed.</p>"""
    code: "capo_customer_profiles.types.response_code.responseCode"
    """<p>The HTTP status code for the error.</p>"""
    message: NotRequired["capo_customer_profiles.types.text.text"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutProfileObjectErrorItem) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchPutProfileObjectErrorItem:
    out: BatchPutProfileObjectErrorItem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = 0
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
