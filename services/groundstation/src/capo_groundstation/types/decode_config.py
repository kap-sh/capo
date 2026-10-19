"""Generated from Smithy shape ``com.amazonaws.groundstation#DecodeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.json_string


class DecodeConfig(TypedDict, closed=True):
    unvalidated_json: "capo_groundstation.types.json_string.JsonString"
    """<p>Unvalidated JSON of a decode <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecodeConfig) -> dict:
    out: dict = {}
    out["unvalidatedJSON"] = value["unvalidated_json"]
    return out


def deserialize_json(data: dict) -> DecodeConfig:
    out: DecodeConfig = {}  # type: ignore[typeddict-item]
    if data.get("unvalidatedJSON") is not None:
        out["unvalidated_json"] = data["unvalidatedJSON"]
    else:
        out["unvalidated_json"] = ""
    return out
