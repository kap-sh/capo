"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SampleValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.value


class SampleValue(TypedDict, closed=True):
    value: "capo_lex_models_v2.types.value.Value"
    """<p>The value that can be used for a slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SampleValue:
    out: SampleValue = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
