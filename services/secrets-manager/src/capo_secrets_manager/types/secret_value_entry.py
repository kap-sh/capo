"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretValueEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.created_date_type
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.secret_binary_type
    import capo_secrets_manager.types.secret_name_type
    import capo_secrets_manager.types.secret_string_type
    import capo_secrets_manager.types.secret_version_id_type
    import capo_secrets_manager.types.secret_version_stages_type


class SecretValueEntry(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The Amazon Resource Name (ARN) of the secret.</p>"""
    name: NotRequired["capo_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The friendly name of the secret. </p>"""
    version_id: NotRequired[
        "capo_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The unique version identifier of this version of the secret.</p>"""
    secret_binary: NotRequired[
        "capo_secrets_manager.types.secret_binary_type.SecretBinaryType"
    ]
    """<p>The decrypted secret value, if the secret value was originally provided as binary data in the form of a byte array. The parameter represents the binary data as a <a href="https://tools.ietf.org/html/rfc4648#section-4">base64-encoded</a> string.</p>"""
    secret_string: NotRequired[
        "capo_secrets_manager.types.secret_string_type.SecretStringType"
    ]
    """<p>The decrypted secret value, if the secret value was originally provided as a string or through the Secrets Manager console.</p>"""
    version_stages: NotRequired[
        "capo_secrets_manager.types.secret_version_stages_type.SecretVersionStagesType"
    ]
    """<p>A list of all of the staging labels currently attached to this version of the secret.</p>"""
    created_date: NotRequired[
        "capo_secrets_manager.types.created_date_type.CreatedDateType"
    ]
    """<p>The date the secret was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretValueEntry) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> SecretValueEntry:
    out: SecretValueEntry = {}  # type: ignore[typeddict-item]
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
