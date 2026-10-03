"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetSecretValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_id_type
    import capo_secrets_manager.types.secret_version_id_type
    import capo_secrets_manager.types.secret_version_stage_type


class GetSecretValueRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to retrieve. To retrieve a secret from another account, you must use an ARN.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    version_id: NotRequired[
        "capo_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The unique identifier of the version of the secret to retrieve. If you include both this parameter and <code>VersionStage</code>, the two parameters must refer to the same secret version. If you don't specify either a <code>VersionStage</code> or <code>VersionId</code>, then Secrets Manager returns the <code>AWSCURRENT</code> version.</p> <p>This value is typically a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value with 32 hexadecimal digits.</p>"""
    version_stage: NotRequired[
        "capo_secrets_manager.types.secret_version_stage_type.SecretVersionStageType"
    ]
    """<p>The staging label of the version of the secret to retrieve. </p> <p>Secrets Manager uses staging labels to keep track of different versions during the rotation process. If you include both this parameter and <code>VersionId</code>, the two parameters must refer to the same secret version. If you don't specify either a <code>VersionStage</code> or <code>VersionId</code>, Secrets Manager returns the <code>AWSCURRENT</code> version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSecretValueRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "version_stage" in value:
        out["VersionStage"] = value["version_stage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSecretValueRequest:
    out: GetSecretValueRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("GetSecretValueRequest.secret_id required")
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    if data.get("VersionStage") is not None:
        out["version_stage"] = data["VersionStage"]
    return out
