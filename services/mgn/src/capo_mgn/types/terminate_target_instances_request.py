"""Generated from Smithy shape ``com.amazonaws.mgn#TerminateTargetInstancesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.tags_map
    import capo_mgn.types.terminate_target_instances_request_source_server_i_ds


class TerminateTargetInstancesRequest(TypedDict, closed=True):
    source_server_i_ds: "capo_mgn.types.terminate_target_instances_request_source_server_i_ds.TerminateTargetInstancesRequestSourceServerIDs"
    """<p>Terminate Target instance by Source Server IDs.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Terminate Target instance by Tags.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Terminate Target instance by Account ID</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateTargetInstancesRequest) -> dict:
    out: dict = {}
    import capo_mgn.types.terminate_target_instances_request_source_server_i_ds

    out["sourceServerIDs"] = (
        capo_mgn.types.terminate_target_instances_request_source_server_i_ds.serialize_json(
            value["source_server_i_ds"]
        )
    )
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> TerminateTargetInstancesRequest:
    out: TerminateTargetInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerIDs") is not None:
        import capo_mgn.types.terminate_target_instances_request_source_server_i_ds

        out["source_server_i_ds"] = (
            capo_mgn.types.terminate_target_instances_request_source_server_i_ds.deserialize_json(
                data["sourceServerIDs"]
            )
        )
    else:
        out["source_server_i_ds"] = []
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out


def redact_sensitive(value: TerminateTargetInstancesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
