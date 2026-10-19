"""Generated from Smithy shape ``com.amazonaws.codeconnections#Revision``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.branch_name
    import capo_codeconnections.types.directory
    import capo_codeconnections.types.owner_id
    import capo_codeconnections.types.provider_type
    import capo_codeconnections.types.repository_name
    import capo_codeconnections.types.sha


class Revision(TypedDict, closed=True):
    branch: "capo_codeconnections.types.branch_name.BranchName"
    """<p>The branch name for a specific revision.</p>"""
    directory: "capo_codeconnections.types.directory.Directory"
    """<p>The directory, if any, for a specific revision.</p>"""
    owner_id: "capo_codeconnections.types.owner_id.OwnerId"
    """<p>The owner ID for a specific revision, such as the GitHub owner ID for a GitHub repository.</p>"""
    repository_name: "capo_codeconnections.types.repository_name.RepositoryName"
    """<p>The repository name for a specific revision.</p>"""
    provider_type: "capo_codeconnections.types.provider_type.ProviderType"
    """<p>The provider type for a revision, such as GitHub.</p>"""
    sha: "capo_codeconnections.types.sha.SHA"
    """<p>The SHA, such as the commit ID, for a specific revision.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Revision) -> dict:
    out: dict = {}
    out["Branch"] = value["branch"]
    out["Directory"] = value["directory"]
    out["OwnerId"] = value["owner_id"]
    out["RepositoryName"] = value["repository_name"]
    import capo_codeconnections.types.provider_type

    out["ProviderType"] = (
        capo_codeconnections.types.provider_type.serialize_aws_json_1_0(
            value["provider_type"]
        )
    )
    out["Sha"] = value["sha"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Revision:
    out: Revision = {}  # type: ignore[typeddict-item]
    if data.get("Branch") is not None:
        out["branch"] = data["Branch"]
    else:
        out["branch"] = ""
    if data.get("Directory") is not None:
        out["directory"] = data["Directory"]
    else:
        out["directory"] = ""
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    else:
        out["owner_id"] = ""
    if data.get("RepositoryName") is not None:
        out["repository_name"] = data["RepositoryName"]
    else:
        out["repository_name"] = ""
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
    if data.get("Sha") is not None:
        out["sha"] = data["Sha"]
    else:
        out["sha"] = ""
    return out
