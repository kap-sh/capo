"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotInstanceRequestsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_instance_request_list
    import capo_ec2.types.string


class DescribeSpotInstanceRequestsResult(TypedDict, closed=True):
    spot_instance_requests: NotRequired[
        "capo_ec2.types.spot_instance_request_list.SpotInstanceRequestList"
    ]
    """<p>The Spot Instance requests.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotInstanceRequestsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "spot_instance_requests" in value:
        import capo_ec2.types.spot_instance_request_list

        capo_ec2.types.spot_instance_request_list.serialize_ec2_query(
            value["spot_instance_requests"],
            pairs,
            f"{key_prefix}SpotInstanceRequestSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSpotInstanceRequestsResult:
    out: DescribeSpotInstanceRequestsResult = {}  # type: ignore[typeddict-item]
    child_spot_instance_requests = el.find("spotInstanceRequestSet")
    if child_spot_instance_requests is not None:
        import capo_ec2.types.spot_instance_request_list

        out["spot_instance_requests"] = (
            capo_ec2.types.spot_instance_request_list.deserialize_ec2_query(
                child_spot_instance_requests
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


def redact_sensitive(value: DescribeSpotInstanceRequestsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spot_instance_requests" in value:
        import capo_ec2.types.spot_instance_request_list

        out["spot_instance_requests"] = (
            capo_ec2.types.spot_instance_request_list.redact_sensitive(
                value["spot_instance_requests"]
            )
        )
    return out
