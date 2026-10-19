"""Generated from Smithy shape ``com.amazonaws.codeconnections#RepositoryLinkInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.connection_arn
    import capo_codeconnections.types.kms_key_arn
    import capo_codeconnections.types.owner_id
    import capo_codeconnections.types.provider_type
    import capo_codeconnections.types.repository_link_arn
    import capo_codeconnections.types.repository_link_id
    import capo_codeconnections.types.repository_name


class RepositoryLinkInfo(TypedDict, closed=True):
    connection_arn: "capo_codeconnections.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the connection associated with the repository link.</p>"""
    encryption_key_arn: NotRequired["capo_codeconnections.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the encryption key for the repository associated with the repository link.</p>"""
    owner_id: "capo_codeconnections.types.owner_id.OwnerId"
    """<p>The owner ID for the repository associated with the repository link, such as the owner ID in GitHub.</p>"""
    provider_type: "capo_codeconnections.types.provider_type.ProviderType"
    """<p>The provider type for the connection, such as GitHub, associated with the repository link.</p>"""
    repository_link_arn: (
        "capo_codeconnections.types.repository_link_arn.RepositoryLinkArn"
    )
    """<p>The Amazon Resource Name (ARN) of the repository link.</p>"""
    repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId"
    """<p>The ID of the repository link.</p>"""
    repository_name: "capo_codeconnections.types.repository_name.RepositoryName"
    """<p>The name of the repository associated with the repository link.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositoryLinkInfo) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    out["OwnerId"] = value["owner_id"]
    import capo_codeconnections.types.provider_type

    out["ProviderType"] = (
        capo_codeconnections.types.provider_type.serialize_aws_json_1_0(
            value["provider_type"]
        )
    )
    out["RepositoryLinkArn"] = value["repository_link_arn"]
    out["RepositoryLinkId"] = value["repository_link_id"]
    out["RepositoryName"] = value["repository_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositoryLinkInfo:
    out: RepositoryLinkInfo = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        out["connection_arn"] = ""
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    else:
        out["owner_id"] = ""
    if data.get("ProviderType") is not None:
        import capo_codeconnections.types.provider_type

        out["provider_type"] = (
            capo_codeconnections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    else:
        import typing

        out["provider_type"] = typing.cast(
            "capo_codeconnections.types.provider_type.ProviderType", ""
        )
    if data.get("RepositoryLinkArn") is not None:
        out["repository_link_arn"] = data["RepositoryLinkArn"]
    else:
        out["repository_link_arn"] = ""
    if data.get("RepositoryLinkId") is not None:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        out["repository_link_id"] = ""
    if data.get("RepositoryName") is not None:
        out["repository_name"] = data["RepositoryName"]
    else:
        out["repository_name"] = ""
    return out
