"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#DirectoryRegistrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pca_connector_ad.types.directory_id
    import capo_pca_connector_ad.types.directory_registration_arn
    import capo_pca_connector_ad.types.directory_registration_status
    import capo_pca_connector_ad.types.directory_registration_status_reason


class DirectoryRegistrationSummary(TypedDict, closed=True):
    arn: NotRequired[
        "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>"""
    directory_id: NotRequired["capo_pca_connector_ad.types.directory_id.DirectoryId"]
    """<p>The identifier of the Active Directory.</p>"""
    status: NotRequired[
        "capo_pca_connector_ad.types.directory_registration_status.DirectoryRegistrationStatus"
    ]
    """<p>Status of the directory registration.</p>"""
    status_reason: NotRequired[
        "capo_pca_connector_ad.types.directory_registration_status_reason.DirectoryRegistrationStatusReason"
    ]
    """<p>Additional information about the directory registration status if the status is failed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the directory registration was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the directory registration was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryRegistrationSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "status" in value:
        import capo_pca_connector_ad.types.directory_registration_status

        out["Status"] = (
            capo_pca_connector_ad.types.directory_registration_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        import capo_pca_connector_ad.types.directory_registration_status_reason

        out["StatusReason"] = (
            capo_pca_connector_ad.types.directory_registration_status_reason.serialize_json(
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


def deserialize_json(data: dict) -> DirectoryRegistrationSummary:
    out: DirectoryRegistrationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Status") is not None:
        import capo_pca_connector_ad.types.directory_registration_status

        out["status"] = (
            capo_pca_connector_ad.types.directory_registration_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        import capo_pca_connector_ad.types.directory_registration_status_reason

        out["status_reason"] = (
            capo_pca_connector_ad.types.directory_registration_status_reason.deserialize_json(
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
