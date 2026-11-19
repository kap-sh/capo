"""Generated from Smithy shape ``com.amazonaws.mgn#ListRemoteSourceActionInvocationsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_arns_filter
    import capo_mgn.types.remote_source_action_invocation_statuses_filter
    import capo_mgn.types.source_server_arns_filter


class ListRemoteSourceActionInvocationsRequestFilters(TypedDict, closed=True):
    source_server_arns: NotRequired[
        "capo_mgn.types.source_server_arns_filter.SourceServerArnsFilter"
    ]
    """<p>A list of source server ARNs to filter by.</p>"""
    remote_source_action_arns: NotRequired[
        "capo_mgn.types.remote_source_action_arns_filter.RemoteSourceActionArnsFilter"
    ]
    """<p>A list of source action ARNs to filter by.</p>"""
    statuses: NotRequired[
        "capo_mgn.types.remote_source_action_invocation_statuses_filter.RemoteSourceActionInvocationStatusesFilter"
    ]
    """<p>A list of invocation statuses to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRemoteSourceActionInvocationsRequestFilters) -> dict:
    out: dict = {}
    if "source_server_arns" in value:
        import capo_mgn.types.source_server_arns_filter

        out["sourceServerArns"] = (
            capo_mgn.types.source_server_arns_filter.serialize_json(
                value["source_server_arns"]
            )
        )
    if "remote_source_action_arns" in value:
        import capo_mgn.types.remote_source_action_arns_filter

        out["remoteSourceActionArns"] = (
            capo_mgn.types.remote_source_action_arns_filter.serialize_json(
                value["remote_source_action_arns"]
            )
        )
    if "statuses" in value:
        import capo_mgn.types.remote_source_action_invocation_statuses_filter

        out["statuses"] = (
            capo_mgn.types.remote_source_action_invocation_statuses_filter.serialize_json(
                value["statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRemoteSourceActionInvocationsRequestFilters:
    out: ListRemoteSourceActionInvocationsRequestFilters = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerArns") is not None:
        import capo_mgn.types.source_server_arns_filter

        out["source_server_arns"] = (
            capo_mgn.types.source_server_arns_filter.deserialize_json(
                data["sourceServerArns"]
            )
        )
    if data.get("remoteSourceActionArns") is not None:
        import capo_mgn.types.remote_source_action_arns_filter

        out["remote_source_action_arns"] = (
            capo_mgn.types.remote_source_action_arns_filter.deserialize_json(
                data["remoteSourceActionArns"]
            )
        )
    if data.get("statuses") is not None:
        import capo_mgn.types.remote_source_action_invocation_statuses_filter

        out["statuses"] = (
            capo_mgn.types.remote_source_action_invocation_statuses_filter.deserialize_json(
                data["statuses"]
            )
        )
    return out
