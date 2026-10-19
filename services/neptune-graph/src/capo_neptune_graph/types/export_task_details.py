"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportTaskDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class ExportTaskDetails(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start time of the export task.</p>"""
    time_elapsed_seconds: "int"
    """<p>The time elapsed, in seconds, since the start time of the export task.</p>"""
    progress_percentage: "int"
    """<p>The number of progress percentage of the export task.</p>"""
    num_vertices_written: NotRequired["int"]
    """<p>The number of exported vertices.</p>"""
    num_edges_written: NotRequired["int"]
    """<p>The number of exported edges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportTaskDetails) -> dict:
    out: dict = {}
    import capo_neptune_graph.types._prelude.timestamp

    out["startTime"] = capo_neptune_graph.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    out["timeElapsedSeconds"] = value["time_elapsed_seconds"]
    out["progressPercentage"] = value["progress_percentage"]
    if "num_vertices_written" in value:
        out["numVerticesWritten"] = value["num_vertices_written"]
    if "num_edges_written" in value:
        out["numEdgesWritten"] = value["num_edges_written"]
    return out


def deserialize_json(data: dict) -> ExportTaskDetails:
    out: ExportTaskDetails = {}  # type: ignore[typeddict-item]
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
    if data.get("numVerticesWritten") is not None:
        out["num_vertices_written"] = data["numVerticesWritten"]
    if data.get("numEdgesWritten") is not None:
        out["num_edges_written"] = data["numEdgesWritten"]
    return out
