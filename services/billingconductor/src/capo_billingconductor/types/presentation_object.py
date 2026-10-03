"""Generated from Smithy shape ``com.amazonaws.billingconductor#PresentationObject``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.service


class PresentationObject(TypedDict, closed=True):
    service: "capo_billingconductor.types.service.Service"
    """<p> The service under which the custom line item charges will be presented. Must be a string between 1 and 128 characters matching the pattern "<code>^[a-zA-Z0-9]+$</code>". </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PresentationObject) -> dict:
    out: dict = {}
    out["Service"] = value["service"]
    return out


def deserialize_json(data: dict) -> PresentationObject:
    out: PresentationObject = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        raise DeserializationError("PresentationObject.service required")
    return out
