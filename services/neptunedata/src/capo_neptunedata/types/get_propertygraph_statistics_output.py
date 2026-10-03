"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetPropertygraphStatisticsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptunedata.types.statistics


class GetPropertygraphStatisticsOutput(TypedDict, closed=True):
    status: "str"
    """<p>The HTTP return code of the request. If the request succeeded, the code is 200. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-statistics.html#neptune-dfe-statistics-errors">Common error codes for DFE statistics request</a> for a list of common errors.</p>"""
    payload: "capo_neptunedata.types.statistics.Statistics"
    """<p>Statistics for property-graph data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertygraphStatisticsOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    import capo_neptunedata.types.statistics

    out["payload"] = capo_neptunedata.types.statistics.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> GetPropertygraphStatisticsOutput:
    out: GetPropertygraphStatisticsOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetPropertygraphStatisticsOutput.status required")
    if data.get("payload") is not None:
        import capo_neptunedata.types.statistics

        out["payload"] = capo_neptunedata.types.statistics.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("GetPropertygraphStatisticsOutput.payload required")
    return out
