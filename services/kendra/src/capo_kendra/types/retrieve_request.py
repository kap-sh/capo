"""Generated from Smithy shape ``com.amazonaws.kendra#RetrieveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.attribute_filter
    import capo_kendra.types.document_attribute_key_list
    import capo_kendra.types.document_relevance_override_configuration_list
    import capo_kendra.types.index_id
    import capo_kendra.types.integer
    import capo_kendra.types.query_text
    import capo_kendra.types.user_context


class RetrieveRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index to retrieve relevant passages for the search.</p>"""
    query_text: "capo_kendra.types.query_text.QueryText"
    """<p>The input query text to retrieve relevant passages for the search. Amazon Kendra truncates queries at 30 token words, which excludes punctuation and stop words. Truncation still applies if you use Boolean or more advanced, complex queries. For example, <code>Timeoff AND October AND Category:HR</code> is counted as 3 tokens: <code>timeoff</code>, <code>october</code>, <code>hr</code>. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax">Searching with advanced query syntax</a> in the Amazon Kendra Developer Guide. </p>"""
    attribute_filter: NotRequired["capo_kendra.types.attribute_filter.AttributeFilter"]
    """<p>Filters search results by document fields/attributes. You can only provide one attribute filter; however, the <code>AndAllFilters</code>, <code>NotFilter</code>, and <code>OrAllFilters</code> parameters contain a list of other filters.</p> <p>The <code>AttributeFilter</code> parameter means you can create a set of filtering rules that a document must satisfy to be included in the query results.</p> <note> <p>For Amazon Kendra Gen AI Enterprise Edition indices use <code>AttributeFilter</code> to enable document filtering for end users using <code>_email_id</code> or include public documents (<code>_email_id=null</code>).</p> </note>"""
    requested_document_attributes: NotRequired[
        "capo_kendra.types.document_attribute_key_list.DocumentAttributeKeyList"
    ]
    """<p>A list of document fields/attributes to include in the response. You can limit the response to include certain document fields. By default, all document fields are included in the response.</p>"""
    document_relevance_override_configurations: NotRequired[
        "capo_kendra.types.document_relevance_override_configuration_list.DocumentRelevanceOverrideConfigurationList"
    ]
    """<p>Overrides relevance tuning configurations of fields/attributes set at the index level.</p> <p>If you use this API to override the relevance tuning configured at the index level, but there is no relevance tuning configured at the index level, then Amazon Kendra does not apply any relevance tuning.</p> <p>If there is relevance tuning configured for fields at the index level, and you use this API to override only some of these fields, then for the fields you did not override, the importance is set to 1.</p>"""
    page_number: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>Retrieved relevant passages are returned in pages the size of the <code>PageSize</code> parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.</p>"""
    page_size: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>Sets the number of retrieved relevant passages that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.</p>"""
    user_context: NotRequired["capo_kendra.types.user_context.UserContext"]
    """<p>The user context token or user and group information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetrieveRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["QueryText"] = value["query_text"]
    if "attribute_filter" in value:
        import capo_kendra.types.attribute_filter

        out["AttributeFilter"] = (
            capo_kendra.types.attribute_filter.serialize_aws_json_1_1(
                value["attribute_filter"]
            )
        )
    if "requested_document_attributes" in value:
        import capo_kendra.types.document_attribute_key_list

        out["RequestedDocumentAttributes"] = (
            capo_kendra.types.document_attribute_key_list.serialize_aws_json_1_1(
                value["requested_document_attributes"]
            )
        )
    if "document_relevance_override_configurations" in value:
        import capo_kendra.types.document_relevance_override_configuration_list

        out["DocumentRelevanceOverrideConfigurations"] = (
            capo_kendra.types.document_relevance_override_configuration_list.serialize_aws_json_1_1(
                value["document_relevance_override_configurations"]
            )
        )
    if "page_number" in value:
        out["PageNumber"] = value["page_number"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "user_context" in value:
        import capo_kendra.types.user_context

        out["UserContext"] = capo_kendra.types.user_context.serialize_aws_json_1_1(
            value["user_context"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetrieveRequest:
    out: RetrieveRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("RetrieveRequest.index_id required")
    if data.get("QueryText") is not None:
        out["query_text"] = data["QueryText"]
    else:
        raise DeserializationError("RetrieveRequest.query_text required")
    if data.get("AttributeFilter") is not None:
        import capo_kendra.types.attribute_filter

        out["attribute_filter"] = (
            capo_kendra.types.attribute_filter.deserialize_aws_json_1_1(
                data["AttributeFilter"]
            )
        )
    if data.get("RequestedDocumentAttributes") is not None:
        import capo_kendra.types.document_attribute_key_list

        out["requested_document_attributes"] = (
            capo_kendra.types.document_attribute_key_list.deserialize_aws_json_1_1(
                data["RequestedDocumentAttributes"]
            )
        )
    if data.get("DocumentRelevanceOverrideConfigurations") is not None:
        import capo_kendra.types.document_relevance_override_configuration_list

        out["document_relevance_override_configurations"] = (
            capo_kendra.types.document_relevance_override_configuration_list.deserialize_aws_json_1_1(
                data["DocumentRelevanceOverrideConfigurations"]
            )
        )
    if data.get("PageNumber") is not None:
        out["page_number"] = data["PageNumber"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("UserContext") is not None:
        import capo_kendra.types.user_context

        out["user_context"] = capo_kendra.types.user_context.deserialize_aws_json_1_1(
            data["UserContext"]
        )
    return out
