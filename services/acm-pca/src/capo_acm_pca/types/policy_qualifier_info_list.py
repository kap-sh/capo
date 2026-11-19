"""Generated from Smithy shape ``com.amazonaws.acmpca#PolicyQualifierInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm_pca.types.policy_qualifier_info

PolicyQualifierInfoList: TypeAlias = list[
    "capo_acm_pca.types.policy_qualifier_info.PolicyQualifierInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyQualifierInfoList) -> list:
    import capo_acm_pca.types.policy_qualifier_info

    out: list = []
    for item in value:
        out.append(
            capo_acm_pca.types.policy_qualifier_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PolicyQualifierInfoList:
    import capo_acm_pca.types.policy_qualifier_info

    out: PolicyQualifierInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_acm_pca.types.policy_qualifier_info.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyQualifierInfoList) -> list:
    import capo_acm_pca.types.policy_qualifier_info

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.policy_qualifier_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PolicyQualifierInfoList:
    import capo_acm_pca.types.policy_qualifier_info

    out: PolicyQualifierInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.policy_qualifier_info.deserialize_cbor(item))
    return out
