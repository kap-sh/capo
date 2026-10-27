"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationBackfillSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.date
    import capo_ecr.types.replication_backfill_error
    import capo_ecr.types.replication_backfill_id
    import capo_ecr.types.replication_backfill_progress
    import capo_ecr.types.replication_backfill_status
    import capo_ecr.types.replication_destination


class ReplicationBackfillSummary(TypedDict, closed=True):
    replication_backfill_id: (
        "capo_ecr.types.replication_backfill_id.ReplicationBackfillId"
    )
    """<p>The ID of the replication backfill.</p>"""
    destination: "capo_ecr.types.replication_destination.ReplicationDestination"
    """<p>The destination Region and registry to which the images are replicated.</p>"""
    status: "capo_ecr.types.replication_backfill_status.ReplicationBackfillStatus"
    """<p>The current status of the replication backfill.</p>"""
    failure_code: NotRequired[
        "capo_ecr.types.replication_backfill_error.ReplicationBackfillError"
    ]
    """<p>The failure code for a replication backfill that has failed.</p>"""
    progress: NotRequired[
        "capo_ecr.types.replication_backfill_progress.ReplicationBackfillProgress"
    ]
    """<p>The progress of the replication backfill, including the total, completed, and failed replication counts. This value is <code>null</code> until the replication backfill finishes preparing the set of images to replicate. It is therefore <code>null</code> while the replication backfill is <code>PREPARING</code>, and remains <code>null</code> if the replication backfill is stopped before preparation completes.</p>"""
    started_at: "capo_ecr.types.date.Date"
    """<p>The date and time, in JavaScript date format, when the replication backfill was started.</p>"""
    ended_at: NotRequired["capo_ecr.types.date.Date"]
    """<p>The date and time, in JavaScript date format, when the replication backfill ended. This value is <code>null</code> while the replication backfill is still in progress.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationBackfillSummary) -> dict:
    out: dict = {}
    out["replicationBackfillId"] = value["replication_backfill_id"]
    import capo_ecr.types.replication_destination

    out["destination"] = capo_ecr.types.replication_destination.serialize_aws_json_1_1(
        value["destination"]
    )
    import capo_ecr.types.replication_backfill_status

    out["status"] = capo_ecr.types.replication_backfill_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "progress" in value:
        import capo_ecr.types.replication_backfill_progress

        out["progress"] = (
            capo_ecr.types.replication_backfill_progress.serialize_aws_json_1_1(
                value["progress"]
            )
        )
    import capo_ecr.types.date

    out["startedAt"] = capo_ecr.types.date.serialize_aws_json_1_1(value["started_at"])
    if "ended_at" in value:
        import capo_ecr.types.date

        out["endedAt"] = capo_ecr.types.date.serialize_aws_json_1_1(value["ended_at"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationBackfillSummary:
    out: ReplicationBackfillSummary = {}  # type: ignore[typeddict-item]
    if data.get("replicationBackfillId") is not None:
        out["replication_backfill_id"] = data["replicationBackfillId"]
    else:
        out["replication_backfill_id"] = ""
    if data.get("destination") is not None:
        import capo_ecr.types.replication_destination

        out["destination"] = (
            capo_ecr.types.replication_destination.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    else:
        raise DeserializationError("ReplicationBackfillSummary.destination required")
    if data.get("status") is not None:
        import capo_ecr.types.replication_backfill_status

        out["status"] = (
            capo_ecr.types.replication_backfill_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_ecr.types.replication_backfill_status.ReplicationBackfillStatus", ""
        )
    if data.get("failureCode") is not None:
        out["failure_code"] = data["failureCode"]
    if data.get("progress") is not None:
        import capo_ecr.types.replication_backfill_progress

        out["progress"] = (
            capo_ecr.types.replication_backfill_progress.deserialize_aws_json_1_1(
                data["progress"]
            )
        )
    if data.get("startedAt") is not None:
        import capo_ecr.types.date

        out["started_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endedAt") is not None:
        import capo_ecr.types.date

        out["ended_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(data["endedAt"])
    return out
