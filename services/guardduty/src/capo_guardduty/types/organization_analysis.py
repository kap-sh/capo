"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_summaries
    import capo_guardduty.types.organization_findings_summary


class OrganizationAnalysis(TypedDict, closed=True):
    findings_summary: NotRequired[
        "capo_guardduty.types.organization_findings_summary.OrganizationFindingsSummary"
    ]
    """<p>A summary of the findings across the organization.</p>"""
    account_breakdown: NotRequired[
        "capo_guardduty.types.account_summaries.AccountSummaries"
    ]
    """<p>The accounts in the organization that have findings, with the number of findings in each.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationAnalysis) -> dict:
    out: dict = {}
    if "findings_summary" in value:
        import capo_guardduty.types.organization_findings_summary

        out["findingsSummary"] = (
            capo_guardduty.types.organization_findings_summary.serialize_json(
                value["findings_summary"]
            )
        )
    if "account_breakdown" in value:
        import capo_guardduty.types.account_summaries

        out["accountBreakdown"] = capo_guardduty.types.account_summaries.serialize_json(
            value["account_breakdown"]
        )
    return out


def deserialize_json(data: dict) -> OrganizationAnalysis:
    out: OrganizationAnalysis = {}  # type: ignore[typeddict-item]
    if data.get("findingsSummary") is not None:
        import capo_guardduty.types.organization_findings_summary

        out["findings_summary"] = (
            capo_guardduty.types.organization_findings_summary.deserialize_json(
                data["findingsSummary"]
            )
        )
    if data.get("accountBreakdown") is not None:
        import capo_guardduty.types.account_summaries

        out["account_breakdown"] = (
            capo_guardduty.types.account_summaries.deserialize_json(
                data["accountBreakdown"]
            )
        )
    return out
