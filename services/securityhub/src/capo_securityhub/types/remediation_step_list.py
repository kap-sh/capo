"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.remediation_step

RemediationStepList: TypeAlias = list[
    "capo_securityhub.types.remediation_step.RemediationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationStepList) -> list:
    import capo_securityhub.types.remediation_step

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.remediation_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemediationStepList:
    import capo_securityhub.types.remediation_step

    out: RemediationStepList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.remediation_step.deserialize_json(item))
    return out
