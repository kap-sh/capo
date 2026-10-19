"""Generated from Smithy shape ``com.amazonaws.codestarconnections#SyncBlocker``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.blocker_status
    import capo_codestar_connections.types.blocker_type
    import capo_codestar_connections.types.created_reason
    import capo_codestar_connections.types.id
    import capo_codestar_connections.types.resolved_reason
    import capo_codestar_connections.types.sync_blocker_context_list
    import capo_codestar_connections.types.timestamp


class SyncBlocker(TypedDict, closed=True):
    id: "capo_codestar_connections.types.id.Id"
    """<p>The ID for a specific sync blocker.</p>"""
    type: "capo_codestar_connections.types.blocker_type.BlockerType"
    """<p>The sync blocker type.</p>"""
    status: "capo_codestar_connections.types.blocker_status.BlockerStatus"
    """<p>The status for a specific sync blocker.</p>"""
    created_reason: "capo_codestar_connections.types.created_reason.CreatedReason"
    """<p>The provided reason for a specific sync blocker.</p>"""
    created_at: "capo_codestar_connections.types.timestamp.Timestamp"
    """<p>The creation time for a specific sync blocker.</p>"""
    contexts: NotRequired[
        "capo_codestar_connections.types.sync_blocker_context_list.SyncBlockerContextList"
    ]
    """<p>The contexts for a specific sync blocker.</p>"""
    resolved_reason: NotRequired[
        "capo_codestar_connections.types.resolved_reason.ResolvedReason"
    ]
    """<p>The resolved reason for a specific sync blocker.</p>"""
    resolved_at: NotRequired["capo_codestar_connections.types.timestamp.Timestamp"]
    """<p>The time that a specific sync blocker was resolved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlocker) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_codestar_connections.types.blocker_type

    out["Type"] = capo_codestar_connections.types.blocker_type.serialize_aws_json_1_0(
        value["type"]
    )
    import capo_codestar_connections.types.blocker_status

    out["Status"] = (
        capo_codestar_connections.types.blocker_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    out["CreatedReason"] = value["created_reason"]
    import capo_codestar_connections.types.timestamp

    out["CreatedAt"] = capo_codestar_connections.types.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "contexts" in value:
        import capo_codestar_connections.types.sync_blocker_context_list

        out["Contexts"] = (
            capo_codestar_connections.types.sync_blocker_context_list.serialize_aws_json_1_0(
                value["contexts"]
            )
        )
    if "resolved_reason" in value:
        out["ResolvedReason"] = value["resolved_reason"]
    if "resolved_at" in value:
        import capo_codestar_connections.types.timestamp

        out["ResolvedAt"] = (
            capo_codestar_connections.types.timestamp.serialize_aws_json_1_0(
                value["resolved_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlocker:
    out: SyncBlocker = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Type") is not None:
        import capo_codestar_connections.types.blocker_type

        out["type"] = (
            capo_codestar_connections.types.blocker_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_codestar_connections.types.blocker_type.BlockerType", ""
        )
    if data.get("Status") is not None:
        import capo_codestar_connections.types.blocker_status

        out["status"] = (
            capo_codestar_connections.types.blocker_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_codestar_connections.types.blocker_status.BlockerStatus", ""
        )
    if data.get("CreatedReason") is not None:
        out["created_reason"] = data["CreatedReason"]
    else:
        out["created_reason"] = ""
    if data.get("CreatedAt") is not None:
        import capo_codestar_connections.types.timestamp

        out["created_at"] = (
            capo_codestar_connections.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Contexts") is not None:
        import capo_codestar_connections.types.sync_blocker_context_list

        out["contexts"] = (
            capo_codestar_connections.types.sync_blocker_context_list.deserialize_aws_json_1_0(
                data["Contexts"]
            )
        )
    if data.get("ResolvedReason") is not None:
        out["resolved_reason"] = data["ResolvedReason"]
    if data.get("ResolvedAt") is not None:
        import capo_codestar_connections.types.timestamp

        out["resolved_at"] = (
            capo_codestar_connections.types.timestamp.deserialize_aws_json_1_0(
                data["ResolvedAt"]
            )
        )
    return out
