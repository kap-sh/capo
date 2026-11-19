"""Generated from Smithy shape ``com.amazonaws.appstream#DomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.domain

DomainList: TypeAlias = list["capo_appstream.types.domain.Domain"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DomainList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DomainList:
    return [item for item in data if item is not None]
