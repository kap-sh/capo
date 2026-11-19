"""Generated from Smithy shape ``com.amazonaws.guardduty#CorrelatedFindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.correlated_finding

CorrelatedFindings: TypeAlias = list[
    "capo_guardduty.types.correlated_finding.CorrelatedFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: CorrelatedFindings) -> list:
    import capo_guardduty.types.correlated_finding

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.correlated_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> CorrelatedFindings:
    import capo_guardduty.types.correlated_finding

    out: CorrelatedFindings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.correlated_finding.deserialize_json(item))
    return out
