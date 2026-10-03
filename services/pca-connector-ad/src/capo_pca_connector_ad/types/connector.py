"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#Connector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pca_connector_ad.types.certificate_authority_arn
    import capo_pca_connector_ad.types.connector_arn
    import capo_pca_connector_ad.types.connector_status
    import capo_pca_connector_ad.types.connector_status_reason
    import capo_pca_connector_ad.types.directory_id
    import capo_pca_connector_ad.types.vpc_information


class Connector(TypedDict, closed=True):
    arn: NotRequired["capo_pca_connector_ad.types.connector_arn.ConnectorArn"]
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>. </p>"""
    certificate_authority_arn: NotRequired[
        "capo_pca_connector_ad.types.certificate_authority_arn.CertificateAuthorityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate authority being used. </p>"""
    certificate_enrollment_policy_server_endpoint: NotRequired["str"]
    """<p>Certificate enrollment endpoint for Active Directory domain-joined objects reach out to when requesting certificates.</p>"""
    directory_id: NotRequired["capo_pca_connector_ad.types.directory_id.DirectoryId"]
    """<p>The identifier of the Active Directory.</p>"""
    vpc_information: NotRequired[
        "capo_pca_connector_ad.types.vpc_information.VpcInformation"
    ]
    """<p>Information of the VPC and security group(s) used with the connector.</p>"""
    status: NotRequired["capo_pca_connector_ad.types.connector_status.ConnectorStatus"]
    """<p>Status of the connector. Status can be creating, active, deleting, or failed.</p>"""
    status_reason: NotRequired[
        "capo_pca_connector_ad.types.connector_status_reason.ConnectorStatusReason"
    ]
    """<p>Additional information about the connector status if the status is failed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the connector was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the connector was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Connector) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "certificate_enrollment_policy_server_endpoint" in value:
        out["CertificateEnrollmentPolicyServerEndpoint"] = value[
            "certificate_enrollment_policy_server_endpoint"
        ]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "vpc_information" in value:
        import capo_pca_connector_ad.types.vpc_information

        out["VpcInformation"] = (
            capo_pca_connector_ad.types.vpc_information.serialize_json(
                value["vpc_information"]
            )
        )
    if "status" in value:
        import capo_pca_connector_ad.types.connector_status

        out["Status"] = capo_pca_connector_ad.types.connector_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        import capo_pca_connector_ad.types.connector_status_reason

        out["StatusReason"] = (
            capo_pca_connector_ad.types.connector_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "created_at" in value:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["CreatedAt"] = (
            capo_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["UpdatedAt"] = (
            capo_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> Connector:
    out: Connector = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if data.get("CertificateEnrollmentPolicyServerEndpoint") is not None:
        out["certificate_enrollment_policy_server_endpoint"] = data[
            "CertificateEnrollmentPolicyServerEndpoint"
        ]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("VpcInformation") is not None:
        import capo_pca_connector_ad.types.vpc_information

        out["vpc_information"] = (
            capo_pca_connector_ad.types.vpc_information.deserialize_json(
                data["VpcInformation"]
            )
        )
    if data.get("Status") is not None:
        import capo_pca_connector_ad.types.connector_status

        out["status"] = capo_pca_connector_ad.types.connector_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusReason") is not None:
        import capo_pca_connector_ad.types.connector_status_reason

        out["status_reason"] = (
            capo_pca_connector_ad.types.connector_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["created_at"] = (
            capo_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["updated_at"] = (
            capo_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out
