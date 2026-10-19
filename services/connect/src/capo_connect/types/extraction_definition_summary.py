"""Generated from Smithy shape ``com.amazonaws.connect#ExtractionDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.extraction_definition_id
    import capo_connect.types.extraction_definition_name
    import capo_connect.types.timestamp


class ExtractionDefinitionSummary(TypedDict, closed=True):
    name: "capo_connect.types.extraction_definition_name.ExtractionDefinitionName"
    """<p>The name of the extraction definition.</p>"""
    extraction_definition_id: (
        "capo_connect.types.extraction_definition_id.ExtractionDefinitionId"
    )
    """<p>The identifier of the extraction definition.</p>"""
    extraction_definition_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the extraction definition.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the extraction definition was created.</p>"""
    last_updated_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the extraction definition was last updated.</p>"""
    last_updated_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the extraction definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionDefinitionSummary) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ExtractionDefinitionId"] = value["extraction_definition_id"]
    out["ExtractionDefinitionArn"] = value["extraction_definition_arn"]
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_connect.types.timestamp

    out["LastUpdatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    out["LastUpdatedBy"] = value["last_updated_by"]
    return out


def deserialize_json(data: dict) -> ExtractionDefinitionSummary:
    out: ExtractionDefinitionSummary = {}  # type: ignore[typeddict-item]
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
    return out
