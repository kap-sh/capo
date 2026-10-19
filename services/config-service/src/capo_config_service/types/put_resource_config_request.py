"""Generated from Smithy shape ``com.amazonaws.configservice#PutResourceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.configuration
    import capo_config_service.types.resource_id
    import capo_config_service.types.resource_name
    import capo_config_service.types.resource_type_string
    import capo_config_service.types.schema_version_id
    import capo_config_service.types.tags


class PutResourceConfigRequest(TypedDict, closed=True):
    resource_type: "capo_config_service.types.resource_type_string.ResourceTypeString"
    """<p>The type of the resource. The custom resource type must be registered with CloudFormation. </p> <note> <p>You cannot use the organization names “amzn”, “amazon”, “alexa”, “custom” with custom resource types. It is the first part of the ResourceType up to the first ::.</p> </note>"""
    schema_version_id: "capo_config_service.types.schema_version_id.SchemaVersionId"
    """<p>Version of the schema registered for the ResourceType in CloudFormation.</p>"""
    resource_id: "capo_config_service.types.resource_id.ResourceId"
    """<p>Unique identifier of the resource.</p>"""
    resource_name: NotRequired["capo_config_service.types.resource_name.ResourceName"]
    """<p>Name of the resource.</p>"""
    configuration: "capo_config_service.types.configuration.Configuration"
    """<p>The configuration object of the resource in valid JSON format. It must match the schema registered with CloudFormation.</p> <note> <p>The configuration JSON must not exceed 64 KB.</p> </note>"""
    tags: NotRequired["capo_config_service.types.tags.Tags"]
    """<p>Tags associated with the resource.</p> <note> <p>This field is not to be confused with the Amazon Web Services-wide tag feature for Amazon Web Services resources. Tags for <code>PutResourceConfig</code> are tags that you supply for the configuration items of your custom resources.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourceConfigRequest) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    out["SchemaVersionId"] = value["schema_version_id"]
    out["ResourceId"] = value["resource_id"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    out["Configuration"] = value["configuration"]
    if "tags" in value:
        import capo_config_service.types.tags

        out["Tags"] = capo_config_service.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourceConfigRequest:
    out: PutResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("SchemaVersionId") is not None:
        out["schema_version_id"] = data["SchemaVersionId"]
    else:
        out["schema_version_id"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    if data.get("Configuration") is not None:
        out["configuration"] = data["Configuration"]
    else:
        out["configuration"] = ""
    if data.get("Tags") is not None:
        import capo_config_service.types.tags

        out["tags"] = capo_config_service.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
