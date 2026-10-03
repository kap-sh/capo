"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.ingestion_type
    import capo_quicksight.types.refresh_frequency
    import capo_quicksight.types.string
    import capo_quicksight.types.timestamp


class RefreshSchedule(TypedDict, closed=True):
    schedule_id: "capo_quicksight.types.string.String"
    """<p>An identifier for the refresh schedule.</p>"""
    schedule_frequency: "capo_quicksight.types.refresh_frequency.RefreshFrequency"
    """<p>The frequency for the refresh schedule.</p>"""
    start_after_date_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>Time after which the refresh schedule can be started, expressed in <code>YYYY-MM-DDTHH:MM:SS</code> format.</p>"""
    refresh_type: "capo_quicksight.types.ingestion_type.IngestionType"
    """<p>The type of refresh that a datset undergoes. Valid values are as follows:</p> <ul> <li> <p> <code>FULL_REFRESH</code>: A complete refresh of a dataset.</p> </li> <li> <p> <code>INCREMENTAL_REFRESH</code>: A partial refresh of some rows of a dataset, based on the time window specified.</p> </li> </ul> <p>For more information on full and incremental refreshes, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html">Refreshing SPICE data</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the refresh schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshSchedule) -> dict:
    out: dict = {}
    out["ScheduleId"] = value["schedule_id"]
    import capo_quicksight.types.refresh_frequency

    out["ScheduleFrequency"] = capo_quicksight.types.refresh_frequency.serialize_json(
        value["schedule_frequency"]
    )
    if "start_after_date_time" in value:
        import capo_quicksight.types.timestamp

        out["StartAfterDateTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["start_after_date_time"]
        )
    import capo_quicksight.types.ingestion_type

    out["RefreshType"] = capo_quicksight.types.ingestion_type.serialize_json(
        value["refresh_type"]
    )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> RefreshSchedule:
    out: RefreshSchedule = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleId") is not None:
        out["schedule_id"] = data["ScheduleId"]
    else:
        raise DeserializationError("RefreshSchedule.schedule_id required")
    if data.get("ScheduleFrequency") is not None:
        import capo_quicksight.types.refresh_frequency

        out["schedule_frequency"] = (
            capo_quicksight.types.refresh_frequency.deserialize_json(
                data["ScheduleFrequency"]
            )
        )
    else:
        raise DeserializationError("RefreshSchedule.schedule_frequency required")
    if data.get("StartAfterDateTime") is not None:
        import capo_quicksight.types.timestamp

        out["start_after_date_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["StartAfterDateTime"]
        )
    if data.get("RefreshType") is not None:
        import capo_quicksight.types.ingestion_type

        out["refresh_type"] = capo_quicksight.types.ingestion_type.deserialize_json(
            data["RefreshType"]
        )
    else:
        raise DeserializationError("RefreshSchedule.refresh_type required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
