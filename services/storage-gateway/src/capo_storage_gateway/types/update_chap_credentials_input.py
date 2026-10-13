"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateChapCredentialsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.chap_secret
    import capo_storage_gateway.types.iqn_name
    import capo_storage_gateway.types.target_arn


class UpdateChapCredentialsInput(TypedDict, closed=True):
    target_arn: "capo_storage_gateway.types.target_arn.TargetARN"
    """<p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return the TargetARN for specified VolumeARN.</p>"""
    secret_to_authenticate_initiator: (
        "capo_storage_gateway.types.chap_secret.ChapSecret"
    )
    """<p>The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.</p> <note> <p>The secret key must be between 12 and 16 bytes when encoded in UTF-8.</p> </note>"""
    initiator_name: "capo_storage_gateway.types.iqn_name.IqnName"
    """<p>The iSCSI initiator that connects to the target.</p>"""
    secret_to_authenticate_target: NotRequired[
        "capo_storage_gateway.types.chap_secret.ChapSecret"
    ]
    """<p>The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).</p> <p>Byte constraints: Minimum bytes of 12. Maximum bytes of 16.</p> <note> <p>The secret key must be between 12 and 16 bytes when encoded in UTF-8.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateChapCredentialsInput) -> dict:
    out: dict = {}
    out["TargetARN"] = value["target_arn"]
    out["SecretToAuthenticateInitiator"] = value["secret_to_authenticate_initiator"]
    out["InitiatorName"] = value["initiator_name"]
    if "secret_to_authenticate_target" in value:
        out["SecretToAuthenticateTarget"] = value["secret_to_authenticate_target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateChapCredentialsInput:
    out: UpdateChapCredentialsInput = {}  # type: ignore[typeddict-item]
    if data.get("TargetARN") is not None:
        out["target_arn"] = data["TargetARN"]
    else:
        raise DeserializationError("UpdateChapCredentialsInput.target_arn required")
    if data.get("SecretToAuthenticateInitiator") is not None:
        out["secret_to_authenticate_initiator"] = data["SecretToAuthenticateInitiator"]
    else:
        raise DeserializationError(
            "UpdateChapCredentialsInput.secret_to_authenticate_initiator required"
        )
    if data.get("InitiatorName") is not None:
        out["initiator_name"] = data["InitiatorName"]
    else:
        raise DeserializationError("UpdateChapCredentialsInput.initiator_name required")
    if data.get("SecretToAuthenticateTarget") is not None:
        out["secret_to_authenticate_target"] = data["SecretToAuthenticateTarget"]
    return out


def redact_sensitive(value: UpdateChapCredentialsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_to_authenticate_initiator" in value:
        out["secret_to_authenticate_initiator"] = "*** Sensitive Data Redacted ***"
    if "secret_to_authenticate_target" in value:
        out["secret_to_authenticate_target"] = "*** Sensitive Data Redacted ***"
    return out
