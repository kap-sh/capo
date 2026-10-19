"""Generated from Smithy shape ``com.amazonaws.proton#SyncBlocker``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.blocker_status
    import capo_proton.types.blocker_type
    import capo_proton.types.sync_blocker_contexts


class SyncBlocker(TypedDict, closed=True):
    id: "str"
    """<p>The ID of the sync blocker.</p>"""
    type: "capo_proton.types.blocker_type.BlockerType"
    """<p>The type of the sync blocker.</p>"""
    status: "capo_proton.types.blocker_status.BlockerStatus"
    """<p>The status of the sync blocker.</p>"""
    created_reason: "str"
    """<p>The reason why the sync blocker was created.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the sync blocker was created.</p>"""
    contexts: NotRequired["capo_proton.types.sync_blocker_contexts.SyncBlockerContexts"]
    """<p>The contexts for the sync blocker.</p>"""
    resolved_reason: NotRequired["str"]
    """<p>The reason the sync blocker was resolved.</p>"""
    resolved_at: NotRequired["datetime.datetime"]
    """<p>The time the sync blocker was resolved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlocker) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    out["status"] = value["status"]
    out["createdReason"] = value["created_reason"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "contexts" in value:
        import capo_proton.types.sync_blocker_contexts

        out["contexts"] = (
            capo_proton.types.sync_blocker_contexts.serialize_aws_json_1_0(
                value["contexts"]
            )
        )
    if "resolved_reason" in value:
        out["resolvedReason"] = value["resolved_reason"]
    if "resolved_at" in value:
        import capo_proton.types._prelude.timestamp

        out["resolvedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["resolved_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlocker:
    out: SyncBlocker = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("createdReason") is not None:
        out["created_reason"] = data["createdReason"]
    else:
        out["created_reason"] = ""
    if data.get("createdAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("contexts") is not None:
        import capo_proton.types.sync_blocker_contexts

        out["contexts"] = (
            capo_proton.types.sync_blocker_contexts.deserialize_aws_json_1_0(
                data["contexts"]
            )
        )
    if data.get("resolvedReason") is not None:
        out["resolved_reason"] = data["resolvedReason"]
    if data.get("resolvedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["resolved_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["resolvedAt"]
            )
        )
    return out
