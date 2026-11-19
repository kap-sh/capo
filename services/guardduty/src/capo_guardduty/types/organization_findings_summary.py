"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFindingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.finding_type_counts
    import capo_guardduty.types.integer
    import capo_guardduty.types.severity_breakdown
    import capo_guardduty.types.time_window_groups


class OrganizationFindingsSummary(TypedDict, closed=True):
    total_findings: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The total number of findings across the organization.</p>"""
    severity_breakdown: NotRequired[
        "capo_guardduty.types.severity_breakdown.SeverityBreakdown"
    ]
    """<p>The number of findings at each severity level across the organization.</p>"""
    top_finding_types: NotRequired[
        "capo_guardduty.types.finding_type_counts.FindingTypeCounts"
    ]
    """<p>The finding types that have the most findings, with counts.</p>"""
    by_time_window: NotRequired[
        "capo_guardduty.types.time_window_groups.TimeWindowGroups"
    ]
    """<p>The number of findings in each time window.</p>"""
    total_account_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The total number of accounts in the organization.</p>"""
    affected_account_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of accounts that have findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationFindingsSummary) -> dict:
    out: dict = {}
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    if "severity_breakdown" in value:
        import capo_guardduty.types.severity_breakdown

        out["severityBreakdown"] = (
            capo_guardduty.types.severity_breakdown.serialize_json(
                value["severity_breakdown"]
            )
        )
    if "top_finding_types" in value:
        import capo_guardduty.types.finding_type_counts

        out["topFindingTypes"] = (
            capo_guardduty.types.finding_type_counts.serialize_json(
                value["top_finding_types"]
            )
        )
    if "by_time_window" in value:
        import capo_guardduty.types.time_window_groups

        out["byTimeWindow"] = capo_guardduty.types.time_window_groups.serialize_json(
            value["by_time_window"]
        )
    if "total_account_count" in value:
        out["totalAccountCount"] = value["total_account_count"]
    if "affected_account_count" in value:
        out["affectedAccountCount"] = value["affected_account_count"]
    return out


def deserialize_json(data: dict) -> OrganizationFindingsSummary:
    out: OrganizationFindingsSummary = {}  # type: ignore[typeddict-item]
    if data.get("totalFindings") is not None:
        out["total_findings"] = data["totalFindings"]
    if data.get("severityBreakdown") is not None:
        import capo_guardduty.types.severity_breakdown

        out["severity_breakdown"] = (
            capo_guardduty.types.severity_breakdown.deserialize_json(
                data["severityBreakdown"]
            )
        )
    if data.get("topFindingTypes") is not None:
        import capo_guardduty.types.finding_type_counts

        out["top_finding_types"] = (
            capo_guardduty.types.finding_type_counts.deserialize_json(
                data["topFindingTypes"]
            )
        )
    if data.get("byTimeWindow") is not None:
        import capo_guardduty.types.time_window_groups

        out["by_time_window"] = (
            capo_guardduty.types.time_window_groups.deserialize_json(
                data["byTimeWindow"]
            )
        )
    if data.get("totalAccountCount") is not None:
        out["total_account_count"] = data["totalAccountCount"]
    if data.get("affectedAccountCount") is not None:
        out["affected_account_count"] = data["affectedAccountCount"]
    return out
