"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#PutEncryptionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.encryption_status
    import capo_iotfleetwise.types.encryption_type


class PutEncryptionConfigurationResponse(TypedDict, closed=True):
    kms_key_id: NotRequired["str"]
    """<p>The ID of the KMS key that is used for encryption.</p>"""
    encryption_status: "capo_iotfleetwise.types.encryption_status.EncryptionStatus"
    """<p>The encryption status.</p>"""
    encryption_type: "capo_iotfleetwise.types.encryption_type.EncryptionType"
    """<p>The type of encryption. Set to <code>KMS_BASED_ENCRYPTION</code> to use an KMS key that you own and manage. Set to <code>FLEETWISE_DEFAULT_ENCRYPTION</code> to use an Amazon Web Services managed key that is owned by the Amazon Web Services IoT FleetWise service account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutEncryptionConfigurationResponse) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> PutEncryptionConfigurationResponse:
    out: PutEncryptionConfigurationResponse = {}  # type: ignore[typeddict-item]
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
    return out
