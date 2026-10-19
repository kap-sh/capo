"""Generated from Smithy shape ``com.amazonaws.appflow#InforNexusSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.object


class InforNexusSourceProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p> The object specified in the Infor Nexus flow source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InforNexusSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> InforNexusSourceProperties:
    out: InforNexusSourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("object") is not None:
        out["object"] = data["object"]
    else:
        out["object"] = ""
    return out
