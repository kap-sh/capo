"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationV2ItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.remediation_v2_item

RemediationV2ItemList: TypeAlias = list[
    "capo_securityhub.types.remediation_v2_item.RemediationV2Item"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationV2ItemList) -> list:
    import capo_securityhub.types.remediation_v2_item

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.remediation_v2_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemediationV2ItemList:
    import capo_securityhub.types.remediation_v2_item

    out: RemediationV2ItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.remediation_v2_item.deserialize_json(item))
    return out
