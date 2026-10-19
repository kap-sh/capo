"""Generated from Smithy shape ``com.amazonaws.appflow#DynatraceSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.object


class DynatraceSourceProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p> The object specified in the Dynatrace flow source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> DynatraceSourceProperties:
    out: DynatraceSourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("object") is not None:
        out["object"] = data["object"]
    else:
        out["object"] = ""
    return out
