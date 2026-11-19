"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEntityRecognizerSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entity_recognizer_summaries_list
    import capo_comprehend.types.string


class ListEntityRecognizerSummariesResponse(TypedDict, closed=True):
    entity_recognizer_summaries_list: NotRequired[
        "capo_comprehend.types.entity_recognizer_summaries_list.EntityRecognizerSummariesList"
    ]
    """<p>The list entity recognizer summaries.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntityRecognizerSummariesResponse) -> dict:
    out: dict = {}
    if "entity_recognizer_summaries_list" in value:
        import capo_comprehend.types.entity_recognizer_summaries_list

        out["EntityRecognizerSummariesList"] = (
            capo_comprehend.types.entity_recognizer_summaries_list.serialize_aws_json_1_1(
                value["entity_recognizer_summaries_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntityRecognizerSummariesResponse:
    out: ListEntityRecognizerSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntityRecognizerSummariesList") is not None:
        import capo_comprehend.types.entity_recognizer_summaries_list

        out["entity_recognizer_summaries_list"] = (
            capo_comprehend.types.entity_recognizer_summaries_list.deserialize_aws_json_1_1(
                data["EntityRecognizerSummariesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEntityRecognizerSummariesResponse) -> dict:
    out: dict = {}
    if "entity_recognizer_summaries_list" in value:
        import capo_comprehend.types.entity_recognizer_summaries_list

        out["EntityRecognizerSummariesList"] = (
            capo_comprehend.types.entity_recognizer_summaries_list.serialize_cbor(
                value["entity_recognizer_summaries_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListEntityRecognizerSummariesResponse:
    out: ListEntityRecognizerSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntityRecognizerSummariesList") is not None:
        import capo_comprehend.types.entity_recognizer_summaries_list

        out["entity_recognizer_summaries_list"] = (
            capo_comprehend.types.entity_recognizer_summaries_list.deserialize_cbor(
                data["EntityRecognizerSummariesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
