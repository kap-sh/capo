"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockExtensionOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_id
    import capo_ec2.types.describe_capacity_block_extension_offerings_max_results
    import capo_ec2.types.integer
    import capo_ec2.types.string


class DescribeCapacityBlockExtensionOfferingsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    capacity_block_extension_duration_hours: NotRequired[
        "capo_ec2.types.integer.Integer"
    ]
    """<p>The duration of the Capacity Block extension offering in hours.</p>"""
    capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity reservation to be extended.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_capacity_block_extension_offerings_max_results.DescribeCapacityBlockExtensionOfferingsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlockExtensionOfferingsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "capacity_block_extension_duration_hours" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityBlockExtensionDurationHours",
                str(value["capacity_block_extension_duration_hours"]),
            )
        )
    if "capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationId",
                str(value["capacity_reservation_id"]),
            )
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeCapacityBlockExtensionOfferingsRequest:
    out: DescribeCapacityBlockExtensionOfferingsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_capacity_block_extension_duration_hours = el.find(
        "CapacityBlockExtensionDurationHours"
    )
    if child_capacity_block_extension_duration_hours is not None:
        out["capacity_block_extension_duration_hours"] = int(
            child_capacity_block_extension_duration_hours.text or ""
        )
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
