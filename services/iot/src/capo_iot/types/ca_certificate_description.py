"""Generated from Smithy shape ``com.amazonaws.iot#CACertificateDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.auto_registration_status
    import capo_iot.types.aws_account_id
    import capo_iot.types.ca_certificate_status
    import capo_iot.types.certificate_arn
    import capo_iot.types.certificate_id
    import capo_iot.types.certificate_mode
    import capo_iot.types.certificate_pem
    import capo_iot.types.certificate_validity
    import capo_iot.types.customer_version
    import capo_iot.types.date_type
    import capo_iot.types.generation_id


class CACertificateDescription(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_iot.types.certificate_arn.CertificateArn"]
    """<p>The CA certificate ARN.</p>"""
    certificate_id: NotRequired["capo_iot.types.certificate_id.CertificateId"]
    """<p>The CA certificate ID.</p>"""
    status: NotRequired["capo_iot.types.ca_certificate_status.CACertificateStatus"]
    """<p>The status of a CA certificate.</p>"""
    certificate_pem: NotRequired["capo_iot.types.certificate_pem.CertificatePem"]
    """<p>The CA certificate data, in PEM format.</p>"""
    owned_by: NotRequired["capo_iot.types.aws_account_id.AwsAccountId"]
    """<p>The owner of the CA certificate.</p>"""
    creation_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the CA certificate was created.</p>"""
    auto_registration_status: NotRequired[
        "capo_iot.types.auto_registration_status.AutoRegistrationStatus"
    ]
    """<p>Whether the CA certificate configured for auto registration of device certificates. Valid values are "ENABLE" and "DISABLE"</p>"""
    last_modified_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the CA certificate was last modified.</p>"""
    customer_version: NotRequired["capo_iot.types.customer_version.CustomerVersion"]
    """<p>The customer version of the CA certificate.</p>"""
    generation_id: NotRequired["capo_iot.types.generation_id.GenerationId"]
    """<p>The generation ID of the CA certificate.</p>"""
    validity: NotRequired["capo_iot.types.certificate_validity.CertificateValidity"]
    """<p>When the CA certificate is valid.</p>"""
    certificate_mode: NotRequired["capo_iot.types.certificate_mode.CertificateMode"]
    """<p>The mode of the CA. </p> <p>All the device certificates that are registered using this CA will be registered in the same mode as the CA. For more information about certificate mode for device certificates, see <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_CertificateDescription.html#iot-Type-CertificateDescription-certificateMode">certificate mode</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CACertificateDescription) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    if "status" in value:
        import capo_iot.types.ca_certificate_status

        out["status"] = capo_iot.types.ca_certificate_status.serialize_json(
            value["status"]
        )
    if "certificate_pem" in value:
        out["certificatePem"] = value["certificate_pem"]
    if "owned_by" in value:
        out["ownedBy"] = value["owned_by"]
    if "creation_date" in value:
        import capo_iot.types.date_type

        out["creationDate"] = capo_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    if "auto_registration_status" in value:
        import capo_iot.types.auto_registration_status

        out["autoRegistrationStatus"] = (
            capo_iot.types.auto_registration_status.serialize_json(
                value["auto_registration_status"]
            )
        )
    if "last_modified_date" in value:
        import capo_iot.types.date_type

        out["lastModifiedDate"] = capo_iot.types.date_type.serialize_json(
            value["last_modified_date"]
        )
    if "customer_version" in value:
        out["customerVersion"] = value["customer_version"]
    if "generation_id" in value:
        out["generationId"] = value["generation_id"]
    if "validity" in value:
        import capo_iot.types.certificate_validity

        out["validity"] = capo_iot.types.certificate_validity.serialize_json(
            value["validity"]
        )
    if "certificate_mode" in value:
        import capo_iot.types.certificate_mode

        out["certificateMode"] = capo_iot.types.certificate_mode.serialize_json(
            value["certificate_mode"]
        )
    return out


def deserialize_json(data: dict) -> CACertificateDescription:
    out: CACertificateDescription = {}  # type: ignore[typeddict-item]
    if data.get("certificateArn") is not None:
        out["certificate_arn"] = data["certificateArn"]
    if data.get("certificateId") is not None:
        out["certificate_id"] = data["certificateId"]
    if data.get("status") is not None:
        import capo_iot.types.ca_certificate_status

        out["status"] = capo_iot.types.ca_certificate_status.deserialize_json(
            data["status"]
        )
    if data.get("certificatePem") is not None:
        out["certificate_pem"] = data["certificatePem"]
    if data.get("ownedBy") is not None:
        out["owned_by"] = data["ownedBy"]
    if data.get("creationDate") is not None:
        import capo_iot.types.date_type

        out["creation_date"] = capo_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    if data.get("autoRegistrationStatus") is not None:
        import capo_iot.types.auto_registration_status

        out["auto_registration_status"] = (
            capo_iot.types.auto_registration_status.deserialize_json(
                data["autoRegistrationStatus"]
            )
        )
    if data.get("lastModifiedDate") is not None:
        import capo_iot.types.date_type

        out["last_modified_date"] = capo_iot.types.date_type.deserialize_json(
            data["lastModifiedDate"]
        )
    if data.get("customerVersion") is not None:
        out["customer_version"] = data["customerVersion"]
    if data.get("generationId") is not None:
        out["generation_id"] = data["generationId"]
    if data.get("validity") is not None:
        import capo_iot.types.certificate_validity

        out["validity"] = capo_iot.types.certificate_validity.deserialize_json(
            data["validity"]
        )
    if data.get("certificateMode") is not None:
        import capo_iot.types.certificate_mode

        out["certificate_mode"] = capo_iot.types.certificate_mode.deserialize_json(
            data["certificateMode"]
        )
    return out
