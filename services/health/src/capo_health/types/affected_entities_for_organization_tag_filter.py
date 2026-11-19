"""Generated from Smithy shape ``com.amazonaws.health#AffectedEntitiesForOrganizationTagFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.affected_entities_for_organization_tag_value_list
    import capo_health.types.tag_filter_key

AffectedEntitiesForOrganizationTagFilter: TypeAlias = dict[
    "capo_health.types.tag_filter_key.TagFilterKey",
    "capo_health.types.affected_entities_for_organization_tag_value_list.AffectedEntitiesForOrganizationTagValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: AffectedEntitiesForOrganizationTagFilter,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_health.types.affected_entities_for_organization_tag_value_list

        out[key] = (
            capo_health.types.affected_entities_for_organization_tag_value_list.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AffectedEntitiesForOrganizationTagFilter:
    out: AffectedEntitiesForOrganizationTagFilter = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_health.types.affected_entities_for_organization_tag_value_list

        out[key] = (
            capo_health.types.affected_entities_for_organization_tag_value_list.deserialize_aws_json_1_1(
                value
            )
        )
    return out
