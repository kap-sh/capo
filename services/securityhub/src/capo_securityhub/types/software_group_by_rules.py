"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareGroupByRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.software_group_by_rule

SoftwareGroupByRules: TypeAlias = list[
    "capo_securityhub.types.software_group_by_rule.SoftwareGroupByRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareGroupByRules) -> list:
    import capo_securityhub.types.software_group_by_rule

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.software_group_by_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> SoftwareGroupByRules:
    import capo_securityhub.types.software_group_by_rule

    out: SoftwareGroupByRules = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.software_group_by_rule.deserialize_json(item))
    return out
