"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetEncryptionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.encryption_status
    import capo_iotfleetwise.types.encryption_type
    import capo_iotfleetwise.types.error_message
    import capo_iotfleetwise.types.timestamp


class GetEncryptionConfigurationResponse(TypedDict, closed=True):
    kms_key_id: NotRequired["str"]
    """<p>The ID of the KMS key that is used for encryption.</p>"""
    encryption_status: "capo_iotfleetwise.types.encryption_status.EncryptionStatus"
    """<p>The encryption status.</p>"""
    encryption_type: "capo_iotfleetwise.types.encryption_type.EncryptionType"
    """<p>The type of encryption. Set to <code>KMS_BASED_ENCRYPTION</code> to use a KMS key that you own and manage. Set to <code>FLEETWISE_DEFAULT_ENCRYPTION</code> to use an Amazon Web Services managed key that is owned by the Amazon Web Services IoT FleetWise service account.</p>"""
    error_message: NotRequired["capo_iotfleetwise.types.error_message.errorMessage"]
    """<p>The error message that describes why encryption settings couldn't be configured, if applicable.</p>"""
    creation_time: NotRequired["capo_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time when encryption was configured in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: NotRequired["capo_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time when encryption was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEncryptionConfigurationResponse) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    import capo_iotfleetwise.types.encryption_status

    out["encryptionStatus"] = (
        capo_iotfleetwise.types.encryption_status.serialize_aws_json_1_0(
            value["encryption_status"]
        )
    )
    import capo_iotfleetwise.types.encryption_type

    out["encryptionType"] = (
        capo_iotfleetwise.types.encryption_type.serialize_aws_json_1_0(
            value["encryption_type"]
        )
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "creation_time" in value:
        import capo_iotfleetwise.types.timestamp

        out["creationTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import capo_iotfleetwise.types.timestamp

        out["lastModificationTime"] = (
            capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["last_modification_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEncryptionConfigurationResponse:
    out: GetEncryptionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("encryptionStatus") is not None:
        import capo_iotfleetwise.types.encryption_status

        out["encryption_status"] = (
            capo_iotfleetwise.types.encryption_status.deserialize_aws_json_1_0(
                data["encryptionStatus"]
            )
        )
    else:
        import typing

        out["encryption_status"] = typing.cast(
            "capo_iotfleetwise.types.encryption_status.EncryptionStatus", ""
        )
    if data.get("encryptionType") is not None:
        import capo_iotfleetwise.types.encryption_type

        out["encryption_type"] = (
            capo_iotfleetwise.types.encryption_type.deserialize_aws_json_1_0(
                data["encryptionType"]
            )
        )
    else:
        import typing

        out["encryption_type"] = typing.cast(
            "capo_iotfleetwise.types.encryption_type.EncryptionType", ""
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("creationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["creation_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    if data.get("lastModificationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    return out
