"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FindingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.failure_category
    import capo_resiliencehubv2.types.finding_severity
    import capo_resiliencehubv2.types.finding_status
    import capo_resiliencehubv2.types.policy_component
    import capo_resiliencehubv2.types.uuid


class FindingSummary(TypedDict, closed=True):
    service_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    finding_id: NotRequired["capo_resiliencehubv2.types.uuid.Uuid"]
    """<p>The unique identifier of the finding.</p>"""
    name: NotRequired["str"]
    """<p>The name of the finding.</p>"""
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    failure_category: NotRequired[
        "capo_resiliencehubv2.types.failure_category.FailureCategory"
    ]
    """<p>The failure category of the finding.</p>"""
    severity: NotRequired["capo_resiliencehubv2.types.finding_severity.FindingSeverity"]
    """<p>The severity of the finding.</p>"""
    status: NotRequired["capo_resiliencehubv2.types.finding_status.FindingStatus"]
    """<p>The current status of the finding.</p>"""
    policy_component: NotRequired[
        "capo_resiliencehubv2.types.policy_component.PolicyComponent"
    ]
    """<p>The policy component associated with the finding.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the finding was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSummary) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "failure_category" in value:
        import capo_resiliencehubv2.types.failure_category

        out["failureCategory"] = (
            capo_resiliencehubv2.types.failure_category.serialize_json(
                value["failure_category"]
            )
        )
    if "severity" in value:
        import capo_resiliencehubv2.types.finding_severity

        out["severity"] = capo_resiliencehubv2.types.finding_severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import capo_resiliencehubv2.types.finding_status

        out["status"] = capo_resiliencehubv2.types.finding_status.serialize_json(
            value["status"]
        )
    if "policy_component" in value:
        import capo_resiliencehubv2.types.policy_component

        out["policyComponent"] = (
            capo_resiliencehubv2.types.policy_component.serialize_json(
                value["policy_component"]
            )
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> FindingSummary:
    out: FindingSummary = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("failureCategory") is not None:
        import capo_resiliencehubv2.types.failure_category

        out["failure_category"] = (
            capo_resiliencehubv2.types.failure_category.deserialize_json(
                data["failureCategory"]
            )
        )
    if data.get("severity") is not None:
        import capo_resiliencehubv2.types.finding_severity

        out["severity"] = capo_resiliencehubv2.types.finding_severity.deserialize_json(
            data["severity"]
        )
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.finding_status

        out["status"] = capo_resiliencehubv2.types.finding_status.deserialize_json(
            data["status"]
        )
    if data.get("policyComponent") is not None:
        import capo_resiliencehubv2.types.policy_component

        out["policy_component"] = (
            capo_resiliencehubv2.types.policy_component.deserialize_json(
                data["policyComponent"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
