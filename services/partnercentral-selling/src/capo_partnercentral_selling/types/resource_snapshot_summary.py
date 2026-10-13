"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_snapshot_arn
    import capo_partnercentral_selling.types.resource_snapshot_revision
    import capo_partnercentral_selling.types.resource_template_name
    import capo_partnercentral_selling.types.resource_type


class ResourceSnapshotSummary(TypedDict, closed=True):
    arn: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_arn.ResourceSnapshotArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the snapshot. This globally unique identifier can be used for cross-service references and in IAM policies. </p>"""
    revision: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_revision.ResourceSnapshotRevision"
    ]
    """<p>The revision number of the snapshot. This integer value is incremented each time the snapshot is updated, allowing for version tracking of the resource snapshot. </p>"""
    resource_type: NotRequired[
        "capo_partnercentral_selling.types.resource_type.ResourceType"
    ]
    """<p>The type of resource snapshotted.</p>"""
    resource_id: NotRequired[
        "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>The identifier of the specific resource snapshotted. The format might vary depending on the ResourceType. </p>"""
    resource_snapshot_template_name: NotRequired[
        "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    ]
    """<p>The name of the template used to create the snapshot.</p>"""
    created_by: NotRequired["capo_partnercentral_selling.types.aws_account.AwsAccount"]
    """<p>The AWS account ID of the entity that owns the resource from which the snapshot was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSnapshotSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "revision" in value:
        out["Revision"] = value["revision"]
    if "resource_type" in value:
        import capo_partnercentral_selling.types.resource_type

        out["ResourceType"] = (
            capo_partnercentral_selling.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_snapshot_template_name" in value:
        out["ResourceSnapshotTemplateName"] = value["resource_snapshot_template_name"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSnapshotSummary:
    out: ResourceSnapshotSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    if data.get("ResourceType") is not None:
        import capo_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            capo_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceSnapshotTemplateName") is not None:
        out["resource_snapshot_template_name"] = data["ResourceSnapshotTemplateName"]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    return out


def redact_sensitive(value: ResourceSnapshotSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "created_by" in value:
        out["created_by"] = "*** Sensitive Data Redacted ***"
    return out
