"""Generated from Smithy shape ``com.amazonaws.comprehend#ImportModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.tag_list
    import capo_comprehend.types.version_name


class ImportModelRequest(TypedDict, closed=True):
    source_model_arn: "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model to import.</p>"""
    model_name: NotRequired[
        "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
    ]
    """<p>The name to assign to the custom model that is created in Amazon Comprehend by this import.</p>"""
    version_name: NotRequired["capo_comprehend.types.version_name.VersionName"]
    """<p>The version name given to the custom model that is created by this import. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the account/Region.</p>"""
    model_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>"""
    data_access_role_arn: NotRequired["capo_comprehend.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to use Amazon Key Management Service (KMS) to encrypt or decrypt the custom model.</p>"""
    tags: NotRequired["capo_comprehend.types.tag_list.TagList"]
    """<p>Tags to associate with the custom model that is created by this import. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportModelRequest) -> dict:
    out: dict = {}
    out["SourceModelArn"] = value["source_model_arn"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "model_kms_key_id" in value:
        out["ModelKmsKeyId"] = value["model_kms_key_id"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "tags" in value:
        import capo_comprehend.types.tag_list

        out["Tags"] = capo_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportModelRequest:
    out: ImportModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceModelArn") is not None:
        out["source_model_arn"] = data["SourceModelArn"]
    else:
        raise DeserializationError("ImportModelRequest.source_model_arn required")
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("ModelKmsKeyId") is not None:
        out["model_kms_key_id"] = data["ModelKmsKeyId"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("Tags") is not None:
        import capo_comprehend.types.tag_list

        out["tags"] = capo_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
