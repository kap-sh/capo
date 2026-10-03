"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeStoreImageTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_store_image_tasks_request_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.image_id_list
    import capo_ec2.types.string


class DescribeStoreImageTasksRequest(TypedDict, closed=True):
    image_ids: NotRequired["capo_ec2.types.image_id_list.ImageIdList"]
    """<p>The AMI IDs for which to show progress. Up to 20 AMI IDs can be included in a request.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>task-state</code> - Returns tasks in a certain state (<code>InProgress</code> | <code>Completed</code> | <code>Failed</code>)</p> </li> <li> <p> <code>bucket</code> - Returns task information for tasks that targeted a specific bucket. For the filter value, specify the bucket name.</p> </li> </ul> <note> <p>When you specify the <code>ImageIds</code> parameter, any filters that you specify are ignored. To use the filters, you must remove the <code>ImageIds</code> parameter.</p> </note>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_store_image_tasks_request_max_results.DescribeStoreImageTasksRequestMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p> <p>You cannot specify this parameter and the <code>ImageIds</code> parameter in the same call.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeStoreImageTasksRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_ids" in value:
        import capo_ec2.types.image_id_list

        capo_ec2.types.image_id_list.serialize_ec2_query(
            value["image_ids"], pairs, f"{key_prefix}ImageId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeStoreImageTasksRequest:
    out: DescribeStoreImageTasksRequest = {}  # type: ignore[typeddict-item]
    child_image_ids = el.find("ImageId")
    if child_image_ids is not None:
        import capo_ec2.types.image_id_list

        out["image_ids"] = capo_ec2.types.image_id_list.deserialize_ec2_query(
            child_image_ids
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
