"""Generated from Smithy shape ``com.amazonaws.secretsmanager#UpdateSecretVersionStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_id_type
    import capo_secrets_manager.types.secret_version_id_type
    import capo_secrets_manager.types.secret_version_stage_type


class UpdateSecretVersionStageRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or the name of the secret with the version and staging labelsto modify.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    version_stage: (
        "capo_secrets_manager.types.secret_version_stage_type.SecretVersionStageType"
    )
    """<p>The staging label to add to this version.</p>"""
    remove_from_version_id: NotRequired[
        "capo_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The ID of the version that the staging label is to be removed from. If the staging label you are trying to attach to one version is already attached to a different version, then you must include this parameter and specify the version that the label is to be removed from. If the label is attached and you either do not specify this parameter, or the version ID does not match, then the operation fails.</p>"""
    move_to_version_id: NotRequired[
        "capo_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The ID of the version to add the staging label to. To remove a label from a version, then do not specify this parameter.</p> <p>If the staging label is already attached to a different version of the secret, then you must also specify the <code>RemoveFromVersionId</code> parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSecretVersionStageRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    out["VersionStage"] = value["version_stage"]
    if "remove_from_version_id" in value:
        out["RemoveFromVersionId"] = value["remove_from_version_id"]
    if "move_to_version_id" in value:
        out["MoveToVersionId"] = value["move_to_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSecretVersionStageRequest:
    out: UpdateSecretVersionStageRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("UpdateSecretVersionStageRequest.secret_id required")
    if data.get("VersionStage") is not None:
        out["version_stage"] = data["VersionStage"]
    else:
        raise DeserializationError(
            "UpdateSecretVersionStageRequest.version_stage required"
        )
    if data.get("RemoveFromVersionId") is not None:
        out["remove_from_version_id"] = data["RemoveFromVersionId"]
    if data.get("MoveToVersionId") is not None:
        out["move_to_version_id"] = data["MoveToVersionId"]
    return out
