"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionDefinition``."""

from typing_extensions import TypedDict


class CustomActionDefinition(TypedDict, closed=True):
    command_text: "str"
    """<p>The command string to run which may include variables by prefixing with a dollar sign ($).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionDefinition) -> dict:
    out: dict = {}
    out["CommandText"] = value["command_text"]
    return out


def deserialize_json(data: dict) -> CustomActionDefinition:
    out: CustomActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("CommandText") is not None:
        out["command_text"] = data["CommandText"]
    else:
        out["command_text"] = ""
    return out
