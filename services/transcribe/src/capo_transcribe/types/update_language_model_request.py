"""Generated from Smithy shape ``com.amazonaws.transcribe#UpdateLanguageModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.data_access_role_arn
    import capo_transcribe.types.encryption_configuration
    import capo_transcribe.types.model_name


class UpdateLanguageModelRequest(TypedDict, closed=True):
    model_name: "capo_transcribe.types.model_name.ModelName"
    """<p>The name of the custom language model you want to update. Model names are case sensitive.</p>"""
    data_access_role_arn: NotRequired[
        "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an IAM role. If you include <code>EncryptionConfiguration</code> in your request, this role must have permissions to access the specified KMS key. If the role that you specify doesn't have the appropriate permissions, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>"""
    encryption_configuration: NotRequired[
        "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Specifies the new encryption configuration for your custom language model. The model artifacts are re-encrypted in place using the specified KMS key or with an AWS-owned key if a key is not supplied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLanguageModelRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "encryption_configuration" in value:
        import capo_transcribe.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_transcribe.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLanguageModelRequest:
    out: UpdateLanguageModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError("UpdateLanguageModelRequest.model_name required")
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_transcribe.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_transcribe.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    return out
