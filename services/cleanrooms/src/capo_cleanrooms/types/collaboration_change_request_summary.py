"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationChangeRequestSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.approval_statuses
    import capo_cleanrooms.types.change_list
    import capo_cleanrooms.types.change_request_status
    import capo_cleanrooms.types.uuid


class CollaborationChangeRequestSummary(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier for the change request.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier for the collaboration.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the change request was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time when the change request was last updated.</p>"""
    status: "capo_cleanrooms.types.change_request_status.ChangeRequestStatus"
    """<p>The current status of the change request.</p>"""
    is_auto_approved: "bool"
    """<p>Whether the change request was automatically approved.</p>"""
    changes: "capo_cleanrooms.types.change_list.ChangeList"
    """<p>Summary of the changes in this change request.</p>"""
    approvals: NotRequired["capo_cleanrooms.types.approval_statuses.ApprovalStatuses"]
    """<p>Summary of approval statuses from all collaboration members for this change request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationChangeRequestSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["collaborationId"] = value["collaboration_id"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import capo_cleanrooms.types.change_request_status

    out["status"] = capo_cleanrooms.types.change_request_status.serialize_json(
        value["status"]
    )
    out["isAutoApproved"] = value["is_auto_approved"]
    import capo_cleanrooms.types.change_list

    out["changes"] = capo_cleanrooms.types.change_list.serialize_json(value["changes"])
    if "approvals" in value:
        import capo_cleanrooms.types.approval_statuses

        out["approvals"] = capo_cleanrooms.types.approval_statuses.serialize_json(
            value["approvals"]
        )
    return out


def deserialize_json(data: dict) -> CollaborationChangeRequestSummary:
    out: CollaborationChangeRequestSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("status") is not None:
        import capo_cleanrooms.types.change_request_status

        out["status"] = capo_cleanrooms.types.change_request_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanrooms.types.change_request_status.ChangeRequestStatus", ""
        )
    if data.get("isAutoApproved") is not None:
        out["is_auto_approved"] = data["isAutoApproved"]
    else:
        out["is_auto_approved"] = False
    if data.get("changes") is not None:
        import capo_cleanrooms.types.change_list

        out["changes"] = capo_cleanrooms.types.change_list.deserialize_json(
            data["changes"]
        )
    else:
        out["changes"] = []
    if data.get("approvals") is not None:
        import capo_cleanrooms.types.approval_statuses

        out["approvals"] = capo_cleanrooms.types.approval_statuses.deserialize_json(
            data["approvals"]
        )
    return out
