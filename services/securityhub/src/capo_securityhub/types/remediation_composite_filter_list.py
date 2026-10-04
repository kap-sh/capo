"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationCompositeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.remediation_composite_filter

RemediationCompositeFilterList: TypeAlias = list[
    "capo_securityhub.types.remediation_composite_filter.RemediationCompositeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationCompositeFilterList) -> list:
    import capo_securityhub.types.remediation_composite_filter

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.remediation_composite_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RemediationCompositeFilterList:
    import capo_securityhub.types.remediation_composite_filter

    out: RemediationCompositeFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityhub.types.remediation_composite_filter.deserialize_json(item)
        )
    return out
