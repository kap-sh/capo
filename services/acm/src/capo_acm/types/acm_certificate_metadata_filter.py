"""Generated from Smithy shape ``com.amazonaws.acm#AcmCertificateMetadataFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.acme_account_id
    import capo_acm.types.arn
    import capo_acm.types.certificate_export
    import capo_acm.types.certificate_key_pair_origin
    import capo_acm.types.certificate_managed_by
    import capo_acm.types.certificate_status
    import capo_acm.types.certificate_type
    import capo_acm.types.nullable_boolean
    import capo_acm.types.renewal_status
    import capo_acm.types.validation_method


class AcmCertificateMetadataFilterStatusMember(TypedDict, closed=True):
    Status: "capo_acm.types.certificate_status.CertificateStatus"


class AcmCertificateMetadataFilterRenewalStatusMember(TypedDict, closed=True):
    RenewalStatus: "capo_acm.types.renewal_status.RenewalStatus"


class AcmCertificateMetadataFilterTypeMember(TypedDict, closed=True):
    Type: "capo_acm.types.certificate_type.CertificateType"


class AcmCertificateMetadataFilterInUseMember(TypedDict, closed=True):
    InUse: "capo_acm.types.nullable_boolean.NullableBoolean"


class AcmCertificateMetadataFilterExportedMember(TypedDict, closed=True):
    Exported: "capo_acm.types.nullable_boolean.NullableBoolean"


class AcmCertificateMetadataFilterExportOptionMember(TypedDict, closed=True):
    ExportOption: "capo_acm.types.certificate_export.CertificateExport"


class AcmCertificateMetadataFilterManagedByMember(TypedDict, closed=True):
    ManagedBy: "capo_acm.types.certificate_managed_by.CertificateManagedBy"


class AcmCertificateMetadataFilterValidationMethodMember(TypedDict, closed=True):
    ValidationMethod: "capo_acm.types.validation_method.ValidationMethod"


class AcmCertificateMetadataFilterCertificateKeyPairOriginMember(
    TypedDict, closed=True
):
    CertificateKeyPairOrigin: (
        "capo_acm.types.certificate_key_pair_origin.CertificateKeyPairOrigin"
    )


class AcmCertificateMetadataFilterAcmeEndpointArnMember(TypedDict, closed=True):
    AcmeEndpointArn: "capo_acm.types.arn.Arn"


class AcmCertificateMetadataFilterAcmeAccountIdMember(TypedDict, closed=True):
    AcmeAccountId: "capo_acm.types.acme_account_id.AcmeAccountId"


AcmCertificateMetadataFilter: TypeAlias = (
    AcmCertificateMetadataFilterStatusMember
    | AcmCertificateMetadataFilterRenewalStatusMember
    | AcmCertificateMetadataFilterTypeMember
    | AcmCertificateMetadataFilterInUseMember
    | AcmCertificateMetadataFilterExportedMember
    | AcmCertificateMetadataFilterExportOptionMember
    | AcmCertificateMetadataFilterManagedByMember
    | AcmCertificateMetadataFilterValidationMethodMember
    | AcmCertificateMetadataFilterCertificateKeyPairOriginMember
    | AcmCertificateMetadataFilterAcmeEndpointArnMember
    | AcmCertificateMetadataFilterAcmeAccountIdMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmCertificateMetadataFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AcmCertificateMetadataFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Status" in value:
        import capo_acm.types.certificate_status

        return {
            "Status": capo_acm.types.certificate_status.serialize_aws_json_1_1(
                value["Status"]
            )
        }
    elif "RenewalStatus" in value:
        import capo_acm.types.renewal_status

        return {
            "RenewalStatus": capo_acm.types.renewal_status.serialize_aws_json_1_1(
                value["RenewalStatus"]
            )
        }
    elif "Type" in value:
        import capo_acm.types.certificate_type

        return {
            "Type": capo_acm.types.certificate_type.serialize_aws_json_1_1(
                value["Type"]
            )
        }
    elif "InUse" in value:
        return {"InUse": value["InUse"]}
    elif "Exported" in value:
        return {"Exported": value["Exported"]}
    elif "ExportOption" in value:
        import capo_acm.types.certificate_export

        return {
            "ExportOption": capo_acm.types.certificate_export.serialize_aws_json_1_1(
                value["ExportOption"]
            )
        }
    elif "ManagedBy" in value:
        import capo_acm.types.certificate_managed_by

        return {
            "ManagedBy": capo_acm.types.certificate_managed_by.serialize_aws_json_1_1(
                value["ManagedBy"]
            )
        }
    elif "ValidationMethod" in value:
        import capo_acm.types.validation_method

        return {
            "ValidationMethod": capo_acm.types.validation_method.serialize_aws_json_1_1(
                value["ValidationMethod"]
            )
        }
    elif "CertificateKeyPairOrigin" in value:
        import capo_acm.types.certificate_key_pair_origin

        return {
            "CertificateKeyPairOrigin": capo_acm.types.certificate_key_pair_origin.serialize_aws_json_1_1(
                value["CertificateKeyPairOrigin"]
            )
        }
    elif "AcmeEndpointArn" in value:
        return {"AcmeEndpointArn": value["AcmeEndpointArn"]}
    elif "AcmeAccountId" in value:
        return {"AcmeAccountId": value["AcmeAccountId"]}
    else:
        raise SerializationError("AcmCertificateMetadataFilter: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AcmCertificateMetadataFilter:
    if data.get("Status") is not None:
        import capo_acm.types.certificate_status

        return {
            "Status": capo_acm.types.certificate_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        }
    elif data.get("RenewalStatus") is not None:
        import capo_acm.types.renewal_status

        return {
            "RenewalStatus": capo_acm.types.renewal_status.deserialize_aws_json_1_1(
                data["RenewalStatus"]
            )
        }
    elif data.get("Type") is not None:
        import capo_acm.types.certificate_type

        return {
            "Type": capo_acm.types.certificate_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        }
    elif data.get("InUse") is not None:
        return {"InUse": data["InUse"]}
    elif data.get("Exported") is not None:
        return {"Exported": data["Exported"]}
    elif data.get("ExportOption") is not None:
        import capo_acm.types.certificate_export

        return {
            "ExportOption": capo_acm.types.certificate_export.deserialize_aws_json_1_1(
                data["ExportOption"]
            )
        }
    elif data.get("ManagedBy") is not None:
        import capo_acm.types.certificate_managed_by

        return {
            "ManagedBy": capo_acm.types.certificate_managed_by.deserialize_aws_json_1_1(
                data["ManagedBy"]
            )
        }
    elif data.get("ValidationMethod") is not None:
        import capo_acm.types.validation_method

        return {
            "ValidationMethod": capo_acm.types.validation_method.deserialize_aws_json_1_1(
                data["ValidationMethod"]
            )
        }
    elif data.get("CertificateKeyPairOrigin") is not None:
        import capo_acm.types.certificate_key_pair_origin

        return {
            "CertificateKeyPairOrigin": capo_acm.types.certificate_key_pair_origin.deserialize_aws_json_1_1(
                data["CertificateKeyPairOrigin"]
            )
        }
    elif data.get("AcmeEndpointArn") is not None:
        return {"AcmeEndpointArn": data["AcmeEndpointArn"]}
    elif data.get("AcmeAccountId") is not None:
        return {"AcmeAccountId": data["AcmeAccountId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AcmCertificateMetadataFilter: no recognized variant key"
        )
