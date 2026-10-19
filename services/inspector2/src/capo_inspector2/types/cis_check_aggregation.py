"""Generated from Smithy shape ``com.amazonaws.inspector2#CisCheckAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.cis_scan_arn
    import capo_inspector2.types.cis_security_level
    import capo_inspector2.types.status_counts


class CisCheckAggregation(TypedDict, closed=True):
    scan_arn: "capo_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The scan ARN for the CIS check scan ARN.</p>"""
    check_id: NotRequired["str"]
    """<p>The check ID for the CIS check.</p>"""
    title: NotRequired["str"]
    """<p>The CIS check title.</p>"""
    check_description: NotRequired["str"]
    """<p>The description for the CIS check.</p>"""
    level: NotRequired["capo_inspector2.types.cis_security_level.CisSecurityLevel"]
    """<p>The CIS check level.</p>"""
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The account ID for the CIS check.</p>"""
    status_counts: NotRequired["capo_inspector2.types.status_counts.StatusCounts"]
    """<p>The CIS check status counts.</p>"""
    platform: NotRequired["str"]
    """<p>The CIS check platform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisCheckAggregation) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "check_id" in value:
        out["checkId"] = value["check_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "check_description" in value:
        out["checkDescription"] = value["check_description"]
    if "level" in value:
        import capo_inspector2.types.cis_security_level

        out["level"] = capo_inspector2.types.cis_security_level.serialize_json(
            value["level"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status_counts" in value:
        import capo_inspector2.types.status_counts

        out["statusCounts"] = capo_inspector2.types.status_counts.serialize_json(
            value["status_counts"]
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> CisCheckAggregation:
    out: CisCheckAggregation = {}  # type: ignore[typeddict-item]
    if data.get("scanArn") is not None:
        out["scan_arn"] = data["scanArn"]
    else:
        out["scan_arn"] = ""
    if data.get("checkId") is not None:
        out["check_id"] = data["checkId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("checkDescription") is not None:
        out["check_description"] = data["checkDescription"]
    if data.get("level") is not None:
        import capo_inspector2.types.cis_security_level

        out["level"] = capo_inspector2.types.cis_security_level.deserialize_json(
            data["level"]
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("statusCounts") is not None:
        import capo_inspector2.types.status_counts

        out["status_counts"] = capo_inspector2.types.status_counts.deserialize_json(
            data["statusCounts"]
        )
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    return out
