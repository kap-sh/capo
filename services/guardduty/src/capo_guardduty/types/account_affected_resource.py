"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountAffectedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.investigation_resource_type
    import capo_guardduty.types.string


class AccountAffectedResource(TypedDict, closed=True):
    identifier: NotRequired["capo_guardduty.types.string.String"]
    """<p>The identifier of the resource.</p>"""
    type: NotRequired[
        "capo_guardduty.types.investigation_resource_type.InvestigationResourceType"
    ]
    """<p>The type of the resource. Possible values are <code>EC2_INSTANCE</code>, <code>EBS_VOLUME</code>, <code>S3_BUCKET</code>, <code>IAM_ROLE</code>, <code>IAM_USER</code>, <code>IAM_ACCESS_KEY</code>, <code>LAMBDA_FUNCTION</code>, <code>EKS_CLUSTER</code>, <code>ECS_CLUSTER</code>, <code>KUBERNETES_WORKLOAD</code>, <code>RDS_INSTANCE</code>, <code>RDS_DB_USER</code>, and <code>EC2_SECURITY_GROUP</code>.</p>"""
    finding_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountAffectedResource) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "type" in value:
        import capo_guardduty.types.investigation_resource_type

        out["type"] = capo_guardduty.types.investigation_resource_type.serialize_json(
            value["type"]
        )
    if "finding_count" in value:
        out["findingCount"] = value["finding_count"]
    return out


def deserialize_json(data: dict) -> AccountAffectedResource:
    out: AccountAffectedResource = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("type") is not None:
        import capo_guardduty.types.investigation_resource_type

        out["type"] = capo_guardduty.types.investigation_resource_type.deserialize_json(
            data["type"]
        )
    if data.get("findingCount") is not None:
        out["finding_count"] = data["findingCount"]
    return out
