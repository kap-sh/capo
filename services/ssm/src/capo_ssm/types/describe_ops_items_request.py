"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeOpsItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_filters
    import capo_ssm.types.ops_item_max_results
    import capo_ssm.types.string


class DescribeOpsItemsRequest(TypedDict, closed=True):
    ops_item_filters: NotRequired["capo_ssm.types.ops_item_filters.OpsItemFilters"]
    """<p>One or more filters to limit the response.</p> <ul> <li> <p>Key: CreatedTime</p> <p>Operations: GreaterThan, LessThan</p> </li> <li> <p>Key: LastModifiedBy</p> <p>Operations: Contains, Equals</p> </li> <li> <p>Key: LastModifiedTime</p> <p>Operations: GreaterThan, LessThan</p> </li> <li> <p>Key: Priority</p> <p>Operations: Equals</p> </li> <li> <p>Key: Source</p> <p>Operations: Contains, Equals</p> </li> <li> <p>Key: Status</p> <p>Operations: Equals</p> </li> <li> <p>Key: Title*</p> <p>Operations: Equals,Contains</p> </li> <li> <p>Key: OperationalData**</p> <p>Operations: Equals</p> </li> <li> <p>Key: OperationalDataKey</p> <p>Operations: Equals</p> </li> <li> <p>Key: OperationalDataValue</p> <p>Operations: Equals, Contains</p> </li> <li> <p>Key: OpsItemId</p> <p>Operations: Equals</p> </li> <li> <p>Key: ResourceId</p> <p>Operations: Contains</p> </li> <li> <p>Key: AutomationId</p> <p>Operations: Equals</p> </li> <li> <p>Key: AccountId</p> <p>Operations: Equals</p> </li> </ul> <p>*The Equals operator for Title matches the first 100 characters. If you specify more than 100 characters, they system returns an error that the filter value exceeds the length limit.</p> <p>**If you filter the response by using the OperationalData operator, specify a key-value pair by using the following JSON format: {"key":"key_name","value":"a_value"}</p>"""
    max_results: NotRequired["capo_ssm.types.ops_item_max_results.OpsItemMaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.string.String"]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOpsItemsRequest) -> dict:
    out: dict = {}
    if "ops_item_filters" in value:
        import capo_ssm.types.ops_item_filters

        out["OpsItemFilters"] = capo_ssm.types.ops_item_filters.serialize_aws_json_1_1(
            value["ops_item_filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOpsItemsRequest:
    out: DescribeOpsItemsRequest = {}  # type: ignore[typeddict-item]
    if data.get("OpsItemFilters") is not None:
        import capo_ssm.types.ops_item_filters

        out["ops_item_filters"] = (
            capo_ssm.types.ops_item_filters.deserialize_aws_json_1_1(
                data["OpsItemFilters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
