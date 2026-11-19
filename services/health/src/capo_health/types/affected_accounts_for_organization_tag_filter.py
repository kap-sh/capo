"""Generated from Smithy shape ``com.amazonaws.health#AffectedAccountsForOrganizationTagFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.affected_accounts_for_organization_tag_value_list
    import capo_health.types.tag_filter_key

AffectedAccountsForOrganizationTagFilter: TypeAlias = dict[
    "capo_health.types.tag_filter_key.TagFilterKey",
    "capo_health.types.affected_accounts_for_organization_tag_value_list.AffectedAccountsForOrganizationTagValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: AffectedAccountsForOrganizationTagFilter,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_health.types.affected_accounts_for_organization_tag_value_list

        out[key] = (
            capo_health.types.affected_accounts_for_organization_tag_value_list.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AffectedAccountsForOrganizationTagFilter:
    out: AffectedAccountsForOrganizationTagFilter = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_health.types.affected_accounts_for_organization_tag_value_list

        out[key] = (
            capo_health.types.affected_accounts_for_organization_tag_value_list.deserialize_aws_json_1_1(
                value
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(
    input_to_serialize: AffectedAccountsForOrganizationTagFilter,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_health.types.affected_accounts_for_organization_tag_value_list

        out[key] = (
            capo_health.types.affected_accounts_for_organization_tag_value_list.serialize_cbor(
                value
            )
        )
    return out


def deserialize_cbor(data: dict) -> AffectedAccountsForOrganizationTagFilter:
    out: AffectedAccountsForOrganizationTagFilter = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_health.types.affected_accounts_for_organization_tag_value_list

        out[key] = (
            capo_health.types.affected_accounts_for_organization_tag_value_list.deserialize_cbor(
                value
            )
        )
    return out
