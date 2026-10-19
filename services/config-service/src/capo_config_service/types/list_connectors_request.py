"""Generated from Smithy shape ``com.amazonaws.configservice#ListConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.connector_filter_list
    import capo_config_service.types.list_connectors_max_results
    import capo_config_service.types.string


class ListConnectorsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_config_service.types.list_connectors_max_results.ListConnectorsMaxResults"
    ]
    """<p>The maximum number of results to include in the response.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>NextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""
    filters: NotRequired[
        "capo_config_service.types.connector_filter_list.ConnectorFilterList"
    ]
    """<p>Filters the results based on a list of <code>ConnectorFilter</code> objects that you specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConnectorsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_config_service.types.connector_filter_list

        out["Filters"] = (
            capo_config_service.types.connector_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConnectorsRequest:
    out: ListConnectorsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_config_service.types.connector_filter_list

        out["filters"] = (
            capo_config_service.types.connector_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
