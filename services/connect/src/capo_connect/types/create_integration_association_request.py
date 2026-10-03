"""Generated from Smithy shape ``com.amazonaws.connect#CreateIntegrationAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.instance_id
    import capo_connect.types.integration_type
    import capo_connect.types.source_application_name
    import capo_connect.types.source_type
    import capo_connect.types.tag_map
    import capo_connect.types.uri


class CreateIntegrationAssociationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    integration_type: "capo_connect.types.integration_type.IntegrationType"
    """<p>The type of information to be ingested.</p>"""
    integration_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the integration.</p> <note> <p>When integrating with Amazon Web Services End User Messaging, the Connect Customer and Amazon Web Services End User Messaging instances must be in the same account.</p> </note>"""
    source_application_url: NotRequired["capo_connect.types.uri.URI"]
    """<p>The URL for the external application. This field is only required for the EVENT integration type.</p>"""
    source_application_name: NotRequired[
        "capo_connect.types.source_application_name.SourceApplicationName"
    ]
    """<p>The name of the external application. This field is only required for the EVENT integration type.</p>"""
    source_type: NotRequired["capo_connect.types.source_type.SourceType"]
    """<p>The type of the data source. This field is only required for the EVENT integration type.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationAssociationRequest) -> dict:
    out: dict = {}
    import capo_connect.types.integration_type

    out["IntegrationType"] = capo_connect.types.integration_type.serialize_json(
        value["integration_type"]
    )
    out["IntegrationArn"] = value["integration_arn"]
    if "source_application_url" in value:
        out["SourceApplicationUrl"] = value["source_application_url"]
    if "source_application_name" in value:
        out["SourceApplicationName"] = value["source_application_name"]
    if "source_type" in value:
        import capo_connect.types.source_type

        out["SourceType"] = capo_connect.types.source_type.serialize_json(
            value["source_type"]
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIntegrationAssociationRequest:
    out: CreateIntegrationAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("IntegrationType") is not None:
        import capo_connect.types.integration_type

        out["integration_type"] = capo_connect.types.integration_type.deserialize_json(
            data["IntegrationType"]
        )
    else:
        raise DeserializationError(
            "CreateIntegrationAssociationRequest.integration_type required"
        )
    if data.get("IntegrationArn") is not None:
        out["integration_arn"] = data["IntegrationArn"]
    else:
        raise DeserializationError(
            "CreateIntegrationAssociationRequest.integration_arn required"
        )
    if data.get("SourceApplicationUrl") is not None:
        out["source_application_url"] = data["SourceApplicationUrl"]
    if data.get("SourceApplicationName") is not None:
        out["source_application_name"] = data["SourceApplicationName"]
    if data.get("SourceType") is not None:
        import capo_connect.types.source_type

        out["source_type"] = capo_connect.types.source_type.deserialize_json(
            data["SourceType"]
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
