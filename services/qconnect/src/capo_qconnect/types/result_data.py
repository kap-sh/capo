"""Generated from Smithy shape ``com.amazonaws.qconnect#ResultData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.data_summary
    import capo_qconnect.types.document
    import capo_qconnect.types.query_result_type
    import capo_qconnect.types.relevance_score
    import capo_qconnect.types.uuid


class ResultData(TypedDict, closed=True):
    result_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the result data.</p>"""
    document: NotRequired["capo_qconnect.types.document.Document"]
    """<p>The document.</p>"""
    relevance_score: "capo_qconnect.types.relevance_score.RelevanceScore"
    """<p>The relevance score of the results.</p>"""
    data: NotRequired["capo_qconnect.types.data_summary.DataSummary"]
    """<p> Summary of the recommended content.</p>"""
    type: NotRequired["capo_qconnect.types.query_result_type.QueryResultType"]
    """<p>The type of the query result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultData) -> dict:
    out: dict = {}
    out["resultId"] = value["result_id"]
    if "document" in value:
        import capo_qconnect.types.document

        out["document"] = capo_qconnect.types.document.serialize_json(value["document"])
    out["relevanceScore"] = (
        "NaN"
        if value.get("relevance_score", 0) != value.get("relevance_score", 0)
        else "Infinity"
        if value.get("relevance_score", 0) == float("inf")
        else "-Infinity"
        if value.get("relevance_score", 0) == float("-inf")
        else value.get("relevance_score", 0)
    )
    if "data" in value:
        import capo_qconnect.types.data_summary

        out["data"] = capo_qconnect.types.data_summary.serialize_json(value["data"])
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ResultData:
    out: ResultData = {}  # type: ignore[typeddict-item]
    if data.get("resultId") is not None:
        out["result_id"] = data["resultId"]
    else:
        raise DeserializationError("ResultData.result_id required")
    if data.get("document") is not None:
        import capo_qconnect.types.document

        out["document"] = capo_qconnect.types.document.deserialize_json(
            data["document"]
        )
    if data.get("relevanceScore") is not None:
        out["relevance_score"] = float(data["relevanceScore"])
    else:
        out["relevance_score"] = 0
    if data.get("data") is not None:
        import capo_qconnect.types.data_summary

        out["data"] = capo_qconnect.types.data_summary.deserialize_json(data["data"])
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out


def redact_sensitive(value: ResultData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document" in value:
        import capo_qconnect.types.document

        out["document"] = capo_qconnect.types.document.redact_sensitive(
            value["document"]
        )
    if "data" in value:
        import capo_qconnect.types.data_summary

        out["data"] = capo_qconnect.types.data_summary.redact_sensitive(value["data"])
    return out
