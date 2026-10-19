"""Generated from Smithy shape ``com.amazonaws.oam#DeleteSinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_oam.types.resource_identifier


class DeleteSinkInput(TypedDict, closed=True):
    identifier: "capo_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the sink to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSinkInput) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> DeleteSinkInput:
    out: DeleteSinkInput = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
