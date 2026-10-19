"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteRecommenderFilterResponse``."""

from typing_extensions import TypedDict


class DeleteRecommenderFilterResponse(TypedDict, closed=True):
    message: "str"
    """<p>A message that indicates the delete request is done.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommenderFilterResponse) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteRecommenderFilterResponse:
    out: DeleteRecommenderFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
