"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.rescore_id
    import capo_kendra_ranking.types.rescore_result_item_list


class RescoreResult(TypedDict, closed=True):
    rescore_id: NotRequired["capo_kendra_ranking.types.rescore_id.RescoreId"]
    """<p>The identifier associated with the scores that Amazon Kendra Intelligent Ranking gives to the results. Amazon Kendra Intelligent Ranking rescores or re-ranks the results for the search service.</p>"""
    result_items: NotRequired[
        "capo_kendra_ranking.types.rescore_result_item_list.RescoreResultItemList"
    ]
    """<p>A list of result items for documents with new relevancy scores. The results are in descending order.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreResult) -> dict:
    out: dict = {}
    if "rescore_id" in value:
        out["RescoreId"] = value["rescore_id"]
    if "result_items" in value:
        import capo_kendra_ranking.types.rescore_result_item_list

        out["ResultItems"] = (
            capo_kendra_ranking.types.rescore_result_item_list.serialize_aws_json_1_0(
                value["result_items"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RescoreResult:
    out: RescoreResult = {}  # type: ignore[typeddict-item]
    if data.get("RescoreId") is not None:
        out["rescore_id"] = data["RescoreId"]
    if data.get("ResultItems") is not None:
        import capo_kendra_ranking.types.rescore_result_item_list

        out["result_items"] = (
            capo_kendra_ranking.types.rescore_result_item_list.deserialize_aws_json_1_0(
                data["ResultItems"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RescoreResult) -> dict:
    out: dict = {}
    if "rescore_id" in value:
        out["RescoreId"] = value["rescore_id"]
    if "result_items" in value:
        import capo_kendra_ranking.types.rescore_result_item_list

        out["ResultItems"] = (
            capo_kendra_ranking.types.rescore_result_item_list.serialize_cbor(
                value["result_items"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RescoreResult:
    out: RescoreResult = {}  # type: ignore[typeddict-item]
    if data.get("RescoreId") is not None:
        out["rescore_id"] = data["RescoreId"]
    if data.get("ResultItems") is not None:
        import capo_kendra_ranking.types.rescore_result_item_list

        out["result_items"] = (
            capo_kendra_ranking.types.rescore_result_item_list.deserialize_cbor(
                data["ResultItems"]
            )
        )
    return out
