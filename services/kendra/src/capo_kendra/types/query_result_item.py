"""Generated from Smithy shape ``com.amazonaws.kendra#QueryResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.additional_result_attribute_list
    import capo_kendra.types.collapsed_result_detail
    import capo_kendra.types.document_attribute_list
    import capo_kendra.types.document_id
    import capo_kendra.types.feedback_token
    import capo_kendra.types.query_result_format
    import capo_kendra.types.query_result_type
    import capo_kendra.types.result_id
    import capo_kendra.types.score_attributes
    import capo_kendra.types.table_excerpt
    import capo_kendra.types.text_with_highlights
    import capo_kendra.types.url


class QueryResultItem(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.result_id.ResultId"]
    """<p>The unique identifier for the query result item id (<code>Id</code>) and the query result item document id (<code>DocumentId</code>) combined. The value of this field changes with every request, even when you have the same documents.</p>"""
    type: NotRequired["capo_kendra.types.query_result_type.QueryResultType"]
    """<p>The type of document within the response. For example, a response could include a question-answer that's relevant to the query.</p>"""
    format: NotRequired["capo_kendra.types.query_result_format.QueryResultFormat"]
    """<p>If the <code>Type</code> of document within the response is <code>ANSWER</code>, then it is either a <code>TABLE</code> answer or <code>TEXT</code> answer. If it's a table answer, a table excerpt is returned in <code>TableExcerpt</code>. If it's a text answer, a text excerpt is returned in <code>DocumentExcerpt</code>.</p>"""
    additional_attributes: NotRequired[
        "capo_kendra.types.additional_result_attribute_list.AdditionalResultAttributeList"
    ]
    """<p>One or more additional fields/attributes associated with the query result.</p>"""
    document_id: NotRequired["capo_kendra.types.document_id.DocumentId"]
    """<p>The identifier for the document.</p>"""
    document_title: NotRequired[
        "capo_kendra.types.text_with_highlights.TextWithHighlights"
    ]
    """<p>The title of the document. Contains the text of the title and information for highlighting the relevant terms in the title.</p>"""
    document_excerpt: NotRequired[
        "capo_kendra.types.text_with_highlights.TextWithHighlights"
    ]
    """<p>An extract of the text in the document. Contains information about highlighting the relevant terms in the excerpt.</p>"""
    document_uri: NotRequired["capo_kendra.types.url.Url"]
    """<p>The URI of the original location of the document.</p>"""
    document_attributes: NotRequired[
        "capo_kendra.types.document_attribute_list.DocumentAttributeList"
    ]
    """<p>An array of document fields/attributes assigned to a document in the search results. For example, the document author (<code>_author</code>) or the source URI (<code>_source_uri</code>) of the document.</p>"""
    score_attributes: NotRequired["capo_kendra.types.score_attributes.ScoreAttributes"]
    """<p>Indicates the confidence level of Amazon Kendra providing a relevant result for the query. Each result is placed into a bin that indicates the confidence, <code>VERY_HIGH</code>, <code>HIGH</code>, <code>MEDIUM</code> and <code>LOW</code>. You can use the score to determine if a response meets the confidence needed for your application.</p> <p>The field is only set to <code>LOW</code> when the <code>Type</code> field is set to <code>DOCUMENT</code> and Amazon Kendra is not confident that the result is relevant to the query.</p>"""
    feedback_token: NotRequired["capo_kendra.types.feedback_token.FeedbackToken"]
    """<p>A token that identifies a particular result from a particular query. Use this token to provide click-through feedback for the result. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/submitting-feedback.html">Submitting feedback</a>.</p>"""
    table_excerpt: NotRequired["capo_kendra.types.table_excerpt.TableExcerpt"]
    """<p>An excerpt from a table within a document.</p>"""
    collapsed_result_detail: NotRequired[
        "capo_kendra.types.collapsed_result_detail.CollapsedResultDetail"
    ]
    """<p>Provides details about a collapsed group of search results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResultItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_kendra.types.query_result_type

        out["Type"] = capo_kendra.types.query_result_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "format" in value:
        import capo_kendra.types.query_result_format

        out["Format"] = capo_kendra.types.query_result_format.serialize_aws_json_1_1(
            value["format"]
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
    if "score_attributes" in value:
        import capo_kendra.types.score_attributes

        out["ScoreAttributes"] = (
            capo_kendra.types.score_attributes.serialize_aws_json_1_1(
                value["score_attributes"]
            )
        )
    if "feedback_token" in value:
        out["FeedbackToken"] = value["feedback_token"]
    if "table_excerpt" in value:
        import capo_kendra.types.table_excerpt

        out["TableExcerpt"] = capo_kendra.types.table_excerpt.serialize_aws_json_1_1(
            value["table_excerpt"]
        )
    if "collapsed_result_detail" in value:
        import capo_kendra.types.collapsed_result_detail

        out["CollapsedResultDetail"] = (
            capo_kendra.types.collapsed_result_detail.serialize_aws_json_1_1(
                value["collapsed_result_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryResultItem:
    out: QueryResultItem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_kendra.types.query_result_type

        out["type"] = capo_kendra.types.query_result_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Format") is not None:
        import capo_kendra.types.query_result_format

        out["format"] = capo_kendra.types.query_result_format.deserialize_aws_json_1_1(
            data["Format"]
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
    if data.get("ScoreAttributes") is not None:
        import capo_kendra.types.score_attributes

        out["score_attributes"] = (
            capo_kendra.types.score_attributes.deserialize_aws_json_1_1(
                data["ScoreAttributes"]
            )
        )
    if data.get("FeedbackToken") is not None:
        out["feedback_token"] = data["FeedbackToken"]
    if data.get("TableExcerpt") is not None:
        import capo_kendra.types.table_excerpt

        out["table_excerpt"] = capo_kendra.types.table_excerpt.deserialize_aws_json_1_1(
            data["TableExcerpt"]
        )
    if data.get("CollapsedResultDetail") is not None:
        import capo_kendra.types.collapsed_result_detail

        out["collapsed_result_detail"] = (
            capo_kendra.types.collapsed_result_detail.deserialize_aws_json_1_1(
                data["CollapsedResultDetail"]
            )
        )
    return out
