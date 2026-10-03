"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ServicePrincipalNameSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pca_connector_ad.types.connector_arn
    import capo_pca_connector_ad.types.directory_registration_arn
    import capo_pca_connector_ad.types.service_principal_name_status
    import capo_pca_connector_ad.types.service_principal_name_status_reason


class ServicePrincipalNameSummary(TypedDict, closed=True):
    directory_registration_arn: NotRequired[
        "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>"""
    connector_arn: NotRequired["capo_pca_connector_ad.types.connector_arn.ConnectorArn"]
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>"""
    status: NotRequired[
        "capo_pca_connector_ad.types.service_principal_name_status.ServicePrincipalNameStatus"
    ]
    """<p>The status of a service principal name.</p>"""
    status_reason: NotRequired[
        "capo_pca_connector_ad.types.service_principal_name_status_reason.ServicePrincipalNameStatusReason"
    ]
    """<p>Additional information for the status of a service principal name if the status is failed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the service principal name was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>Time when the service principal name was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServicePrincipalNameSummary) -> dict:
    out: dict = {}
    if "directory_registration_arn" in value:
        out["DirectoryRegistrationArn"] = value["directory_registration_arn"]
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "status" in value:
        import capo_pca_connector_ad.types.service_principal_name_status

        out["Status"] = (
            capo_pca_connector_ad.types.service_principal_name_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        import capo_pca_connector_ad.types.service_principal_name_status_reason

        out["StatusReason"] = (
            capo_pca_connector_ad.types.service_principal_name_status_reason.serialize_json(
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


def deserialize_json(data: dict) -> ServicePrincipalNameSummary:
    out: ServicePrincipalNameSummary = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryRegistrationArn") is not None:
        out["directory_registration_arn"] = data["DirectoryRegistrationArn"]
    if data.get("ConnectorArn") is not None:
        out["connector_arn"] = data["ConnectorArn"]
    if data.get("Status") is not None:
        import capo_pca_connector_ad.types.service_principal_name_status

        out["status"] = (
            capo_pca_connector_ad.types.service_principal_name_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        import capo_pca_connector_ad.types.service_principal_name_status_reason

        out["status_reason"] = (
            capo_pca_connector_ad.types.service_principal_name_status_reason.deserialize_json(
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
