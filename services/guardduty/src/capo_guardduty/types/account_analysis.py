"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_affected_resources
    import capo_guardduty.types.findings_summary
    import capo_guardduty.types.tactic_coverages


class AccountAnalysis(TypedDict, closed=True):
    findings_summary: NotRequired[
        "capo_guardduty.types.findings_summary.FindingsSummary"
    ]
    """<p>A summary of the findings in the account.</p>"""
    tactic_coverage: NotRequired[
        "capo_guardduty.types.tactic_coverages.TacticCoverages"
    ]
    """<p>The findings in the account, mapped to MITRE ATT&amp;CK tactics and techniques.</p>"""
    affected_resources: NotRequired[
        "capo_guardduty.types.account_affected_resources.AccountAffectedResources"
    ]
    """<p>The resources in the account that are associated with findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountAnalysis) -> dict:
    out: dict = {}
    if "findings_summary" in value:
        import capo_guardduty.types.findings_summary

        out["findingsSummary"] = capo_guardduty.types.findings_summary.serialize_json(
            value["findings_summary"]
        )
    if "tactic_coverage" in value:
        import capo_guardduty.types.tactic_coverages

        out["tacticCoverage"] = capo_guardduty.types.tactic_coverages.serialize_json(
            value["tactic_coverage"]
        )
    if "affected_resources" in value:
        import capo_guardduty.types.account_affected_resources

        out["affectedResources"] = (
            capo_guardduty.types.account_affected_resources.serialize_json(
                value["affected_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountAnalysis:
    out: AccountAnalysis = {}  # type: ignore[typeddict-item]
    if data.get("findingsSummary") is not None:
        import capo_guardduty.types.findings_summary

        out["findings_summary"] = (
            capo_guardduty.types.findings_summary.deserialize_json(
                data["findingsSummary"]
            )
        )
    if data.get("tacticCoverage") is not None:
        import capo_guardduty.types.tactic_coverages

        out["tactic_coverage"] = capo_guardduty.types.tactic_coverages.deserialize_json(
            data["tacticCoverage"]
        )
    if data.get("affectedResources") is not None:
        import capo_guardduty.types.account_affected_resources

        out["affected_resources"] = (
            capo_guardduty.types.account_affected_resources.deserialize_json(
                data["affectedResources"]
            )
        )
    return out
