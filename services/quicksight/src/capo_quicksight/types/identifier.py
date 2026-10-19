"""Generated from Smithy shape ``com.amazonaws.quicksight#Identifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string


class Identifier(TypedDict, closed=True):
    identity: "capo_quicksight.types.limited_string.LimitedString"
    """<p>The identity of the identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Identifier) -> dict:
    out: dict = {}
    out["Identity"] = value["identity"]
    return out


def deserialize_json(data: dict) -> Identifier:
    out: Identifier = {}  # type: ignore[typeddict-item]
    if data.get("Identity") is not None:
        out["identity"] = data["Identity"]
    else:
        out["identity"] = ""
    return out
