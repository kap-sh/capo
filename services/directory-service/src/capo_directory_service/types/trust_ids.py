"""Generated from Smithy shape ``com.amazonaws.directoryservice#TrustIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.trust_id

TrustIds: TypeAlias = list["capo_directory_service.types.trust_id.TrustId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TrustIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TrustIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TrustIds:
    return [item for item in data if item is not None]
