"""Generated from Smithy shape ``com.amazonaws.acmpca#GeneralNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm_pca.types.general_name

GeneralNameList: TypeAlias = list["capo_acm_pca.types.general_name.GeneralName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeneralNameList) -> list:
    import capo_acm_pca.types.general_name

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.general_name.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GeneralNameList:
    import capo_acm_pca.types.general_name

    out: GeneralNameList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.general_name.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GeneralNameList) -> list:
    import capo_acm_pca.types.general_name

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.general_name.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> GeneralNameList:
    import capo_acm_pca.types.general_name

    out: GeneralNameList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.general_name.deserialize_cbor(item))
    return out
