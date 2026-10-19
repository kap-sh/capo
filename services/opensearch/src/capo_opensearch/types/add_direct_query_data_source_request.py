"""Generated from Smithy shape ``com.amazonaws.opensearch#AddDirectQueryDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.direct_query_data_source_description
    import capo_opensearch.types.direct_query_data_source_name
    import capo_opensearch.types.direct_query_data_source_type
    import capo_opensearch.types.direct_query_open_search_arn_list
    import capo_opensearch.types.policy_document
    import capo_opensearch.types.tag_list


class AddDirectQueryDataSourceRequest(TypedDict, closed=True):
    data_source_name: (
        "capo_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName"
    )
    """<p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>"""
    data_source_type: (
        "capo_opensearch.types.direct_query_data_source_type.DirectQueryDataSourceType"
    )
    """<p> The supported Amazon Web Services service that you want to use as the source for direct queries in OpenSearch Service. </p>"""
    description: NotRequired[
        "capo_opensearch.types.direct_query_data_source_description.DirectQueryDataSourceDescription"
    ]
    """<p> An optional text field for providing additional context and details about the data source. </p>"""
    open_search_arns: NotRequired[
        "capo_opensearch.types.direct_query_open_search_arn_list.DirectQueryOpenSearchARNList"
    ]
    """<p> An optional list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source. This field is required for CloudWatchLogs and SecurityLake datasource types. </p>"""
    data_source_access_policy: NotRequired[
        "capo_opensearch.types.policy_document.PolicyDocument"
    ]
    """<p> An optional IAM access policy document that defines the permissions for accessing the data source. The policy document must be in valid JSON format and follow IAM policy syntax.</p>"""
    tag_list: NotRequired["capo_opensearch.types.tag_list.TagList"]


# --- restJson1 ser/de ---
def serialize_json(value: AddDirectQueryDataSourceRequest) -> dict:
    out: dict = {}
    out["DataSourceName"] = value["data_source_name"]
    import capo_opensearch.types.direct_query_data_source_type

    out["DataSourceType"] = (
        capo_opensearch.types.direct_query_data_source_type.serialize_json(
            value["data_source_type"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "open_search_arns" in value:
        import capo_opensearch.types.direct_query_open_search_arn_list

        out["OpenSearchArns"] = (
            capo_opensearch.types.direct_query_open_search_arn_list.serialize_json(
                value["open_search_arns"]
            )
        )
    if "data_source_access_policy" in value:
        out["DataSourceAccessPolicy"] = value["data_source_access_policy"]
    if "tag_list" in value:
        import capo_opensearch.types.tag_list

        out["TagList"] = capo_opensearch.types.tag_list.serialize_json(
            value["tag_list"]
        )
    return out


def deserialize_json(data: dict) -> AddDirectQueryDataSourceRequest:
    out: AddDirectQueryDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceName") is not None:
        out["data_source_name"] = data["DataSourceName"]
    else:
        out["data_source_name"] = ""
    if data.get("DataSourceType") is not None:
        import capo_opensearch.types.direct_query_data_source_type

        out["data_source_type"] = (
            capo_opensearch.types.direct_query_data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    else:
        import capo_opensearch.types._unknown

        out["data_source_type"] = capo_opensearch.types._unknown.UnknownUnionMember("")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("OpenSearchArns") is not None:
        import capo_opensearch.types.direct_query_open_search_arn_list

        out["open_search_arns"] = (
            capo_opensearch.types.direct_query_open_search_arn_list.deserialize_json(
                data["OpenSearchArns"]
            )
        )
    if data.get("DataSourceAccessPolicy") is not None:
        out["data_source_access_policy"] = data["DataSourceAccessPolicy"]
    if data.get("TagList") is not None:
        import capo_opensearch.types.tag_list

        out["tag_list"] = capo_opensearch.types.tag_list.deserialize_json(
            data["TagList"]
        )
    return out
