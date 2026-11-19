"""Generated from Smithy shape ``com.amazonaws.acmpca#ExtendedKeyUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm_pca.types.extended_key_usage

ExtendedKeyUsageList: TypeAlias = list[
    "capo_acm_pca.types.extended_key_usage.ExtendedKeyUsage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendedKeyUsageList) -> list:
    import capo_acm_pca.types.extended_key_usage

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.extended_key_usage.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExtendedKeyUsageList:
    import capo_acm_pca.types.extended_key_usage

    out: ExtendedKeyUsageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.extended_key_usage.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExtendedKeyUsageList) -> list:
    import capo_acm_pca.types.extended_key_usage

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.extended_key_usage.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ExtendedKeyUsageList:
    import capo_acm_pca.types.extended_key_usage

    out: ExtendedKeyUsageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.extended_key_usage.deserialize_cbor(item))
    return out
