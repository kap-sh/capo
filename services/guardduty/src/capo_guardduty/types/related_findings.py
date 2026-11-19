"""Generated from Smithy shape ``com.amazonaws.guardduty#RelatedFindings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.correlated_findings
    import capo_guardduty.types.observed_finding_types


class RelatedFindings(TypedDict, closed=True):
    correlated: NotRequired[
        "capo_guardduty.types.correlated_findings.CorrelatedFindings"
    ]
    """<p>The findings that GuardDuty correlated with the investigated activity, grouped by finding type.</p>"""
    observed: NotRequired[
        "capo_guardduty.types.observed_finding_types.ObservedFindingTypes"
    ]
    """<p>Other finding types that GuardDuty observed, with counts. These entries don't include finding IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedFindings) -> dict:
    out: dict = {}
    if "correlated" in value:
        import capo_guardduty.types.correlated_findings

        out["correlated"] = capo_guardduty.types.correlated_findings.serialize_json(
            value["correlated"]
        )
    if "observed" in value:
        import capo_guardduty.types.observed_finding_types

        out["observed"] = capo_guardduty.types.observed_finding_types.serialize_json(
            value["observed"]
        )
    return out


def deserialize_json(data: dict) -> RelatedFindings:
    out: RelatedFindings = {}  # type: ignore[typeddict-item]
    if data.get("correlated") is not None:
        import capo_guardduty.types.correlated_findings

        out["correlated"] = capo_guardduty.types.correlated_findings.deserialize_json(
            data["correlated"]
        )
    if data.get("observed") is not None:
        import capo_guardduty.types.observed_finding_types

        out["observed"] = capo_guardduty.types.observed_finding_types.deserialize_json(
            data["observed"]
        )
    return out
