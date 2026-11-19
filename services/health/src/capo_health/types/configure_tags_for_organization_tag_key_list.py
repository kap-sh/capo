"""Generated from Smithy shape ``com.amazonaws.health#ConfigureTagsForOrganizationTagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.tag_key_for_organization

ConfigureTagsForOrganizationTagKeyList: TypeAlias = list[
    "capo_health.types.tag_key_for_organization.TagKeyForOrganization"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigureTagsForOrganizationTagKeyList) -> list:
    import capo_health.types.tag_key_for_organization

    out: list = []
    for item in value:
        out.append(
            capo_health.types.tag_key_for_organization.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigureTagsForOrganizationTagKeyList:
    import capo_health.types.tag_key_for_organization

    out: ConfigureTagsForOrganizationTagKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.tag_key_for_organization.deserialize_aws_json_1_1(item)
        )
    return out
