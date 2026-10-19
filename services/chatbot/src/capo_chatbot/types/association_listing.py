"""Generated from Smithy shape ``com.amazonaws.chatbot#AssociationListing``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.arn


class AssociationListing(TypedDict, closed=True):
    resource: "capo_chatbot.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource (for example, a custom action).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociationListing) -> dict:
    out: dict = {}
    out["Resource"] = value["resource"]
    return out


def deserialize_json(data: dict) -> AssociationListing:
    out: AssociationListing = {}  # type: ignore[typeddict-item]
    if data.get("Resource") is not None:
        out["resource"] = data["Resource"]
    else:
        out["resource"] = ""
    return out
