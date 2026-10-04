"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.remediation_string_filter

RemediationStringFilterList: TypeAlias = list[
    "capo_securityhub.types.remediation_string_filter.RemediationStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationStringFilterList) -> list:
    import capo_securityhub.types.remediation_string_filter

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.remediation_string_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RemediationStringFilterList:
    import capo_securityhub.types.remediation_string_filter

    out: RemediationStringFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityhub.types.remediation_string_filter.deserialize_json(item)
        )
    return out
