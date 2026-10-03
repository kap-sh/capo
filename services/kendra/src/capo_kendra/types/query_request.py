"""Generated from Smithy shape ``com.amazonaws.kendra#QueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.attribute_filter
    import capo_kendra.types.collapse_configuration
    import capo_kendra.types.document_attribute_key_list
    import capo_kendra.types.document_relevance_override_configuration_list
    import capo_kendra.types.facet_list
    import capo_kendra.types.index_id
    import capo_kendra.types.integer
    import capo_kendra.types.query_result_type
    import capo_kendra.types.query_text
    import capo_kendra.types.sorting_configuration
    import capo_kendra.types.sorting_configuration_list
    import capo_kendra.types.spell_correction_configuration
    import capo_kendra.types.user_context
    import capo_kendra.types.visitor_id


class QueryRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the search.</p>"""
    query_text: NotRequired["capo_kendra.types.query_text.QueryText"]
    """<p>The input query text for the search. Amazon Kendra truncates queries at 30 token words, which excludes punctuation and stop words. Truncation still applies if you use Boolean or more advanced, complex queries. For example, <code>Timeoff AND October AND Category:HR</code> is counted as 3 tokens: <code>timeoff</code>, <code>october</code>, <code>hr</code>. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax">Searching with advanced query syntax</a> in the Amazon Kendra Developer Guide. </p>"""
    attribute_filter: NotRequired["capo_kendra.types.attribute_filter.AttributeFilter"]
    """<p>Filters search results by document fields/attributes. You can only provide one attribute filter; however, the <code>AndAllFilters</code>, <code>NotFilter</code>, and <code>OrAllFilters</code> parameters contain a list of other filters.</p> <p>The <code>AttributeFilter</code> parameter means you can create a set of filtering rules that a document must satisfy to be included in the query results.</p> <note> <p>For Amazon Kendra Gen AI Enterprise Edition indices use <code>AttributeFilter</code> to enable document filtering for end users using <code>_email_id</code> or include public documents (<code>_email_id=null</code>).</p> </note>"""
    facets: NotRequired["capo_kendra.types.facet_list.FacetList"]
    """<p>An array of documents fields/attributes for faceted search. Amazon Kendra returns a count for each field key specified. This helps your users narrow their search.</p>"""
    requested_document_attributes: NotRequired[
        "capo_kendra.types.document_attribute_key_list.DocumentAttributeKeyList"
    ]
    """<p>An array of document fields/attributes to include in the response. You can limit the response to include certain document fields. By default, all document attributes are included in the response.</p>"""
    query_result_type_filter: NotRequired[
        "capo_kendra.types.query_result_type.QueryResultType"
    ]
    """<p>Sets the type of query result or response. Only results for the specified type are returned.</p>"""
    document_relevance_override_configurations: NotRequired[
        "capo_kendra.types.document_relevance_override_configuration_list.DocumentRelevanceOverrideConfigurationList"
    ]
    """<p>Overrides relevance tuning configurations of fields/attributes set at the index level.</p> <p>If you use this API to override the relevance tuning configured at the index level, but there is no relevance tuning configured at the index level, then Amazon Kendra does not apply any relevance tuning.</p> <p>If there is relevance tuning configured for fields at the index level, and you use this API to override only some of these fields, then for the fields you did not override, the importance is set to 1.</p>"""
    page_number: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>Query results are returned in pages the size of the <code>PageSize</code> parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.</p>"""
    page_size: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>Sets the number of results that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.</p>"""
    sorting_configuration: NotRequired[
        "capo_kendra.types.sorting_configuration.SortingConfiguration"
    ]
    """<p>Provides information that determines how the results of the query are sorted. You can set the field that Amazon Kendra should sort the results on, and specify whether the results should be sorted in ascending or descending order. In the case of ties in sorting the results, the results are sorted by relevance.</p> <p>If you don't provide sorting configuration, the results are sorted by the relevance that Amazon Kendra determines for the result.</p>"""
    sorting_configurations: NotRequired[
        "capo_kendra.types.sorting_configuration_list.SortingConfigurationList"
    ]
    """<p>Provides configuration information to determine how the results of a query are sorted.</p> <p>You can set upto 3 fields that Amazon Kendra should sort the results on, and specify whether the results should be sorted in ascending or descending order. The sort field quota can be increased.</p> <p>If you don't provide a sorting configuration, the results are sorted by the relevance that Amazon Kendra determines for the result. In the case of ties in sorting the results, the results are sorted by relevance. </p>"""
    user_context: NotRequired["capo_kendra.types.user_context.UserContext"]
    """<p>The user context token or user and group information.</p>"""
    visitor_id: NotRequired["capo_kendra.types.visitor_id.VisitorId"]
    """<p>Provides an identifier for a specific user. The <code>VisitorId</code> should be a unique identifier, such as a GUID. Don't use personally identifiable information, such as the user's email address, as the <code>VisitorId</code>.</p>"""
    spell_correction_configuration: NotRequired[
        "capo_kendra.types.spell_correction_configuration.SpellCorrectionConfiguration"
    ]
    """<p>Enables suggested spell corrections for queries.</p>"""
    collapse_configuration: NotRequired[
        "capo_kendra.types.collapse_configuration.CollapseConfiguration"
    ]
    """<p>Provides configuration to determine how to group results by document attribute value, and how to display them (collapsed or expanded) under a designated primary document for each group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "query_text" in value:
        out["QueryText"] = value["query_text"]
    if "attribute_filter" in value:
        import capo_kendra.types.attribute_filter

        out["AttributeFilter"] = (
            capo_kendra.types.attribute_filter.serialize_aws_json_1_1(
                value["attribute_filter"]
            )
        )
    if "facets" in value:
        import capo_kendra.types.facet_list

        out["Facets"] = capo_kendra.types.facet_list.serialize_aws_json_1_1(
            value["facets"]
        )
    if "requested_document_attributes" in value:
        import capo_kendra.types.document_attribute_key_list

        out["RequestedDocumentAttributes"] = (
            capo_kendra.types.document_attribute_key_list.serialize_aws_json_1_1(
                value["requested_document_attributes"]
            )
        )
    if "query_result_type_filter" in value:
        import capo_kendra.types.query_result_type

        out["QueryResultTypeFilter"] = (
            capo_kendra.types.query_result_type.serialize_aws_json_1_1(
                value["query_result_type_filter"]
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
    if "sorting_configuration" in value:
        import capo_kendra.types.sorting_configuration

        out["SortingConfiguration"] = (
            capo_kendra.types.sorting_configuration.serialize_aws_json_1_1(
                value["sorting_configuration"]
            )
        )
    if "sorting_configurations" in value:
        import capo_kendra.types.sorting_configuration_list

        out["SortingConfigurations"] = (
            capo_kendra.types.sorting_configuration_list.serialize_aws_json_1_1(
                value["sorting_configurations"]
            )
        )
    if "user_context" in value:
        import capo_kendra.types.user_context

        out["UserContext"] = capo_kendra.types.user_context.serialize_aws_json_1_1(
            value["user_context"]
        )
    if "visitor_id" in value:
        out["VisitorId"] = value["visitor_id"]
    if "spell_correction_configuration" in value:
        import capo_kendra.types.spell_correction_configuration

        out["SpellCorrectionConfiguration"] = (
            capo_kendra.types.spell_correction_configuration.serialize_aws_json_1_1(
                value["spell_correction_configuration"]
            )
        )
    if "collapse_configuration" in value:
        import capo_kendra.types.collapse_configuration

        out["CollapseConfiguration"] = (
            capo_kendra.types.collapse_configuration.serialize_aws_json_1_1(
                value["collapse_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryRequest:
    out: QueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("QueryRequest.index_id required")
    if data.get("QueryText") is not None:
        out["query_text"] = data["QueryText"]
    if data.get("AttributeFilter") is not None:
        import capo_kendra.types.attribute_filter

        out["attribute_filter"] = (
            capo_kendra.types.attribute_filter.deserialize_aws_json_1_1(
                data["AttributeFilter"]
            )
        )
    if data.get("Facets") is not None:
        import capo_kendra.types.facet_list

        out["facets"] = capo_kendra.types.facet_list.deserialize_aws_json_1_1(
            data["Facets"]
        )
    if data.get("RequestedDocumentAttributes") is not None:
        import capo_kendra.types.document_attribute_key_list

        out["requested_document_attributes"] = (
            capo_kendra.types.document_attribute_key_list.deserialize_aws_json_1_1(
                data["RequestedDocumentAttributes"]
            )
        )
    if data.get("QueryResultTypeFilter") is not None:
        import capo_kendra.types.query_result_type

        out["query_result_type_filter"] = (
            capo_kendra.types.query_result_type.deserialize_aws_json_1_1(
                data["QueryResultTypeFilter"]
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
    if data.get("SortingConfiguration") is not None:
        import capo_kendra.types.sorting_configuration

        out["sorting_configuration"] = (
            capo_kendra.types.sorting_configuration.deserialize_aws_json_1_1(
                data["SortingConfiguration"]
            )
        )
    if data.get("SortingConfigurations") is not None:
        import capo_kendra.types.sorting_configuration_list

        out["sorting_configurations"] = (
            capo_kendra.types.sorting_configuration_list.deserialize_aws_json_1_1(
                data["SortingConfigurations"]
            )
        )
    if data.get("UserContext") is not None:
        import capo_kendra.types.user_context

        out["user_context"] = capo_kendra.types.user_context.deserialize_aws_json_1_1(
            data["UserContext"]
        )
    if data.get("VisitorId") is not None:
        out["visitor_id"] = data["VisitorId"]
    if data.get("SpellCorrectionConfiguration") is not None:
        import capo_kendra.types.spell_correction_configuration

        out["spell_correction_configuration"] = (
            capo_kendra.types.spell_correction_configuration.deserialize_aws_json_1_1(
                data["SpellCorrectionConfiguration"]
            )
        )
    if data.get("CollapseConfiguration") is not None:
        import capo_kendra.types.collapse_configuration

        out["collapse_configuration"] = (
            capo_kendra.types.collapse_configuration.deserialize_aws_json_1_1(
                data["CollapseConfiguration"]
            )
        )
    return out
