"""Generated from Smithy shape ``com.amazonaws.comprehend#ListDocumentClassifierSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_classifier_summaries_list
    import capo_comprehend.types.string


class ListDocumentClassifierSummariesResponse(TypedDict, closed=True):
    document_classifier_summaries_list: NotRequired[
        "capo_comprehend.types.document_classifier_summaries_list.DocumentClassifierSummariesList"
    ]
    """<p>The list of summaries of document classifiers.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentClassifierSummariesResponse) -> dict:
    out: dict = {}
    if "document_classifier_summaries_list" in value:
        import capo_comprehend.types.document_classifier_summaries_list

        out["DocumentClassifierSummariesList"] = (
            capo_comprehend.types.document_classifier_summaries_list.serialize_aws_json_1_1(
                value["document_classifier_summaries_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentClassifierSummariesResponse:
    out: ListDocumentClassifierSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierSummariesList") is not None:
        import capo_comprehend.types.document_classifier_summaries_list

        out["document_classifier_summaries_list"] = (
            capo_comprehend.types.document_classifier_summaries_list.deserialize_aws_json_1_1(
                data["DocumentClassifierSummariesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDocumentClassifierSummariesResponse) -> dict:
    out: dict = {}
    if "document_classifier_summaries_list" in value:
        import capo_comprehend.types.document_classifier_summaries_list

        out["DocumentClassifierSummariesList"] = (
            capo_comprehend.types.document_classifier_summaries_list.serialize_cbor(
                value["document_classifier_summaries_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDocumentClassifierSummariesResponse:
    out: ListDocumentClassifierSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierSummariesList") is not None:
        import capo_comprehend.types.document_classifier_summaries_list

        out["document_classifier_summaries_list"] = (
            capo_comprehend.types.document_classifier_summaries_list.deserialize_cbor(
                data["DocumentClassifierSummariesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
