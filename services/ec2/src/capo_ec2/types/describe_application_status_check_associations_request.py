"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeApplicationStatusCheckAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status_check_id_list
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_application_status_check_associations_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string


class DescribeApplicationStatusCheckAssociationsRequest(TypedDict, closed=True):
    application_status_check_ids: NotRequired[
        "capo_ec2.types.application_status_check_id_list.ApplicationStatusCheckIdList"
    ]
    """<p>The IDs of the application status checks for which to describe associations.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters to use to limit the results.</p> <ul> <li> <p> <code>association-type</code> – The type of association. Valid values: <code>tag</code> and <code>instance-id</code>.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_application_status_check_associations_max_results.DescribeApplicationStatusCheckAssociationsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeApplicationStatusCheckAssociationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_status_check_ids" in value:
        import capo_ec2.types.application_status_check_id_list

        capo_ec2.types.application_status_check_id_list.serialize_ec2_query(
            value["application_status_check_ids"],
            pairs,
            f"{key_prefix}ApplicationStatusCheckId",
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DescribeApplicationStatusCheckAssociationsRequest:
    out: DescribeApplicationStatusCheckAssociationsRequest = {}  # type: ignore[typeddict-item]
    child_application_status_check_ids = el.find("ApplicationStatusCheckId")
    if child_application_status_check_ids is not None:
        import capo_ec2.types.application_status_check_id_list

        out["application_status_check_ids"] = (
            capo_ec2.types.application_status_check_id_list.deserialize_ec2_query(
                child_application_status_check_ids
            )
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
