"""Generated from Smithy shape ``com.amazonaws.connect#CreateExtractionDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.extraction_configuration
    import capo_connect.types.extraction_definition_display
    import capo_connect.types.extraction_definition_name
    import capo_connect.types.instance_id
    import capo_connect.types.tag_map


class CreateExtractionDefinitionRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.extraction_definition_name.ExtractionDefinitionName"
    """<p>A unique name of the extraction definition.</p>"""
    extraction_configuration: (
        "capo_connect.types.extraction_configuration.ExtractionConfiguration"
    )
    """<p>The configuration that defines how data is extracted, including the prompt hint and not-found behavior.</p>"""
    display: NotRequired[
        "capo_connect.types.extraction_definition_display.ExtractionDefinitionDisplay"
    ]
    """<p>The display settings for the extraction definition, including the label shown in the agent workspace.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExtractionDefinitionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Name"] = value["name"]
    import capo_connect.types.extraction_configuration

    out["ExtractionConfiguration"] = (
        capo_connect.types.extraction_configuration.serialize_json(
            value["extraction_configuration"]
        )
    )
    if "display" in value:
        import capo_connect.types.extraction_definition_display

        out["Display"] = (
            capo_connect.types.extraction_definition_display.serialize_json(
                value["display"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateExtractionDefinitionRequest:
    out: CreateExtractionDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateExtractionDefinitionRequest.name required")
    if data.get("ExtractionConfiguration") is not None:
        import capo_connect.types.extraction_configuration

        out["extraction_configuration"] = (
            capo_connect.types.extraction_configuration.deserialize_json(
                data["ExtractionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateExtractionDefinitionRequest.extraction_configuration required"
        )
    if data.get("Display") is not None:
        import capo_connect.types.extraction_definition_display

        out["display"] = (
            capo_connect.types.extraction_definition_display.deserialize_json(
                data["Display"]
            )
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
