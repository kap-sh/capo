"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.additional_result_attribute_list
    import capo_kendra.types.document_attribute_list
    import capo_kendra.types.document_id
    import capo_kendra.types.feedback_token
    import capo_kendra.types.query_result_type
    import capo_kendra.types.result_id
    import capo_kendra.types.text_with_highlights
    import capo_kendra.types.url


class FeaturedResultsItem(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.result_id.ResultId"]
    """<p>The identifier of the featured result.</p>"""
    type: NotRequired["capo_kendra.types.query_result_type.QueryResultType"]
    """<p>The type of document within the featured result response. For example, a response could include a question-answer type that's relevant to the query.</p>"""
    additional_attributes: NotRequired[
        "capo_kendra.types.additional_result_attribute_list.AdditionalResultAttributeList"
    ]
    """<p>One or more additional attributes associated with the featured result.</p>"""
    document_id: NotRequired["capo_kendra.types.document_id.DocumentId"]
    """<p>The identifier of the featured document.</p>"""
    document_title: NotRequired[
        "capo_kendra.types.text_with_highlights.TextWithHighlights"
    ]
    document_excerpt: NotRequired[
        "capo_kendra.types.text_with_highlights.TextWithHighlights"
    ]
    document_uri: NotRequired["capo_kendra.types.url.Url"]
    """<p>The source URI location of the featured document.</p>"""
    document_attributes: NotRequired[
        "capo_kendra.types.document_attribute_list.DocumentAttributeList"
    ]
    """<p>An array of document attributes assigned to a featured document in the search results. For example, the document author (<code>_author</code>) or the source URI (<code>_source_uri</code>) of the document.</p>"""
    feedback_token: NotRequired["capo_kendra.types.feedback_token.FeedbackToken"]
    """<p>A token that identifies a particular featured result from a particular query. Use this token to provide click-through feedback for the result. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/submitting-feedback.html">Submitting feedback</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_kendra.types.query_result_type

        out["Type"] = capo_kendra.types.query_result_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "additional_attributes" in value:
        import capo_kendra.types.additional_result_attribute_list

        out["AdditionalAttributes"] = (
            capo_kendra.types.additional_result_attribute_list.serialize_aws_json_1_1(
                value["additional_attributes"]
            )
        )
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "document_title" in value:
        import capo_kendra.types.text_with_highlights

        out["DocumentTitle"] = (
            capo_kendra.types.text_with_highlights.serialize_aws_json_1_1(
                value["document_title"]
            )
        )
    if "document_excerpt" in value:
        import capo_kendra.types.text_with_highlights

        out["DocumentExcerpt"] = (
            capo_kendra.types.text_with_highlights.serialize_aws_json_1_1(
                value["document_excerpt"]
            )
        )
    if "document_uri" in value:
        out["DocumentURI"] = value["document_uri"]
    if "document_attributes" in value:
        import capo_kendra.types.document_attribute_list

        out["DocumentAttributes"] = (
            capo_kendra.types.document_attribute_list.serialize_aws_json_1_1(
                value["document_attributes"]
            )
        )
    if "feedback_token" in value:
        out["FeedbackToken"] = value["feedback_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturedResultsItem:
    out: FeaturedResultsItem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_kendra.types.query_result_type

        out["type"] = capo_kendra.types.query_result_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("AdditionalAttributes") is not None:
        import capo_kendra.types.additional_result_attribute_list

        out["additional_attributes"] = (
            capo_kendra.types.additional_result_attribute_list.deserialize_aws_json_1_1(
                data["AdditionalAttributes"]
            )
        )
    if data.get("DocumentId") is not None:
        out["document_id"] = data["DocumentId"]
    if data.get("DocumentTitle") is not None:
        import capo_kendra.types.text_with_highlights

        out["document_title"] = (
            capo_kendra.types.text_with_highlights.deserialize_aws_json_1_1(
                data["DocumentTitle"]
            )
        )
    if data.get("DocumentExcerpt") is not None:
        import capo_kendra.types.text_with_highlights

        out["document_excerpt"] = (
            capo_kendra.types.text_with_highlights.deserialize_aws_json_1_1(
                data["DocumentExcerpt"]
            )
        )
    if data.get("DocumentURI") is not None:
        out["document_uri"] = data["DocumentURI"]
    if data.get("DocumentAttributes") is not None:
        import capo_kendra.types.document_attribute_list

        out["document_attributes"] = (
            capo_kendra.types.document_attribute_list.deserialize_aws_json_1_1(
                data["DocumentAttributes"]
            )
        )
    if data.get("FeedbackToken") is not None:
        out["feedback_token"] = data["FeedbackToken"]
    return out
