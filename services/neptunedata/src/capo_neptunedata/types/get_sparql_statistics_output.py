"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetSparqlStatisticsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptunedata.types.statistics


class GetSparqlStatisticsOutput(TypedDict, closed=True):
    status: "str"
    """<p>The HTTP return code of the request. If the request succeeded, the code is 200. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-statistics.html#neptune-dfe-statistics-errors">Common error codes for DFE statistics request</a> for a list of common errors.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstatisticsstatus">neptune-db:GetStatisticsStatus</a> IAM action in that cluster.</p>"""
    payload: "capo_neptunedata.types.statistics.Statistics"
    """<p>Statistics for RDF data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSparqlStatisticsOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    import capo_neptunedata.types.statistics

    out["payload"] = capo_neptunedata.types.statistics.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> GetSparqlStatisticsOutput:
    out: GetSparqlStatisticsOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetSparqlStatisticsOutput.status required")
    if data.get("payload") is not None:
        import capo_neptunedata.types.statistics

        out["payload"] = capo_neptunedata.types.statistics.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("GetSparqlStatisticsOutput.payload required")
    return out
