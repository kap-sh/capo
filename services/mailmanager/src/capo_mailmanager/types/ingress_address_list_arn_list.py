"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressAddressListArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.address_list_arn

IngressAddressListArnList: TypeAlias = list[
    "capo_mailmanager.types.address_list_arn.AddressListArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressAddressListArnList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> IngressAddressListArnList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressAddressListArnList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> IngressAddressListArnList:
    return [item for item in data if item is not None]
