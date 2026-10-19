"""Generated from Smithy shape ``com.amazonaws.oam#DeleteLinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_oam.types.resource_identifier


class DeleteLinkInput(TypedDict, closed=True):
    identifier: "capo_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the link to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLinkInput) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> DeleteLinkInput:
    out: DeleteLinkInput = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
