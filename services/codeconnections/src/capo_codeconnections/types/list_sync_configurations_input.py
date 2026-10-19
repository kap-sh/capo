"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListSyncConfigurationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.max_results
    import capo_codeconnections.types.repository_link_id
    import capo_codeconnections.types.sharp_next_token
    import capo_codeconnections.types.sync_configuration_type


class ListSyncConfigurationsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_codeconnections.types.max_results.MaxResults"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results.</p>"""
    next_token: NotRequired[
        "capo_codeconnections.types.sharp_next_token.SharpNextToken"
    ]
    """<p>An enumeration token that allows the operation to batch the results of the operation.</p>"""
    repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId"
    """<p>The ID of the repository link for the requested list of sync configurations.</p>"""
    sync_type: (
        "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The sync type for the requested list of sync configurations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSyncConfigurationsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["RepositoryLinkId"] = value["repository_link_id"]
    import capo_codeconnections.types.sync_configuration_type

    out["SyncType"] = (
        capo_codeconnections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSyncConfigurationsInput:
    out: ListSyncConfigurationsInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RepositoryLinkId") is not None:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        out["repository_link_id"] = ""
    if data.get("SyncType") is not None:
        import capo_codeconnections.types.sync_configuration_type

        out["sync_type"] = (
            capo_codeconnections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        import typing

        out["sync_type"] = typing.cast(
            "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
            "",
        )
    return out
