"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIamInstanceProfileAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.association_id_list
    import capo_ec2.types.describe_iam_instance_profile_associations_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.next_token


class DescribeIamInstanceProfileAssociationsRequest(TypedDict, closed=True):
    association_ids: NotRequired["capo_ec2.types.association_id_list.AssociationIdList"]
    """<p>The IAM instance profile associations.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>instance-id</code> - The ID of the instance.</p> </li> <li> <p> <code>state</code> - The state of the association (<code>associating</code> | <code>associated</code> | <code>disassociating</code>).</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_iam_instance_profile_associations_max_results.DescribeIamInstanceProfileAssociationsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIamInstanceProfileAssociationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association_ids" in value:
        import capo_ec2.types.association_id_list

        capo_ec2.types.association_id_list.serialize_ec2_query(
            value["association_ids"], pairs, f"{key_prefix}AssociationId"
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


def deserialize_ec2_query(el: Element) -> DescribeIamInstanceProfileAssociationsRequest:
    out: DescribeIamInstanceProfileAssociationsRequest = {}  # type: ignore[typeddict-item]
    child_association_ids = el.find("AssociationId")
    if child_association_ids is not None:
        import capo_ec2.types.association_id_list

        out["association_ids"] = (
            capo_ec2.types.association_id_list.deserialize_ec2_query(
                child_association_ids
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
    return out
