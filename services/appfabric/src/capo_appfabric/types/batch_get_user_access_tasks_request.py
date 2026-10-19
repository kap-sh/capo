"""Generated from Smithy shape ``com.amazonaws.appfabric#BatchGetUserAccessTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.identifier
    import capo_appfabric.types.task_id_list


class BatchGetUserAccessTasksRequest(TypedDict, closed=True):
    app_bundle_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    task_id_list: "capo_appfabric.types.task_id_list.TaskIdList"
    """<p>The tasks IDs to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetUserAccessTasksRequest) -> dict:
    out: dict = {}
    out["appBundleIdentifier"] = value["app_bundle_identifier"]
    import capo_appfabric.types.task_id_list

    out["taskIdList"] = capo_appfabric.types.task_id_list.serialize_json(
        value["task_id_list"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetUserAccessTasksRequest:
    out: BatchGetUserAccessTasksRequest = {}  # type: ignore[typeddict-item]
    if data.get("appBundleIdentifier") is not None:
        out["app_bundle_identifier"] = data["appBundleIdentifier"]
    else:
        out["app_bundle_identifier"] = ""
    if data.get("taskIdList") is not None:
        import capo_appfabric.types.task_id_list

        out["task_id_list"] = capo_appfabric.types.task_id_list.deserialize_json(
            data["taskIdList"]
        )
    else:
        out["task_id_list"] = []
    return out
