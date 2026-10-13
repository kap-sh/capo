"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetSecretValueResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.created_date_type
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.secret_binary_type
    import capo_secrets_manager.types.secret_name_type
    import capo_secrets_manager.types.secret_string_type
    import capo_secrets_manager.types.secret_version_id_type
    import capo_secrets_manager.types.secret_version_stages_type


class GetSecretValueResponse(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["capo_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The friendly name of the secret.</p>"""
    version_id: NotRequired[
        "capo_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The unique identifier of this version of the secret.</p>"""
    secret_binary: NotRequired[
        "capo_secrets_manager.types.secret_binary_type.SecretBinaryType"
    ]
    """<p>The decrypted secret value, if the secret value was originally provided as binary data in the form of a byte array. When you retrieve a <code>SecretBinary</code> using the HTTP API, the Python SDK, or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not encoded.</p> <p>If the secret was created by using the Secrets Manager console, or if the secret value was originally provided as a string, then this field is omitted. The secret value appears in <code>SecretString</code> instead.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>"""
    secret_string: NotRequired[
        "capo_secrets_manager.types.secret_string_type.SecretStringType"
    ]
    """<p>The decrypted secret value, if the secret value was originally provided as a string or through the Secrets Manager console.</p> <p>If this secret was created by using the console, then Secrets Manager stores the information as a JSON structure of key/value pairs. </p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>"""
    version_stages: NotRequired[
        "capo_secrets_manager.types.secret_version_stages_type.SecretVersionStagesType"
    ]
    """<p>A list of all of the staging labels currently attached to this version of the secret.</p>"""
    created_date: NotRequired[
        "capo_secrets_manager.types.created_date_type.CreatedDateType"
    ]
    """<p>The date and time that this version of the secret was created. If you don't specify which version in <code>VersionId</code> or <code>VersionStage</code>, then Secrets Manager uses the <code>AWSCURRENT</code> version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSecretValueResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
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
    if "created_date" in value:
        import capo_secrets_manager.types.created_date_type

        out["CreatedDate"] = (
            capo_secrets_manager.types.created_date_type.serialize_aws_json_1_1(
                value["created_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSecretValueResponse:
    out: GetSecretValueResponse = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
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
    if data.get("CreatedDate") is not None:
        import capo_secrets_manager.types.created_date_type

        out["created_date"] = (
            capo_secrets_manager.types.created_date_type.deserialize_aws_json_1_1(
                data["CreatedDate"]
            )
        )
    return out


def redact_sensitive(value: GetSecretValueResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_binary" in value:
        out["secret_binary"] = "*** Sensitive Data Redacted ***"
    if "secret_string" in value:
        out["secret_string"] = "*** Sensitive Data Redacted ***"
    return out
