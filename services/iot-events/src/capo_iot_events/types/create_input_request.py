"""Generated from Smithy shape ``com.amazonaws.iotevents#CreateInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events.types.input_definition
    import capo_iot_events.types.input_description
    import capo_iot_events.types.input_name
    import capo_iot_events.types.tags


class CreateInputRequest(TypedDict, closed=True):
    input_name: "capo_iot_events.types.input_name.InputName"
    """<p>The name you want to give to the input.</p>"""
    input_description: NotRequired[
        "capo_iot_events.types.input_description.InputDescription"
    ]
    """<p>A brief description of the input.</p>"""
    input_definition: "capo_iot_events.types.input_definition.InputDefinition"
    """<p>The definition of the input.</p>"""
    tags: NotRequired["capo_iot_events.types.tags.Tags"]
    """<p>Metadata that can be used to manage the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputRequest) -> dict:
    out: dict = {}
    out["inputName"] = value["input_name"]
    if "input_description" in value:
        out["inputDescription"] = value["input_description"]
    import capo_iot_events.types.input_definition

    out["inputDefinition"] = capo_iot_events.types.input_definition.serialize_json(
        value["input_definition"]
    )
    if "tags" in value:
        import capo_iot_events.types.tags

        out["tags"] = capo_iot_events.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateInputRequest:
    out: CreateInputRequest = {}  # type: ignore[typeddict-item]
    if data.get("inputName") is not None:
        out["input_name"] = data["inputName"]
    else:
        out["input_name"] = ""
    if data.get("inputDescription") is not None:
        out["input_description"] = data["inputDescription"]
    if data.get("inputDefinition") is not None:
        import capo_iot_events.types.input_definition

        out["input_definition"] = (
            capo_iot_events.types.input_definition.deserialize_json(
                data["inputDefinition"]
            )
        )
    else:
        raise DeserializationError("CreateInputRequest.input_definition required")
    if data.get("tags") is not None:
        import capo_iot_events.types.tags

        out["tags"] = capo_iot_events.types.tags.deserialize_json(data["tags"])
    return out
