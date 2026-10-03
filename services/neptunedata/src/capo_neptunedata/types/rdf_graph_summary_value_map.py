"""Generated from Smithy shape ``com.amazonaws.neptunedata#RDFGraphSummaryValueMap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_neptunedata.types.rdf_graph_summary


class RDFGraphSummaryValueMap(TypedDict, closed=True):
    version: NotRequired["str"]
    """<p>The version of this graph summary response.</p>"""
    last_statistics_computation_time: NotRequired["datetime.datetime"]
    """<p>The timestamp, in ISO 8601 format, of the time at which Neptune last computed statistics.</p>"""
    graph_summary: NotRequired[
        "capo_neptunedata.types.rdf_graph_summary.RDFGraphSummary"
    ]
    """<p>The graph summary of an RDF graph. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-graph-summary.html#neptune-graph-summary-rdf-response">Graph summary response for an RDF graph</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RDFGraphSummaryValueMap) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "last_statistics_computation_time" in value:
        import capo_neptunedata._protocol.serialize

        out["lastStatisticsComputationTime"] = (
            capo_neptunedata._protocol.serialize.fmt_date_time(
                value["last_statistics_computation_time"]
            )
        )
    if "graph_summary" in value:
        import capo_neptunedata.types.rdf_graph_summary

        out["graphSummary"] = capo_neptunedata.types.rdf_graph_summary.serialize_json(
            value["graph_summary"]
        )
    return out


def deserialize_json(data: dict) -> RDFGraphSummaryValueMap:
    out: RDFGraphSummaryValueMap = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("lastStatisticsComputationTime") is not None:
        import datetime

        out["last_statistics_computation_time"] = datetime.datetime.fromisoformat(
            data["lastStatisticsComputationTime"].replace("Z", "+00:00")
        )
    if data.get("graphSummary") is not None:
        import capo_neptunedata.types.rdf_graph_summary

        out["graph_summary"] = (
            capo_neptunedata.types.rdf_graph_summary.deserialize_json(
                data["graphSummary"]
            )
        )
    return out
