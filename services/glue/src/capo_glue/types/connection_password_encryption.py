"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionPasswordEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean
    import capo_glue.types.name_string


class ConnectionPasswordEncryption(TypedDict, closed=True):
    return_connection_password_encrypted: "capo_glue.types.boolean.Boolean"
    """<p>When the <code>ReturnConnectionPasswordEncrypted</code> flag is set to "true", passwords remain encrypted in the responses of <code>GetConnection</code> and <code>GetConnections</code>. This encryption takes effect independently from catalog encryption. </p>"""
    aws_kms_key_id: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>An KMS key that is used to encrypt the connection password. </p> <p>If connection password protection is enabled, the caller of <code>CreateConnection</code> and <code>UpdateConnection</code> needs at least <code>kms:Encrypt</code> permission on the specified KMS key, to encrypt passwords before storing them in the Data Catalog. </p> <p>You can set the decrypt permission to enable or restrict access on the password key according to your security requirements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionPasswordEncryption) -> dict:
    out: dict = {}
    out["ReturnConnectionPasswordEncrypted"] = value.get(
        "return_connection_password_encrypted", False
    )
    if "aws_kms_key_id" in value:
        out["AwsKmsKeyId"] = value["aws_kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionPasswordEncryption:
    out: ConnectionPasswordEncryption = {}  # type: ignore[typeddict-item]
    if data.get("ReturnConnectionPasswordEncrypted") is not None:
        out["return_connection_password_encrypted"] = data[
            "ReturnConnectionPasswordEncrypted"
        ]
    else:
        out["return_connection_password_encrypted"] = False
    if data.get("AwsKmsKeyId") is not None:
        out["aws_kms_key_id"] = data["AwsKmsKeyId"]
    return out
