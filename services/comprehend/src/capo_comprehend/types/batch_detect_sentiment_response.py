"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectSentimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.batch_item_error_list
    import capo_comprehend.types.list_of_detect_sentiment_result


class BatchDetectSentimentResponse(TypedDict, closed=True):
    result_list: "capo_comprehend.types.list_of_detect_sentiment_result.ListOfDetectSentimentResult"
    """<p>A list of objects containing the results of the operation. The results are sorted in ascending order by the <code>Index</code> field and match the order of the documents in the input list. If all of the documents contain an error, the <code>ResultList</code> is empty.</p>"""
    error_list: "capo_comprehend.types.batch_item_error_list.BatchItemErrorList"
    """<p>A list containing one object for each document that contained an error. The results are sorted in ascending order by the <code>Index</code> field and match the order of the documents in the input list. If there are no errors in the batch, the <code>ErrorList</code> is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectSentimentResponse) -> dict:
    out: dict = {}
    import capo_comprehend.types.list_of_detect_sentiment_result

    out["ResultList"] = (
        capo_comprehend.types.list_of_detect_sentiment_result.serialize_aws_json_1_1(
            value["result_list"]
        )
    )
    import capo_comprehend.types.batch_item_error_list

    out["ErrorList"] = (
        capo_comprehend.types.batch_item_error_list.serialize_aws_json_1_1(
            value["error_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectSentimentResponse:
    out: BatchDetectSentimentResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResultList") is not None:
        import capo_comprehend.types.list_of_detect_sentiment_result

        out["result_list"] = (
            capo_comprehend.types.list_of_detect_sentiment_result.deserialize_aws_json_1_1(
                data["ResultList"]
            )
        )
    else:
        out["result_list"] = []
    if data.get("ErrorList") is not None:
        import capo_comprehend.types.batch_item_error_list

        out["error_list"] = (
            capo_comprehend.types.batch_item_error_list.deserialize_aws_json_1_1(
                data["ErrorList"]
            )
        )
    else:
        out["error_list"] = []
    return out
