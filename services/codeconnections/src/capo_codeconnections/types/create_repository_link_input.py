"""Generated from Smithy shape ``com.amazonaws.codeconnections#CreateRepositoryLinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.connection_arn
    import capo_codeconnections.types.kms_key_arn
    import capo_codeconnections.types.owner_id
    import capo_codeconnections.types.repository_name
    import capo_codeconnections.types.tag_list


class CreateRepositoryLinkInput(TypedDict, closed=True):
    connection_arn: "capo_codeconnections.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the connection to be associated with the repository link.</p>"""
    owner_id: "capo_codeconnections.types.owner_id.OwnerId"
    """<p>The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.</p>"""
    repository_name: "capo_codeconnections.types.repository_name.RepositoryName"
    """<p>The name of the repository to be associated with the repository link.</p>"""
    encryption_key_arn: NotRequired["capo_codeconnections.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) encryption key for the repository to be associated with the repository link.</p>"""
    tags: NotRequired["capo_codeconnections.types.tag_list.TagList"]
    """<p>The tags for the repository to be associated with the repository link.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRepositoryLinkInput) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    out["OwnerId"] = value["owner_id"]
    out["RepositoryName"] = value["repository_name"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "tags" in value:
        import capo_codeconnections.types.tag_list

        out["Tags"] = capo_codeconnections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRepositoryLinkInput:
    out: CreateRepositoryLinkInput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        out["connection_arn"] = ""
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    else:
        out["owner_id"] = ""
    if data.get("RepositoryName") is not None:
        out["repository_name"] = data["RepositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("Tags") is not None:
        import capo_codeconnections.types.tag_list

        out["tags"] = capo_codeconnections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
