"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEntityAccountFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.entity_account_filter

OrganizationEntityAccountFiltersList: TypeAlias = list[
    "capo_health.types.entity_account_filter.EntityAccountFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEntityAccountFiltersList) -> list:
    import capo_health.types.entity_account_filter

    out: list = []
    for item in value:
        out.append(capo_health.types.entity_account_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationEntityAccountFiltersList:
    import capo_health.types.entity_account_filter

    out: OrganizationEntityAccountFiltersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.entity_account_filter.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationEntityAccountFiltersList) -> list:
    import capo_health.types.entity_account_filter

    out: list = []
    for item in value:
        out.append(capo_health.types.entity_account_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OrganizationEntityAccountFiltersList:
    import capo_health.types.entity_account_filter

    out: OrganizationEntityAccountFiltersList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.entity_account_filter.deserialize_cbor(item))
    return out
