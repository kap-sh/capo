"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsSelectedFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.findings_selectable_field

FindingsSelectedFieldList: TypeAlias = list[
    "capo_securityhub.types.findings_selectable_field.FindingsSelectableField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsSelectedFieldList) -> list:
    import capo_securityhub.types.findings_selectable_field

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.findings_selectable_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingsSelectedFieldList:
    import capo_securityhub.types.findings_selectable_field

    out: FindingsSelectedFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityhub.types.findings_selectable_field.deserialize_json(item)
        )
    return out
