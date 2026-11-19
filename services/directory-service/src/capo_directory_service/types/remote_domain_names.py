"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoteDomainNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.remote_domain_name

RemoteDomainNames: TypeAlias = list[
    "capo_directory_service.types.remote_domain_name.RemoteDomainName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteDomainNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RemoteDomainNames:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RemoteDomainNames) -> list:
    return list(value)


def deserialize_cbor(data: list) -> RemoteDomainNames:
    return [item for item in data if item is not None]
