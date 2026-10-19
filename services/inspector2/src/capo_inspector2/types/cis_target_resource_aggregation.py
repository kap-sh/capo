"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetResourceAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.cis_scan_arn
    import capo_inspector2.types.cis_target_status
    import capo_inspector2.types.cis_target_status_reason
    import capo_inspector2.types.resource_id
    import capo_inspector2.types.status_counts
    import capo_inspector2.types.target_resource_tags


class CisTargetResourceAggregation(TypedDict, closed=True):
    scan_arn: "capo_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The scan ARN for the CIS target resource.</p>"""
    target_resource_id: NotRequired["capo_inspector2.types.resource_id.ResourceId"]
    """<p>The ID of the target resource.</p>"""
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The account ID for the CIS target resource.</p>"""
    target_resource_tags: NotRequired[
        "capo_inspector2.types.target_resource_tags.TargetResourceTags"
    ]
    """<p>The tag for the target resource.</p>"""
    status_counts: NotRequired["capo_inspector2.types.status_counts.StatusCounts"]
    """<p>The target resource status counts.</p>"""
    platform: NotRequired["str"]
    """<p>The platform for the CIS target resource.</p>"""
    target_status: NotRequired[
        "capo_inspector2.types.cis_target_status.CisTargetStatus"
    ]
    """<p>The status of the target resource.</p>"""
    target_status_reason: NotRequired[
        "capo_inspector2.types.cis_target_status_reason.CisTargetStatusReason"
    ]
    """<p>The reason for the target resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetResourceAggregation) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "target_resource_id" in value:
        out["targetResourceId"] = value["target_resource_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "target_resource_tags" in value:
        import capo_inspector2.types.target_resource_tags

        out["targetResourceTags"] = (
            capo_inspector2.types.target_resource_tags.serialize_json(
                value["target_resource_tags"]
            )
        )
    if "status_counts" in value:
        import capo_inspector2.types.status_counts

        out["statusCounts"] = capo_inspector2.types.status_counts.serialize_json(
            value["status_counts"]
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    if "target_status" in value:
        import capo_inspector2.types.cis_target_status

        out["targetStatus"] = capo_inspector2.types.cis_target_status.serialize_json(
            value["target_status"]
        )
    if "target_status_reason" in value:
        import capo_inspector2.types.cis_target_status_reason

        out["targetStatusReason"] = (
            capo_inspector2.types.cis_target_status_reason.serialize_json(
                value["target_status_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> CisTargetResourceAggregation:
    out: CisTargetResourceAggregation = {}  # type: ignore[typeddict-item]
    if data.get("scanArn") is not None:
        out["scan_arn"] = data["scanArn"]
    else:
        out["scan_arn"] = ""
    if data.get("targetResourceId") is not None:
        out["target_resource_id"] = data["targetResourceId"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("targetResourceTags") is not None:
        import capo_inspector2.types.target_resource_tags

        out["target_resource_tags"] = (
            capo_inspector2.types.target_resource_tags.deserialize_json(
                data["targetResourceTags"]
            )
        )
    if data.get("statusCounts") is not None:
        import capo_inspector2.types.status_counts

        out["status_counts"] = capo_inspector2.types.status_counts.deserialize_json(
            data["statusCounts"]
        )
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("targetStatus") is not None:
        import capo_inspector2.types.cis_target_status

        out["target_status"] = capo_inspector2.types.cis_target_status.deserialize_json(
            data["targetStatus"]
        )
    if data.get("targetStatusReason") is not None:
        import capo_inspector2.types.cis_target_status_reason

        out["target_status_reason"] = (
            capo_inspector2.types.cis_target_status_reason.deserialize_json(
                data["targetStatusReason"]
            )
        )
    return out
