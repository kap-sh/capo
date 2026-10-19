"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetRepositorySyncStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.branch_name
    import capo_codestar_connections.types.repository_link_id
    import capo_codestar_connections.types.sync_configuration_type


class GetRepositorySyncStatusInput(TypedDict, closed=True):
    branch: "capo_codestar_connections.types.branch_name.BranchName"
    """<p>The branch of the repository link for the requested repository sync status.</p>"""
    repository_link_id: (
        "capo_codestar_connections.types.repository_link_id.RepositoryLinkId"
    )
    """<p>The repository link ID for the requested repository sync status.</p>"""
    sync_type: (
        "capo_codestar_connections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The sync type of the requested sync status.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositorySyncStatusInput) -> dict:
    out: dict = {}
    out["Branch"] = value["branch"]
    out["RepositoryLinkId"] = value["repository_link_id"]
    import capo_codestar_connections.types.sync_configuration_type

    out["SyncType"] = (
        capo_codestar_connections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositorySyncStatusInput:
    out: GetRepositorySyncStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("Branch") is not None:
        out["branch"] = data["Branch"]
    else:
        out["branch"] = ""
    if data.get("RepositoryLinkId") is not None:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        out["repository_link_id"] = ""
    if data.get("SyncType") is not None:
        import capo_codestar_connections.types.sync_configuration_type

        out["sync_type"] = (
            capo_codestar_connections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        import typing

        out["sync_type"] = typing.cast(
            "capo_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
            "",
        )
    return out
