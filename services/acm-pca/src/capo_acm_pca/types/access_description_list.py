"""Generated from Smithy shape ``com.amazonaws.acmpca#AccessDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm_pca.types.access_description

AccessDescriptionList: TypeAlias = list[
    "capo_acm_pca.types.access_description.AccessDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDescriptionList) -> list:
    import capo_acm_pca.types.access_description

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.access_description.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AccessDescriptionList:
    import capo_acm_pca.types.access_description

    out: AccessDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.access_description.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessDescriptionList) -> list:
    import capo_acm_pca.types.access_description

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.access_description.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AccessDescriptionList:
    import capo_acm_pca.types.access_description

    out: AccessDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.access_description.deserialize_cbor(item))
    return out
