"""Generated from Smithy shape ``com.amazonaws.health#AffectedAccountsForOrganizationTagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.tag_filter_value

AffectedAccountsForOrganizationTagValueList: TypeAlias = list[
    "capo_health.types.tag_filter_value.TagFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AffectedAccountsForOrganizationTagValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AffectedAccountsForOrganizationTagValueList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AffectedAccountsForOrganizationTagValueList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AffectedAccountsForOrganizationTagValueList:
    return [item for item in data if item is not None]
