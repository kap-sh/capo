"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PutSecretValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.client_request_token_type
    import capo_secrets_manager.types.rotation_token_type
    import capo_secrets_manager.types.secret_binary_type
    import capo_secrets_manager.types.secret_id_type
    import capo_secrets_manager.types.secret_string_type
    import capo_secrets_manager.types.secret_version_stages_type


class PutSecretValueRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to add a new version to.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p> <p>If the secret doesn't already exist, use <code>CreateSecret</code> instead.</p>"""
    client_request_token: NotRequired[
        "capo_secrets_manager.types.client_request_token_type.ClientRequestTokenType"
    ]
    """<p>A unique identifier for the new version of the secret. </p> <note> <p>If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. </p> </note> <p>If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a <code>ClientRequestToken</code> and include it in the request.</p> <p>This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value to ensure uniqueness of your versions within the specified secret. </p> <ul> <li> <p>If the <code>ClientRequestToken</code> value isn't already associated with a version of the secret then a new version of the secret is created. </p> </li> <li> <p>If a version with this value already exists and that version's <code>SecretString</code> or <code>SecretBinary</code> values are the same as those in the request then the request is ignored. The operation is idempotent. </p> </li> <li> <p>If a version with this value already exists and the version of the <code>SecretString</code> and <code>SecretBinary</code> values are different from those in the request, then the request fails because you can't modify a secret version. You can only create new versions to store new secret values.</p> </li> </ul> <p>This value becomes the <code>VersionId</code> of the new version.</p>"""
    secret_binary: NotRequired[
        "capo_secrets_manager.types.secret_binary_type.SecretBinaryType"
    ]
    """<p>The binary data to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then pass the contents of the file as a parameter. </p> <p>You must include <code>SecretBinary</code> or <code>SecretString</code>, but not both.</p> <p>You can't access this value from the Secrets Manager console.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>"""
    secret_string: NotRequired[
        "capo_secrets_manager.types.secret_string_type.SecretStringType"
    ]
    """<p>The text to encrypt and store in the new version of the secret. </p> <p>You must include <code>SecretBinary</code> or <code>SecretString</code>, but not both.</p> <p>We recommend you create the secret string as JSON key/value pairs, as shown in the example.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>"""
    version_stages: NotRequired[
        "capo_secrets_manager.types.secret_version_stages_type.SecretVersionStagesType"
    ]
    """<p>A list of staging labels to attach to this version of the secret. Secrets Manager uses staging labels to track versions of a secret through the rotation process.</p> <p>If you specify a staging label that's already associated with a different version of the same secret, then Secrets Manager removes the label from the other version and attaches it to this version. If you specify <code>AWSCURRENT</code>, and it is already attached to another version, then Secrets Manager also moves the staging label <code>AWSPREVIOUS</code> to the version that <code>AWSCURRENT</code> was removed from.</p> <p>If you don't include <code>VersionStages</code>, then Secrets Manager automatically moves the staging label <code>AWSCURRENT</code> to this version.</p>"""
    rotation_token: NotRequired[
        "capo_secrets_manager.types.rotation_token_type.RotationTokenType"
    ]
    """<p>A unique identifier that indicates the source of the request. Required for secret rotations using an IAM assumed role or cross-account rotation, in which you rotate a secret in one account by using a Lambda rotation function in another account. In both cases, the rotation function assumes an IAM role to call Secrets Manager, and then Secrets Manager validates the identity using the token. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html">How rotation works</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_lambda">Rotation by Lambda functions</a>.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutSecretValueRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "secret_binary" in value:
        import capo_secrets_manager.types.secret_binary_type

        out["SecretBinary"] = (
            capo_secrets_manager.types.secret_binary_type.serialize_aws_json_1_1(
                value["secret_binary"]
            )
        )
    if "secret_string" in value:
        out["SecretString"] = value["secret_string"]
    if "version_stages" in value:
        import capo_secrets_manager.types.secret_version_stages_type

        out["VersionStages"] = (
            capo_secrets_manager.types.secret_version_stages_type.serialize_aws_json_1_1(
                value["version_stages"]
            )
        )
    if "rotation_token" in value:
        out["RotationToken"] = value["rotation_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutSecretValueRequest:
    out: PutSecretValueRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("PutSecretValueRequest.secret_id required")
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("SecretBinary") is not None:
        import capo_secrets_manager.types.secret_binary_type

        out["secret_binary"] = (
            capo_secrets_manager.types.secret_binary_type.deserialize_aws_json_1_1(
                data["SecretBinary"]
            )
        )
    if data.get("SecretString") is not None:
        out["secret_string"] = data["SecretString"]
    if data.get("VersionStages") is not None:
        import capo_secrets_manager.types.secret_version_stages_type

        out["version_stages"] = (
            capo_secrets_manager.types.secret_version_stages_type.deserialize_aws_json_1_1(
                data["VersionStages"]
            )
        )
    if data.get("RotationToken") is not None:
        out["rotation_token"] = data["RotationToken"]
    return out
