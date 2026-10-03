"""Generated from Smithy shape ``com.amazonaws.secretsmanager#UpdateSecretRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.client_request_token_type
    import capo_secrets_manager.types.description_type
    import capo_secrets_manager.types.kms_key_id_type
    import capo_secrets_manager.types.medea_type_type
    import capo_secrets_manager.types.secret_binary_type
    import capo_secrets_manager.types.secret_id_type
    import capo_secrets_manager.types.secret_string_type


class UpdateSecretRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    client_request_token: NotRequired[
        "capo_secrets_manager.types.client_request_token_type.ClientRequestTokenType"
    ]
    """<p>If you include <code>SecretString</code> or <code>SecretBinary</code>, then Secrets Manager creates a new version for the secret, and this parameter specifies the unique identifier for the new version.</p> <note> <p>If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. </p> </note> <p>If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a <code>ClientRequestToken</code> and include it in the request.</p> <p>This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value to ensure uniqueness of your versions within the specified secret. </p>"""
    description: NotRequired[
        "capo_secrets_manager.types.description_type.DescriptionType"
    ]
    """<p>The description of the secret.</p>"""
    kms_key_id: NotRequired["capo_secrets_manager.types.kms_key_id_type.KmsKeyIdType"]
    """<p>The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt new secret versions as well as any existing versions with the staging labels <code>AWSCURRENT</code>, <code>AWSPENDING</code>, or <code>AWSPREVIOUS</code>. If you don't have <code>kms:Encrypt</code> permission to the new key, Secrets Manager does not re-encrypt existing secret versions with the new key. For more information about versions and staging labels, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version">Concepts: Version</a>.</p> <p>A key alias is always prefixed by <code>alias/</code>, for example <code>alias/aws/secretsmanager</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html">About aliases</a>.</p> <p>If you set this to an empty string, Secrets Manager uses the Amazon Web Services managed key <code>aws/secretsmanager</code>. If this key doesn't already exist in your account, then Secrets Manager creates it for you automatically. All users and roles in the Amazon Web Services account automatically have access to use <code>aws/secretsmanager</code>. Creating <code>aws/secretsmanager</code> can result in a one-time significant delay in returning the result. </p> <important> <p>You can only use the Amazon Web Services managed key <code>aws/secretsmanager</code> if you call this operation using credentials from the same Amazon Web Services account that owns the secret. If the secret is in a different account, then you must use a customer managed key and provide the ARN of that KMS key in this field. The user making the call must have permissions to both the secret and the KMS key in their respective accounts.</p> </important>"""
    secret_binary: NotRequired[
        "capo_secrets_manager.types.secret_binary_type.SecretBinaryType"
    ]
    """<p>The binary data to encrypt and store in the new version of the secret. We recommend that you store your binary data in a file and then pass the contents of the file as a parameter. </p> <p>Either <code>SecretBinary</code> or <code>SecretString</code> must have a value, but not both.</p> <p>You can't access this parameter in the Secrets Manager console.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>"""
    secret_string: NotRequired[
        "capo_secrets_manager.types.secret_string_type.SecretStringType"
    ]
    """<p>The text data to encrypt and store in the new version of the secret. We recommend you use a JSON structure of key/value pairs for your secret value. </p> <p>Either <code>SecretBinary</code> or <code>SecretString</code> must have a value, but not both. </p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>"""
    type: NotRequired["capo_secrets_manager.types.medea_type_type.MedeaTypeType"]
    """<p>The exact string that identifies the third-party partner that holds the external secret. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html">Managed external secret partners</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSecretRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "secret_binary" in value:
        import capo_secrets_manager.types.secret_binary_type

        out["SecretBinary"] = (
            capo_secrets_manager.types.secret_binary_type.serialize_aws_json_1_1(
                value["secret_binary"]
            )
        )
    if "secret_string" in value:
        out["SecretString"] = value["secret_string"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSecretRequest:
    out: UpdateSecretRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("UpdateSecretRequest.secret_id required")
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("SecretBinary") is not None:
        import capo_secrets_manager.types.secret_binary_type

        out["secret_binary"] = (
            capo_secrets_manager.types.secret_binary_type.deserialize_aws_json_1_1(
                data["SecretBinary"]
            )
        )
    if data.get("SecretString") is not None:
        out["secret_string"] = data["SecretString"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
