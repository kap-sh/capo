"""Generated from Smithy shape ``com.amazonaws.directoryservice#CertificatesInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.certificate_info

CertificatesInfo: TypeAlias = list[
    "capo_directory_service.types.certificate_info.CertificateInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificatesInfo) -> list:
    import capo_directory_service.types.certificate_info

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.certificate_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CertificatesInfo:
    import capo_directory_service.types.certificate_info

    out: CertificatesInfo = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.certificate_info.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificatesInfo) -> list:
    import capo_directory_service.types.certificate_info

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.certificate_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> CertificatesInfo:
    import capo_directory_service.types.certificate_info

    out: CertificatesInfo = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.certificate_info.deserialize_cbor(item))
    return out
