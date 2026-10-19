"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SSMLMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.ssml_message_value


class SSMLMessage(TypedDict, closed=True):
    value: "capo_lex_models_v2.types.ssml_message_value.SSMLMessageValue"
    """<p>The SSML text that defines the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SSMLMessage) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SSMLMessage:
    out: SSMLMessage = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
