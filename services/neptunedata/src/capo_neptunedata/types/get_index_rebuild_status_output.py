"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetIndexRebuildStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_neptunedata.types.rebuild_concurrency
    import capo_neptunedata.types.rebuild_status
    import capo_neptunedata.types.scope
    import capo_neptunedata.types.write_buffer_size


class GetIndexRebuildStatusOutput(TypedDict, closed=True):
    status: "capo_neptunedata.types.rebuild_status.RebuildStatus"
    """<p>The current status of the rebuild operation. See <code>RebuildStatus</code> for possible values: <code>PREPARING</code>, <code>REBUILDING</code>, <code>COMPLETED</code>, <code>FAILED</code>, <code>CANCELLING</code> or <code>CANCELLED</code>.</p>"""
    scope: "capo_neptunedata.types.scope.Scope"
    """<p>The scope of the rebuild operation. See <code>Scope</code> for possible values: <code>ALL</code>, <code>QUADS</code>, or <code>DICTIONARIES</code>.</p>"""
    concurrency: "capo_neptunedata.types.rebuild_concurrency.RebuildConcurrency"
    """<p>The concurrency in effect for this rebuild, as echoed from the original <code>StartIndexRebuild</code> request.</p>"""
    write_buffer_size: "capo_neptunedata.types.write_buffer_size.WriteBufferSize"
    """<p>The <code>WriteBufferSize</code> in effect for this rebuild, as echoed from the original <code>StartIndexRebuild</code> request.</p>"""
    start_time: "datetime.datetime"
    """<p>The ISO-8601 timestamp indicating when the index rebuild operation started.</p>"""
    progress_percentage: "int"
    """<p>The percentage of the index rebuild operation that has been completed, expressed as an integer from 0 to 100.</p>"""
    estimated_end_time: NotRequired["datetime.datetime"]
    """<p>The estimated ISO-8601 timestamp for when the index rebuild operation will complete. The estimate may change as the operation progresses.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp indicating when the index rebuild operation completed. This field is only present when the operation has completed (status is <code>COMPLETED</code>, <code>FAILED</code>, or <code>CANCELLED</code>).</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for the failure, if the rebuild operation failed. This field is only populated when the status is <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexRebuildStatusOutput) -> dict:
    out: dict = {}
    import capo_neptunedata.types.rebuild_status

    out["status"] = capo_neptunedata.types.rebuild_status.serialize_json(
        value["status"]
    )
    import capo_neptunedata.types.scope

    out["scope"] = capo_neptunedata.types.scope.serialize_json(value["scope"])
    out["concurrency"] = value["concurrency"]
    import capo_neptunedata.types.write_buffer_size

    out["writeBufferSize"] = capo_neptunedata.types.write_buffer_size.serialize_json(
        value["write_buffer_size"]
    )
    import capo_neptunedata._protocol.serialize

    out["startTime"] = capo_neptunedata._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    out["progressPercentage"] = value["progress_percentage"]
    if "estimated_end_time" in value:
        import capo_neptunedata._protocol.serialize

        out["estimatedEndTime"] = capo_neptunedata._protocol.serialize.fmt_date_time(
            value["estimated_end_time"]
        )
    if "end_time" in value:
        import capo_neptunedata._protocol.serialize

        out["endTime"] = capo_neptunedata._protocol.serialize.fmt_date_time(
            value["end_time"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> GetIndexRebuildStatusOutput:
    out: GetIndexRebuildStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_neptunedata.types.rebuild_status

        out["status"] = capo_neptunedata.types.rebuild_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_neptunedata.types.rebuild_status.RebuildStatus", ""
        )
    if data.get("scope") is not None:
        import capo_neptunedata.types.scope

        out["scope"] = capo_neptunedata.types.scope.deserialize_json(data["scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_neptunedata.types.scope.Scope", "")
    if data.get("concurrency") is not None:
        out["concurrency"] = data["concurrency"]
    else:
        out["concurrency"] = 0
    if data.get("writeBufferSize") is not None:
        import capo_neptunedata.types.write_buffer_size

        out["write_buffer_size"] = (
            capo_neptunedata.types.write_buffer_size.deserialize_json(
                data["writeBufferSize"]
            )
        )
    else:
        import typing

        out["write_buffer_size"] = typing.cast(
            "capo_neptunedata.types.write_buffer_size.WriteBufferSize", ""
        )
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("progressPercentage") is not None:
        out["progress_percentage"] = data["progressPercentage"]
    else:
        out["progress_percentage"] = 0
    if data.get("estimatedEndTime") is not None:
        import datetime

        out["estimated_end_time"] = datetime.datetime.fromisoformat(
            data["estimatedEndTime"].replace("Z", "+00:00")
        )
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out
