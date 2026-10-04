"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.remediation_parameter

RemediationParameterList: TypeAlias = list[
    "capo_securityhub.types.remediation_parameter.RemediationParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationParameterList) -> list:
    import capo_securityhub.types.remediation_parameter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.remediation_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemediationParameterList:
    import capo_securityhub.types.remediation_parameter

    out: RemediationParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.remediation_parameter.deserialize_json(item))
    return out
