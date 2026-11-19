"""Generated from Smithy shape ``com.amazonaws.directoryservice#DomainControllerIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.domain_controller_id

DomainControllerIds: TypeAlias = list[
    "capo_directory_service.types.domain_controller_id.DomainControllerId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainControllerIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DomainControllerIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainControllerIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DomainControllerIds:
    return [item for item in data if item is not None]
