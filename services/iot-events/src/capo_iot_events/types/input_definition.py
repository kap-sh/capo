"""Generated from Smithy shape ``com.amazonaws.iotevents#InputDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.attributes


class InputDefinition(TypedDict, closed=True):
    attributes: "capo_iot_events.types.attributes.Attributes"
    """<p>The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using <code>BatchPutMessage</code>. Each such message contains a JSON payload, and those attributes (and their paired values) specified here are available for use in the <code>condition</code> expressions used by detectors that monitor this input. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputDefinition) -> dict:
    out: dict = {}
    import capo_iot_events.types.attributes

    out["attributes"] = capo_iot_events.types.attributes.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> InputDefinition:
    out: InputDefinition = {}  # type: ignore[typeddict-item]
    if data.get("attributes") is not None:
        import capo_iot_events.types.attributes

        out["attributes"] = capo_iot_events.types.attributes.deserialize_json(
            data["attributes"]
        )
    else:
        out["attributes"] = []
    return out
