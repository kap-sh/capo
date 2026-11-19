"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.document_id
    import capo_kendra_ranking.types.float


class RescoreResultItem(TypedDict, closed=True):
    document_id: NotRequired["capo_kendra_ranking.types.document_id.DocumentId"]
    """<p>The identifier of the document from the search service.</p>"""
    score: NotRequired["capo_kendra_ranking.types.float.Float"]
    """<p>The relevancy score or rank that Amazon Kendra Intelligent Ranking gives to the result.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreResultItem) -> dict:
    out: dict = {}
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RescoreResultItem:
    out: RescoreResultItem = {}  # type: ignore[typeddict-item]
    if data.get("DocumentId") is not None:
        out["document_id"] = data["DocumentId"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RescoreResultItem) -> dict:
    out: dict = {}
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_cbor(data: dict) -> RescoreResultItem:
    out: RescoreResultItem = {}  # type: ignore[typeddict-item]
    if data.get("DocumentId") is not None:
        out["document_id"] = data["DocumentId"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out
