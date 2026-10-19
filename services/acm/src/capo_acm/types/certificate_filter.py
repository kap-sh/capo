"""Generated from Smithy shape ``com.amazonaws.acm#CertificateFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.acm_certificate_metadata_filter
    import capo_acm.types.arn
    import capo_acm.types.x509_attribute_filter


class _CertificateFilter_CertificateArn(TypedDict, closed=True):
    CertificateArn: "capo_acm.types.arn.Arn"


class _CertificateFilter_X509AttributeFilter(TypedDict, closed=True):
    X509AttributeFilter: "capo_acm.types.x509_attribute_filter.X509AttributeFilter"


class _CertificateFilter_AcmCertificateMetadataFilter(TypedDict, closed=True):
    AcmCertificateMetadataFilter: (
        "capo_acm.types.acm_certificate_metadata_filter.AcmCertificateMetadataFilter"
    )


CertificateFilter: TypeAlias = (
    _CertificateFilter_CertificateArn
    | _CertificateFilter_X509AttributeFilter
    | _CertificateFilter_AcmCertificateMetadataFilter
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CertificateFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "CertificateArn" in value:
        return {"CertificateArn": value["CertificateArn"]}
    elif "X509AttributeFilter" in value:
        import capo_acm.types.x509_attribute_filter

        return {
            "X509AttributeFilter": capo_acm.types.x509_attribute_filter.serialize_aws_json_1_1(
                value["X509AttributeFilter"]
            )
        }
    elif "AcmCertificateMetadataFilter" in value:
        import capo_acm.types.acm_certificate_metadata_filter

        return {
            "AcmCertificateMetadataFilter": capo_acm.types.acm_certificate_metadata_filter.serialize_aws_json_1_1(
                value["AcmCertificateMetadataFilter"]
            )
        }
    else:
        raise SerializationError("CertificateFilter: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CertificateFilter:
    if data.get("CertificateArn") is not None:
        return {"CertificateArn": data["CertificateArn"]}
    elif data.get("X509AttributeFilter") is not None:
        import capo_acm.types.x509_attribute_filter

        return {
            "X509AttributeFilter": capo_acm.types.x509_attribute_filter.deserialize_aws_json_1_1(
                data["X509AttributeFilter"]
            )
        }
    elif data.get("AcmCertificateMetadataFilter") is not None:
        import capo_acm.types.acm_certificate_metadata_filter

        return {
            "AcmCertificateMetadataFilter": capo_acm.types.acm_certificate_metadata_filter.deserialize_aws_json_1_1(
                data["AcmCertificateMetadataFilter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CertificateFilter: no recognized variant key")
