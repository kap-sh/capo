"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ConsumedResourceShareDetails``."""

from typing_extensions import TypedDict


class ConsumedResourceShareDetails(TypedDict, closed=True):
    owner_account_id: "str"
    """<p>The ID of the Amazon Web Services account that owns the shared endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsumedResourceShareDetails) -> dict:
    out: dict = {}
    out["ownerAccountId"] = value["owner_account_id"]
    return out


def deserialize_json(data: dict) -> ConsumedResourceShareDetails:
    out: ConsumedResourceShareDetails = {}  # type: ignore[typeddict-item]
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        out["owner_account_id"] = ""
    return out
