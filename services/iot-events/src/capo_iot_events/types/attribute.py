"""Generated from Smithy shape ``com.amazonaws.iotevents#Attribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.attribute_json_path


class Attribute(TypedDict, closed=True):
    json_path: "capo_iot_events.types.attribute_json_path.AttributeJsonPath"
    """<p>An expression that specifies an attribute-value pair in a JSON structure. Use this to specify an attribute from the JSON payload that is made available by the input. Inputs are derived from messages sent to AWS IoT Events (<code>BatchPutMessage</code>). Each such message contains a JSON payload. The attribute (and its paired value) specified here are available for use in the <code>condition</code> expressions used by detectors. </p> <p>Syntax: <code><field-name>.<field-name>...</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attribute) -> dict:
    out: dict = {}
    out["jsonPath"] = value["json_path"]
    return out


def deserialize_json(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if data.get("jsonPath") is not None:
        out["json_path"] = data["jsonPath"]
    else:
        out["json_path"] = ""
    return out
