"""Generated from Smithy shape ``com.amazonaws.connect#IntegrationAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.instance_id
    import capo_connect.types.integration_association_id
    import capo_connect.types.integration_type
    import capo_connect.types.source_application_name
    import capo_connect.types.source_type
    import capo_connect.types.uri


class IntegrationAssociationSummary(TypedDict, closed=True):
    integration_association_id: NotRequired[
        "capo_connect.types.integration_association_id.IntegrationAssociationId"
    ]
    """<p>The identifier for the AppIntegration association.</p>"""
    integration_association_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the AppIntegration association.</p>"""
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    integration_type: NotRequired["capo_connect.types.integration_type.IntegrationType"]
    """<p>The integration type.</p>"""
    integration_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the AppIntegration.</p>"""
    source_application_url: NotRequired["capo_connect.types.uri.URI"]
    """<p>The URL for the external application.</p>"""
    source_application_name: NotRequired[
        "capo_connect.types.source_application_name.SourceApplicationName"
    ]
    """<p>The user-provided, friendly name for the external application.</p>"""
    source_type: NotRequired["capo_connect.types.source_type.SourceType"]
    """<p>The name of the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationAssociationSummary) -> dict:
    out: dict = {}
    if "integration_association_id" in value:
        out["IntegrationAssociationId"] = value["integration_association_id"]
    if "integration_association_arn" in value:
        out["IntegrationAssociationArn"] = value["integration_association_arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "integration_type" in value:
        import capo_connect.types.integration_type

        out["IntegrationType"] = capo_connect.types.integration_type.serialize_json(
            value["integration_type"]
        )
    if "integration_arn" in value:
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
    return out


def deserialize_json(data: dict) -> IntegrationAssociationSummary:
    out: IntegrationAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("IntegrationAssociationId") is not None:
        out["integration_association_id"] = data["IntegrationAssociationId"]
    if data.get("IntegrationAssociationArn") is not None:
        out["integration_association_arn"] = data["IntegrationAssociationArn"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("IntegrationType") is not None:
        import capo_connect.types.integration_type

        out["integration_type"] = capo_connect.types.integration_type.deserialize_json(
            data["IntegrationType"]
        )
    if data.get("IntegrationArn") is not None:
        out["integration_arn"] = data["IntegrationArn"]
    if data.get("SourceApplicationUrl") is not None:
        out["source_application_url"] = data["SourceApplicationUrl"]
    if data.get("SourceApplicationName") is not None:
        out["source_application_name"] = data["SourceApplicationName"]
    if data.get("SourceType") is not None:
        import capo_connect.types.source_type

        out["source_type"] = capo_connect.types.source_type.deserialize_json(
            data["SourceType"]
        )
    return out
