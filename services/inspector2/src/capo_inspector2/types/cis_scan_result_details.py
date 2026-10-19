"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.cis_finding_arn
    import capo_inspector2.types.cis_finding_status
    import capo_inspector2.types.cis_scan_arn
    import capo_inspector2.types.cis_security_level
    import capo_inspector2.types.resource_id


class CisScanResultDetails(TypedDict, closed=True):
    scan_arn: "capo_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The CIS scan result details' scan ARN.</p>"""
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The CIS scan result details' account ID.</p>"""
    target_resource_id: NotRequired["capo_inspector2.types.resource_id.ResourceId"]
    """<p>The CIS scan result details' target resource ID.</p>"""
    platform: NotRequired["str"]
    """<p>The CIS scan result details' platform.</p>"""
    status: NotRequired["capo_inspector2.types.cis_finding_status.CisFindingStatus"]
    """<p>The CIS scan result details' status.</p>"""
    status_reason: NotRequired["str"]
    """<p>The CIS scan result details' status reason.</p>"""
    check_id: NotRequired["str"]
    """<p>The CIS scan result details' check ID.</p>"""
    title: NotRequired["str"]
    """<p>The CIS scan result details' title.</p>"""
    check_description: NotRequired["str"]
    """<p>The account ID that's associated with the CIS scan result details.</p>"""
    remediation: NotRequired["str"]
    """<p>The CIS scan result details' remediation.</p>"""
    level: NotRequired["capo_inspector2.types.cis_security_level.CisSecurityLevel"]
    """<p>The CIS scan result details' level.</p>"""
    finding_arn: NotRequired["capo_inspector2.types.cis_finding_arn.CisFindingArn"]
    """<p>The CIS scan result details' finding ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisScanResultDetails) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "target_resource_id" in value:
        out["targetResourceId"] = value["target_resource_id"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "status" in value:
        import capo_inspector2.types.cis_finding_status

        out["status"] = capo_inspector2.types.cis_finding_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "check_id" in value:
        out["checkId"] = value["check_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "check_description" in value:
        out["checkDescription"] = value["check_description"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    if "level" in value:
        import capo_inspector2.types.cis_security_level

        out["level"] = capo_inspector2.types.cis_security_level.serialize_json(
            value["level"]
        )
    if "finding_arn" in value:
        out["findingArn"] = value["finding_arn"]
    return out


def deserialize_json(data: dict) -> CisScanResultDetails:
    out: CisScanResultDetails = {}  # type: ignore[typeddict-item]
    if data.get("scanArn") is not None:
        out["scan_arn"] = data["scanArn"]
    else:
        out["scan_arn"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("targetResourceId") is not None:
        out["target_resource_id"] = data["targetResourceId"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("status") is not None:
        import capo_inspector2.types.cis_finding_status

        out["status"] = capo_inspector2.types.cis_finding_status.deserialize_json(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("checkId") is not None:
        out["check_id"] = data["checkId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("checkDescription") is not None:
        out["check_description"] = data["checkDescription"]
    if data.get("remediation") is not None:
        out["remediation"] = data["remediation"]
    if data.get("level") is not None:
        import capo_inspector2.types.cis_security_level

        out["level"] = capo_inspector2.types.cis_security_level.deserialize_json(
            data["level"]
        )
    if data.get("findingArn") is not None:
        out["finding_arn"] = data["findingArn"]
    return out
