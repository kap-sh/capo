"""Generated from Smithy shape ``com.amazonaws.groundstation#DemodulationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.json_string


class DemodulationConfig(TypedDict, closed=True):
    unvalidated_json: "capo_groundstation.types.json_string.JsonString"
    """<p>Unvalidated JSON of a demodulation <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DemodulationConfig) -> dict:
    out: dict = {}
    out["unvalidatedJSON"] = value["unvalidated_json"]
    return out


def deserialize_json(data: dict) -> DemodulationConfig:
    out: DemodulationConfig = {}  # type: ignore[typeddict-item]
    if data.get("unvalidatedJSON") is not None:
        out["unvalidated_json"] = data["unvalidatedJSON"]
    else:
        out["unvalidated_json"] = ""
    return out
