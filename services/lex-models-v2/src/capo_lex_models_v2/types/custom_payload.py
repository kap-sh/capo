"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.custom_payload_value


class CustomPayload(TypedDict, closed=True):
    value: "capo_lex_models_v2.types.custom_payload_value.CustomPayloadValue"
    """<p>The string that is sent to your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPayload) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CustomPayload:
    out: CustomPayload = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
