"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationResource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_resource_data
    import capo_guardduty.types.investigation_resource_type
    import capo_guardduty.types.string


class InvestigationResource(TypedDict, closed=True):
    uid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique identifier of the resource. This is the Amazon Resource Name (ARN) of the resource when it's available. Otherwise, it's the name or ID of the resource.</p>"""
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the resource.</p>"""
    resource_type: NotRequired[
        "capo_guardduty.types.investigation_resource_type.InvestigationResourceType"
    ]
    """<p>The type of the resource. Possible values are <code>EC2_INSTANCE</code>, <code>EBS_VOLUME</code>, <code>S3_BUCKET</code>, <code>IAM_ROLE</code>, <code>IAM_USER</code>, <code>IAM_ACCESS_KEY</code>, <code>LAMBDA_FUNCTION</code>, <code>EKS_CLUSTER</code>, <code>ECS_CLUSTER</code>, <code>KUBERNETES_WORKLOAD</code>, <code>RDS_INSTANCE</code>, <code>RDS_DB_USER</code>, and <code>EC2_SECURITY_GROUP</code>.</p>"""
    data: NotRequired[
        "capo_guardduty.types.investigation_resource_data.InvestigationResourceData"
    ]
    """<p>Details that are specific to the type of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationResource) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "name" in value:
        out["name"] = value["name"]
    if "resource_type" in value:
        import capo_guardduty.types.investigation_resource_type

        out["resourceType"] = (
            capo_guardduty.types.investigation_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "data" in value:
        import capo_guardduty.types.investigation_resource_data

        out["data"] = capo_guardduty.types.investigation_resource_data.serialize_json(
            value["data"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationResource:
    out: InvestigationResource = {}  # type: ignore[typeddict-item]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("resourceType") is not None:
        import capo_guardduty.types.investigation_resource_type

        out["resource_type"] = (
            capo_guardduty.types.investigation_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if data.get("data") is not None:
        import capo_guardduty.types.investigation_resource_data

        out["data"] = capo_guardduty.types.investigation_resource_data.deserialize_json(
            data["data"]
        )
    return out


def redact_sensitive(value: InvestigationResource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data" in value:
        import capo_guardduty.types.investigation_resource_data

        out["data"] = capo_guardduty.types.investigation_resource_data.redact_sensitive(
            value["data"]
        )
    return out
