"""Generated from Smithy shape ``com.amazonaws.acm#CertificateMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.acm_certificate_metadata


class _CertificateMetadata_AcmCertificateMetadata(TypedDict, closed=True):
    AcmCertificateMetadata: (
        "capo_acm.types.acm_certificate_metadata.AcmCertificateMetadata"
    )


CertificateMetadata: TypeAlias = (
    _CertificateMetadata_AcmCertificateMetadata | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CertificateMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AcmCertificateMetadata" in value:
        import capo_acm.types.acm_certificate_metadata

        return {
            "AcmCertificateMetadata": capo_acm.types.acm_certificate_metadata.serialize_aws_json_1_1(
                value["AcmCertificateMetadata"]
            )
        }
    else:
        raise SerializationError("CertificateMetadata: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CertificateMetadata:
    if data.get("AcmCertificateMetadata") is not None:
        import capo_acm.types.acm_certificate_metadata

        return {
            "AcmCertificateMetadata": capo_acm.types.acm_certificate_metadata.deserialize_aws_json_1_1(
                data["AcmCertificateMetadata"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CertificateMetadata: no recognized variant key")
