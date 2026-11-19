"""Generated from Smithy shape ``com.amazonaws.guardduty#RepresentativeFindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.representative_finding

RepresentativeFindings: TypeAlias = list[
    "capo_guardduty.types.representative_finding.RepresentativeFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: RepresentativeFindings) -> list:
    import capo_guardduty.types.representative_finding

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.representative_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> RepresentativeFindings:
    import capo_guardduty.types.representative_finding

    out: RepresentativeFindings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.representative_finding.deserialize_json(item))
    return out
