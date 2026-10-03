"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEncryptionControlsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_vpc_encryption_controls_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string
    import capo_ec2.types.vpc_encryption_control_id_list
    import capo_ec2.types.vpc_id_string_list


class DescribeVpcEncryptionControlsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters to apply to the request.</p>"""
    vpc_encryption_control_ids: NotRequired[
        "capo_ec2.types.vpc_encryption_control_id_list.VpcEncryptionControlIdList"
    ]
    """<p>The IDs of the VPC Encryption Control configurations to describe.</p>"""
    vpc_ids: NotRequired["capo_ec2.types.vpc_id_string_list.VpcIdStringList"]
    """<p>The IDs of the VPCs to describe encryption control configurations for.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_vpc_encryption_controls_max_results.DescribeVpcEncryptionControlsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEncryptionControlsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "vpc_encryption_control_ids" in value:
        import capo_ec2.types.vpc_encryption_control_id_list

        capo_ec2.types.vpc_encryption_control_id_list.serialize_ec2_query(
            value["vpc_encryption_control_ids"],
            pairs,
            f"{key_prefix}VpcEncryptionControlId",
        )
    if "vpc_ids" in value:
        import capo_ec2.types.vpc_id_string_list

        capo_ec2.types.vpc_id_string_list.serialize_ec2_query(
            value["vpc_ids"], pairs, f"{key_prefix}VpcId"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEncryptionControlsRequest:
    out: DescribeVpcEncryptionControlsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_vpc_encryption_control_ids = el.find("VpcEncryptionControlId")
    if child_vpc_encryption_control_ids is not None:
        import capo_ec2.types.vpc_encryption_control_id_list

        out["vpc_encryption_control_ids"] = (
            capo_ec2.types.vpc_encryption_control_id_list.deserialize_ec2_query(
                child_vpc_encryption_control_ids
            )
        )
    child_vpc_ids = el.find("VpcId")
    if child_vpc_ids is not None:
        import capo_ec2.types.vpc_id_string_list

        out["vpc_ids"] = capo_ec2.types.vpc_id_string_list.deserialize_ec2_query(
            child_vpc_ids
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
