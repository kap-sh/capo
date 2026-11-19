"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetLocationAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_list
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer


class DescribeFleetLocationAttributesInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to retrieve remote locations for. You can use either the fleet ID or ARN value.</p>"""
    locations: NotRequired["capo_gamelift.types.location_list.LocationList"]
    """<p>A list of fleet locations to retrieve information for. Specify locations in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. This limit is not currently enforced.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetLocationAttributesInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "locations" in value:
        import capo_gamelift.types.location_list

        out["Locations"] = capo_gamelift.types.location_list.serialize_aws_json_1_1(
            value["locations"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetLocationAttributesInput:
    out: DescribeFleetLocationAttributesInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Locations") is not None:
        import capo_gamelift.types.location_list

        out["locations"] = capo_gamelift.types.location_list.deserialize_aws_json_1_1(
            data["Locations"]
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFleetLocationAttributesInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "locations" in value:
        import capo_gamelift.types.location_list

        out["Locations"] = capo_gamelift.types.location_list.serialize_cbor(
            value["locations"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeFleetLocationAttributesInput:
    out: DescribeFleetLocationAttributesInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Locations") is not None:
        import capo_gamelift.types.location_list

        out["locations"] = capo_gamelift.types.location_list.deserialize_cbor(
            data["Locations"]
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
