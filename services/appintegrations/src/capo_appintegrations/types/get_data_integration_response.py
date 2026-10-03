"""Generated from Smithy shape ``com.amazonaws.appintegrations#GetDataIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.description
    import capo_appintegrations.types.file_configuration
    import capo_appintegrations.types.name
    import capo_appintegrations.types.non_blank_string
    import capo_appintegrations.types.object_configuration
    import capo_appintegrations.types.schedule_configuration
    import capo_appintegrations.types.source_uri
    import capo_appintegrations.types.tag_map
    import capo_appintegrations.types.uuid


class GetDataIntegrationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the DataIntegration.</p>"""
    id: NotRequired["capo_appintegrations.types.uuid.UUID"]
    """<p>A unique identifier.</p>"""
    name: NotRequired["capo_appintegrations.types.name.Name"]
    """<p>The name of the DataIntegration.</p>"""
    description: NotRequired["capo_appintegrations.types.description.Description"]
    """<p>The KMS key ARN for the DataIntegration.</p>"""
    kms_key: NotRequired["capo_appintegrations.types.non_blank_string.NonBlankString"]
    """<p>The KMS key ARN for the DataIntegration.</p>"""
    source_uri: NotRequired["capo_appintegrations.types.source_uri.SourceURI"]
    """<p>The URI of the data source.</p>"""
    schedule_configuration: NotRequired[
        "capo_appintegrations.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The name of the data and how often it should be pulled from the source.</p>"""
    tags: NotRequired["capo_appintegrations.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    file_configuration: NotRequired[
        "capo_appintegrations.types.file_configuration.FileConfiguration"
    ]
    """<p>The configuration for what files should be pulled from the source.</p>"""
    object_configuration: NotRequired[
        "capo_appintegrations.types.object_configuration.ObjectConfiguration"
    ]
    """<p>The configuration for what data should be pulled from the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    if "source_uri" in value:
        out["SourceURI"] = value["source_uri"]
    if "schedule_configuration" in value:
        import capo_appintegrations.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            capo_appintegrations.types.schedule_configuration.serialize_json(
                value["schedule_configuration"]
            )
        )
    if "tags" in value:
        import capo_appintegrations.types.tag_map

        out["Tags"] = capo_appintegrations.types.tag_map.serialize_json(value["tags"])
    if "file_configuration" in value:
        import capo_appintegrations.types.file_configuration

        out["FileConfiguration"] = (
            capo_appintegrations.types.file_configuration.serialize_json(
                value["file_configuration"]
            )
        )
    if "object_configuration" in value:
        import capo_appintegrations.types.object_configuration

        out["ObjectConfiguration"] = (
            capo_appintegrations.types.object_configuration.serialize_json(
                value["object_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataIntegrationResponse:
    out: GetDataIntegrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    if data.get("SourceURI") is not None:
        out["source_uri"] = data["SourceURI"]
    if data.get("ScheduleConfiguration") is not None:
        import capo_appintegrations.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_appintegrations.types.schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_appintegrations.types.tag_map

        out["tags"] = capo_appintegrations.types.tag_map.deserialize_json(data["Tags"])
    if data.get("FileConfiguration") is not None:
        import capo_appintegrations.types.file_configuration

        out["file_configuration"] = (
            capo_appintegrations.types.file_configuration.deserialize_json(
                data["FileConfiguration"]
            )
        )
    if data.get("ObjectConfiguration") is not None:
        import capo_appintegrations.types.object_configuration

        out["object_configuration"] = (
            capo_appintegrations.types.object_configuration.deserialize_json(
                data["ObjectConfiguration"]
            )
        )
    return out
