"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationOutcome``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class RemediationOutcome(TypedDict, closed=True):
    resolved_findings_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of associated exposure findings that are resolved by remediating the target.</p>"""
    severity_reduction_findings_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of associated exposure findings whose severity is reduced by remediating the target.</p>"""
    severity_unchanged_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of associated exposure findings whose severity is unchanged by remediating the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationOutcome) -> dict:
    out: dict = {}
    if "resolved_findings_count" in value:
        out["ResolvedFindingsCount"] = value["resolved_findings_count"]
    if "severity_reduction_findings_count" in value:
        out["SeverityReductionFindingsCount"] = value[
            "severity_reduction_findings_count"
        ]
    if "severity_unchanged_count" in value:
        out["SeverityUnchangedCount"] = value["severity_unchanged_count"]
    return out


def deserialize_json(data: dict) -> RemediationOutcome:
    out: RemediationOutcome = {}  # type: ignore[typeddict-item]
    if data.get("ResolvedFindingsCount") is not None:
        out["resolved_findings_count"] = data["ResolvedFindingsCount"]
    if data.get("SeverityReductionFindingsCount") is not None:
        out["severity_reduction_findings_count"] = data[
            "SeverityReductionFindingsCount"
        ]
    if data.get("SeverityUnchangedCount") is not None:
        out["severity_unchanged_count"] = data["SeverityUnchangedCount"]
    return out
