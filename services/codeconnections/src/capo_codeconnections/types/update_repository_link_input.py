"""Generated from Smithy shape ``com.amazonaws.codeconnections#UpdateRepositoryLinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.connection_arn
    import capo_codeconnections.types.kms_key_arn
    import capo_codeconnections.types.repository_link_id


class UpdateRepositoryLinkInput(TypedDict, closed=True):
    connection_arn: NotRequired[
        "capo_codeconnections.types.connection_arn.ConnectionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the connection for the repository link to be updated. The updated connection ARN must have the same providerType (such as GitHub) as the original connection ARN for the repo link.</p>"""
    encryption_key_arn: NotRequired["capo_codeconnections.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the encryption key for the repository link to be updated.</p>"""
    repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId"
    """<p>The ID of the repository link to be updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRepositoryLinkInput) -> dict:
    out: dict = {}
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    out["RepositoryLinkId"] = value["repository_link_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRepositoryLinkInput:
    out: UpdateRepositoryLinkInput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("RepositoryLinkId") is not None:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        out["repository_link_id"] = ""
    return out
