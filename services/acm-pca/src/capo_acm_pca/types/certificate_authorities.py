"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm_pca.types.certificate_authority

CertificateAuthorities: TypeAlias = list[
    "capo_acm_pca.types.certificate_authority.CertificateAuthority"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthorities) -> list:
    import capo_acm_pca.types.certificate_authority

    out: list = []
    for item in value:
        out.append(
            capo_acm_pca.types.certificate_authority.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateAuthorities:
    import capo_acm_pca.types.certificate_authority

    out: CertificateAuthorities = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_acm_pca.types.certificate_authority.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateAuthorities) -> list:
    import capo_acm_pca.types.certificate_authority

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.certificate_authority.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> CertificateAuthorities:
    import capo_acm_pca.types.certificate_authority

    out: CertificateAuthorities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm_pca.types.certificate_authority.deserialize_cbor(item))
    return out
