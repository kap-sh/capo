"""Generated from Smithy shape ``com.amazonaws.connect#ExtractionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.extraction_configuration
    import capo_connect.types.extraction_definition_display
    import capo_connect.types.extraction_definition_id
    import capo_connect.types.extraction_definition_name
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp


class ExtractionDefinition(TypedDict, closed=True):
    name: "capo_connect.types.extraction_definition_name.ExtractionDefinitionName"
    """<p>The name of the extraction definition.</p>"""
    extraction_definition_id: (
        "capo_connect.types.extraction_definition_id.ExtractionDefinitionId"
    )
    """<p>The identifier of the extraction definition.</p>"""
    extraction_definition_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the extraction definition.</p>"""
    extraction_configuration: (
        "capo_connect.types.extraction_configuration.ExtractionConfiguration"
    )
    """<p>The configuration that defines how data is extracted.</p>"""
    display: NotRequired[
        "capo_connect.types.extraction_definition_display.ExtractionDefinitionDisplay"
    ]
    """<p>The display settings for the extraction definition.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the extraction definition was created.</p>"""
    last_updated_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the extraction definition was last updated.</p>"""
    last_updated_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the extraction definition.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionDefinition) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ExtractionDefinitionId"] = value["extraction_definition_id"]
    out["ExtractionDefinitionArn"] = value["extraction_definition_arn"]
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
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_connect.types.timestamp

    out["LastUpdatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    out["LastUpdatedBy"] = value["last_updated_by"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ExtractionDefinition:
    out: ExtractionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ExtractionDefinitionId") is not None:
        out["extraction_definition_id"] = data["ExtractionDefinitionId"]
    else:
        out["extraction_definition_id"] = ""
    if data.get("ExtractionDefinitionArn") is not None:
        out["extraction_definition_arn"] = data["ExtractionDefinitionArn"]
    else:
        out["extraction_definition_arn"] = ""
    if data.get("ExtractionConfiguration") is not None:
        import capo_connect.types.extraction_configuration

        out["extraction_configuration"] = (
            capo_connect.types.extraction_configuration.deserialize_json(
                data["ExtractionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ExtractionDefinition.extraction_configuration required"
        )
    if data.get("Display") is not None:
        import capo_connect.types.extraction_definition_display

        out["display"] = (
            capo_connect.types.extraction_definition_display.deserialize_json(
                data["Display"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_connect.types.timestamp

        out["last_updated_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdatedBy") is not None:
        out["last_updated_by"] = data["LastUpdatedBy"]
    else:
        out["last_updated_by"] = ""
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
