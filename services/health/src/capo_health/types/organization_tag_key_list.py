"""Generated from Smithy shape ``com.amazonaws.health#OrganizationTagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.organization_tag_key

OrganizationTagKeyList: TypeAlias = list[
    "capo_health.types.organization_tag_key.OrganizationTagKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationTagKeyList) -> list:
    import capo_health.types.organization_tag_key

    out: list = []
    for item in value:
        out.append(capo_health.types.organization_tag_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationTagKeyList:
    import capo_health.types.organization_tag_key

    out: OrganizationTagKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.organization_tag_key.deserialize_aws_json_1_1(item)
        )
    return out
