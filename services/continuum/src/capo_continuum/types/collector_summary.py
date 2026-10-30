"""Generated from Smithy shape ``com.amazonaws.continuum#CollectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.collector_arn
    import capo_continuum.types.collector_id
    import capo_continuum.types.collector_status
    import capo_continuum.types.collector_type


class CollectorSummary(TypedDict, closed=True):
    collector_id: "capo_continuum.types.collector_id.CollectorId"
    """The unique identifier of the Collector."""
    collector_arn: "capo_continuum.types.collector_arn.CollectorArn"
    """The ARN of the Collector."""
    type: "capo_continuum.types.collector_type.CollectorType"
    """The source collected by this Collector."""
    status: "capo_continuum.types.collector_status.CollectorStatus"
    """The current lifecycle status."""
    created_at: "datetime.datetime"
    """The timestamp when the Collector was created."""


# --- restJson1 ser/de ---
def serialize_json(value: CollectorSummary) -> dict:
    out: dict = {}
    out["collectorId"] = value["collector_id"]
    out["collectorArn"] = value["collector_arn"]
    import capo_continuum.types.collector_type

    out["type"] = capo_continuum.types.collector_type.serialize_json(value["type"])
    import capo_continuum.types.collector_status

    out["status"] = capo_continuum.types.collector_status.serialize_json(
        value["status"]
    )
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CollectorSummary:
    out: CollectorSummary = {}  # type: ignore[typeddict-item]
    if data.get("collectorId") is not None:
        out["collector_id"] = data["collectorId"]
    else:
        out["collector_id"] = ""
    if data.get("collectorArn") is not None:
        out["collector_arn"] = data["collectorArn"]
    else:
        out["collector_arn"] = ""
    if data.get("type") is not None:
        import capo_continuum.types.collector_type

        out["type"] = capo_continuum.types.collector_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast(
            "capo_continuum.types.collector_type.CollectorType", ""
        )
    if data.get("status") is not None:
        import capo_continuum.types.collector_status

        out["status"] = capo_continuum.types.collector_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_continuum.types.collector_status.CollectorStatus", ""
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
