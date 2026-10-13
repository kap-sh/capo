"""Generated from Smithy shape ``com.amazonaws.storagegateway#ChapInfo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.chap_secret
    import capo_storage_gateway.types.iqn_name
    import capo_storage_gateway.types.target_arn


class ChapInfo(TypedDict, closed=True):
    target_arn: NotRequired["capo_storage_gateway.types.target_arn.TargetARN"]
    """<p>The Amazon Resource Name (ARN) of the volume.</p> <p>Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).</p>"""
    secret_to_authenticate_initiator: NotRequired[
        "capo_storage_gateway.types.chap_secret.ChapSecret"
    ]
    """<p>The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.</p>"""
    initiator_name: NotRequired["capo_storage_gateway.types.iqn_name.IqnName"]
    """<p>The iSCSI initiator that connects to the target.</p>"""
    secret_to_authenticate_target: NotRequired[
        "capo_storage_gateway.types.chap_secret.ChapSecret"
    ]
    """<p>The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g., Windows client).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChapInfo) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetARN"] = value["target_arn"]
    if "secret_to_authenticate_initiator" in value:
        out["SecretToAuthenticateInitiator"] = value["secret_to_authenticate_initiator"]
    if "initiator_name" in value:
        out["InitiatorName"] = value["initiator_name"]
    if "secret_to_authenticate_target" in value:
        out["SecretToAuthenticateTarget"] = value["secret_to_authenticate_target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ChapInfo:
    out: ChapInfo = {}  # type: ignore[typeddict-item]
    if data.get("TargetARN") is not None:
        out["target_arn"] = data["TargetARN"]
    if data.get("SecretToAuthenticateInitiator") is not None:
        out["secret_to_authenticate_initiator"] = data["SecretToAuthenticateInitiator"]
    if data.get("InitiatorName") is not None:
        out["initiator_name"] = data["InitiatorName"]
    if data.get("SecretToAuthenticateTarget") is not None:
        out["secret_to_authenticate_target"] = data["SecretToAuthenticateTarget"]
    return out


def redact_sensitive(value: ChapInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_to_authenticate_initiator" in value:
        out["secret_to_authenticate_initiator"] = "*** Sensitive Data Redacted ***"
    if "secret_to_authenticate_target" in value:
        out["secret_to_authenticate_target"] = "*** Sensitive Data Redacted ***"
    return out
