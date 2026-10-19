"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ImportTaskDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class ImportTaskDetails(TypedDict, closed=True):
    status: "str"
    """<p>Status of the import task.</p>"""
    start_time: "datetime.datetime"
    """<p>Time at which the import task started.</p>"""
    time_elapsed_seconds: "int"
    """<p>Seconds elapsed since the import task started.</p>"""
    progress_percentage: "int"
    """<p>The percentage progress so far.</p>"""
    error_count: "int"
    """<p>The number of errors encountered so far.</p>"""
    error_details: NotRequired["str"]
    """<p>Details about the errors that have been encountered.</p>"""
    statement_count: "int"
    """<p>The number of statements in the import task.</p>"""
    dictionary_entry_count: "int"
    """<p>The number of dictionary entries in the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskDetails) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    import capo_neptune_graph.types._prelude.timestamp

    out["startTime"] = capo_neptune_graph.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    out["timeElapsedSeconds"] = value["time_elapsed_seconds"]
    out["progressPercentage"] = value["progress_percentage"]
    out["errorCount"] = value["error_count"]
    if "error_details" in value:
        out["errorDetails"] = value["error_details"]
    out["statementCount"] = value["statement_count"]
    out["dictionaryEntryCount"] = value["dictionary_entry_count"]
    return out


def deserialize_json(data: dict) -> ImportTaskDetails:
    out: ImportTaskDetails = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("startTime") is not None:
        import capo_neptune_graph.types._prelude.timestamp

        out["start_time"] = (
            capo_neptune_graph.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("timeElapsedSeconds") is not None:
        out["time_elapsed_seconds"] = data["timeElapsedSeconds"]
    else:
        out["time_elapsed_seconds"] = 0
    if data.get("progressPercentage") is not None:
        out["progress_percentage"] = data["progressPercentage"]
    else:
        out["progress_percentage"] = 0
    if data.get("errorCount") is not None:
        out["error_count"] = data["errorCount"]
    else:
        out["error_count"] = 0
    if data.get("errorDetails") is not None:
        out["error_details"] = data["errorDetails"]
    if data.get("statementCount") is not None:
        out["statement_count"] = data["statementCount"]
    else:
        out["statement_count"] = 0
    if data.get("dictionaryEntryCount") is not None:
        out["dictionary_entry_count"] = data["dictionaryEntryCount"]
    else:
        out["dictionary_entry_count"] = 0
    return out
