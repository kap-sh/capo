"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Namespaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.account_id

Namespaces: TypeAlias = list["capo_service_catalog.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Namespaces) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Namespaces:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Namespaces) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Namespaces:
    return [item for item in data if item is not None]
