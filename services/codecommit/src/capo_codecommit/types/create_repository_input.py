"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateRepositoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.kms_key_id
    import capo_codecommit.types.repository_description
    import capo_codecommit.types.repository_name
    import capo_codecommit.types.tags_map


class CreateRepositoryInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the new repository to be created.</p> <note> <p>The repository name must be unique across the calling Amazon Web Services account. Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For more information about the limits on repository names, see <a href="https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html">Quotas</a> in the <i>CodeCommit User Guide</i>. The suffix .git is prohibited.</p> </note>"""
    repository_description: NotRequired[
        "capo_codecommit.types.repository_description.RepositoryDescription"
    ]
    """<p>A comment or description about the new repository.</p> <note> <p>The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.</p> </note>"""
    tags: NotRequired["capo_codecommit.types.tags_map.TagsMap"]
    """<p>One or more tag key-value pairs to use when tagging this repository.</p>"""
    kms_key_id: NotRequired["capo_codecommit.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the encryption key. You can view the ID of an encryption key in the KMS console, or use the KMS APIs to programmatically retrieve a key ID. For more information about acceptable values for kmsKeyID, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html#KMS-Decrypt-request-KeyId">KeyId</a> in the Decrypt API description in the <i>Key Management Service API Reference</i>.</p> <p>If no key is specified, the default <code>aws/codecommit</code> Amazon Web Services managed key is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRepositoryInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "repository_description" in value:
        out["repositoryDescription"] = value["repository_description"]
    if "tags" in value:
        import capo_codecommit.types.tags_map

        out["tags"] = capo_codecommit.types.tags_map.serialize_aws_json_1_1(
            value["tags"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRepositoryInput:
    out: CreateRepositoryInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("CreateRepositoryInput.repository_name required")
    if data.get("repositoryDescription") is not None:
        out["repository_description"] = data["repositoryDescription"]
    if data.get("tags") is not None:
        import capo_codecommit.types.tags_map

        out["tags"] = capo_codecommit.types.tags_map.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
