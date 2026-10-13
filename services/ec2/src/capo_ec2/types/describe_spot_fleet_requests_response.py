"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetRequestsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_fleet_request_config_set
    import capo_ec2.types.string


class DescribeSpotFleetRequestsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    spot_fleet_request_configs: NotRequired[
        "capo_ec2.types.spot_fleet_request_config_set.SpotFleetRequestConfigSet"
    ]
    """<p>Information about the configuration of your Spot Fleet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotFleetRequestsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "spot_fleet_request_configs" in value:
        import capo_ec2.types.spot_fleet_request_config_set

        capo_ec2.types.spot_fleet_request_config_set.serialize_ec2_query(
            value["spot_fleet_request_configs"],
            pairs,
            f"{key_prefix}SpotFleetRequestConfigSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeSpotFleetRequestsResponse:
    out: DescribeSpotFleetRequestsResponse = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_spot_fleet_request_configs = el.find("spotFleetRequestConfigSet")
    if child_spot_fleet_request_configs is not None:
        import capo_ec2.types.spot_fleet_request_config_set

        out["spot_fleet_request_configs"] = (
            capo_ec2.types.spot_fleet_request_config_set.deserialize_ec2_query(
                child_spot_fleet_request_configs
            )
        )
    return out


def redact_sensitive(value: DescribeSpotFleetRequestsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spot_fleet_request_configs" in value:
        import capo_ec2.types.spot_fleet_request_config_set

        out["spot_fleet_request_configs"] = (
            capo_ec2.types.spot_fleet_request_config_set.redact_sensitive(
                value["spot_fleet_request_configs"]
            )
        )
    return out
