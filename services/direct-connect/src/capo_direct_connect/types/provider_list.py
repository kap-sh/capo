"""Generated from Smithy shape ``com.amazonaws.directconnect#ProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.provider_name

ProviderList: TypeAlias = list["capo_direct_connect.types.provider_name.ProviderName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProviderList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProviderList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProviderList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProviderList:
    return [item for item in data if item is not None]
