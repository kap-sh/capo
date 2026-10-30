"""Generated from Smithy shape ``com.amazonaws.continuum#FindingComplianceCheckList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.finding_compliance_check

FindingComplianceCheckList: TypeAlias = list[
    "capo_continuum.types.finding_compliance_check.FindingComplianceCheck"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingComplianceCheckList) -> list:
    import capo_continuum.types.finding_compliance_check

    out: list = []
    for item in value:
        out.append(capo_continuum.types.finding_compliance_check.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingComplianceCheckList:
    import capo_continuum.types.finding_compliance_check

    out: FindingComplianceCheckList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.finding_compliance_check.deserialize_json(item))
    return out
