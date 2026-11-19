"""Generated from Smithy shape ``com.amazonaws.directoryservice#Trusts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.trust

Trusts: TypeAlias = list["capo_directory_service.types.trust.Trust"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Trusts) -> list:
    import capo_directory_service.types.trust

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.trust.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Trusts:
    import capo_directory_service.types.trust

    out: Trusts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.trust.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Trusts) -> list:
    import capo_directory_service.types.trust

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.trust.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Trusts:
    import capo_directory_service.types.trust

    out: Trusts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.trust.deserialize_cbor(item))
    return out
