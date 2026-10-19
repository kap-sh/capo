"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceChatterFeedConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_field_name
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.salesforce_chatter_feed_include_filter_types


class SalesforceChatterFeedConfiguration(TypedDict, closed=True):
    document_data_field_name: (
        "capo_kendra.types.data_source_field_name.DataSourceFieldName"
    )
    """<p>The name of the column in the Salesforce FeedItem table that contains the content to index. Typically this is the <code>Body</code> column.</p>"""
    document_title_field_name: NotRequired[
        "capo_kendra.types.data_source_field_name.DataSourceFieldName"
    ]
    """<p>The name of the column in the Salesforce FeedItem table that contains the title of the document. This is typically the <code>Title</code> column.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>Maps fields from a Salesforce chatter feed into Amazon Kendra index fields.</p>"""
    include_filter_types: NotRequired[
        "capo_kendra.types.salesforce_chatter_feed_include_filter_types.SalesforceChatterFeedIncludeFilterTypes"
    ]
    """<p>Filters the documents in the feed based on status of the user. When you specify <code>ACTIVE_USERS</code> only documents from users who have an active account are indexed. When you specify <code>STANDARD_USER</code> only documents for Salesforce standard users are documented. You can specify both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceChatterFeedConfiguration) -> dict:
    out: dict = {}
    out["DocumentDataFieldName"] = value["document_data_field_name"]
    if "document_title_field_name" in value:
        out["DocumentTitleFieldName"] = value["document_title_field_name"]
    if "field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    if "include_filter_types" in value:
        import capo_kendra.types.salesforce_chatter_feed_include_filter_types

        out["IncludeFilterTypes"] = (
            capo_kendra.types.salesforce_chatter_feed_include_filter_types.serialize_aws_json_1_1(
                value["include_filter_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SalesforceChatterFeedConfiguration:
    out: SalesforceChatterFeedConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DocumentDataFieldName") is not None:
        out["document_data_field_name"] = data["DocumentDataFieldName"]
    else:
        out["document_data_field_name"] = ""
    if data.get("DocumentTitleFieldName") is not None:
        out["document_title_field_name"] = data["DocumentTitleFieldName"]
    if data.get("FieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    if data.get("IncludeFilterTypes") is not None:
        import capo_kendra.types.salesforce_chatter_feed_include_filter_types

        out["include_filter_types"] = (
            capo_kendra.types.salesforce_chatter_feed_include_filter_types.deserialize_aws_json_1_1(
                data["IncludeFilterTypes"]
            )
        )
    return out
