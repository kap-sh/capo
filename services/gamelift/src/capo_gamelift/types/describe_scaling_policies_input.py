"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeScalingPoliciesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.scaling_status_type


class DescribeScalingPoliciesInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet for which to retrieve scaling policies. You can use either the fleet ID or ARN value.</p>"""
    status_filter: NotRequired[
        "capo_gamelift.types.scaling_status_type.ScalingStatusType"
    ]
    """<p>Scaling policy status to filter results on. A scaling policy is only in force when in an <code>ACTIVE</code> status.</p> <ul> <li> <p> <b>ACTIVE</b> -- The scaling policy is currently in force.</p> </li> <li> <p> <b>UPDATEREQUESTED</b> -- A request to update the scaling policy has been received.</p> </li> <li> <p> <b>UPDATING</b> -- A change is being made to the scaling policy.</p> </li> <li> <p> <b>DELETEREQUESTED</b> -- A request to delete the scaling policy has been received.</p> </li> <li> <p> <b>DELETING</b> -- The scaling policy is being deleted.</p> </li> <li> <p> <b>DELETED</b> -- The scaling policy has been deleted.</p> </li> <li> <p> <b>ERROR</b> -- An error occurred in creating the policy. It should be removed and recreated.</p> </li> </ul>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p> The fleet location. If you don't specify this value, the response contains the scaling policies of every location in the fleet. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalingPoliciesInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "status_filter" in value:
        import capo_gamelift.types.scaling_status_type

        out["StatusFilter"] = (
            capo_gamelift.types.scaling_status_type.serialize_aws_json_1_1(
                value["status_filter"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalingPoliciesInput:
    out: DescribeScalingPoliciesInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("StatusFilter") is not None:
        import capo_gamelift.types.scaling_status_type

        out["status_filter"] = (
            capo_gamelift.types.scaling_status_type.deserialize_aws_json_1_1(
                data["StatusFilter"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeScalingPoliciesInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "status_filter" in value:
        import capo_gamelift.types.scaling_status_type

        out["StatusFilter"] = capo_gamelift.types.scaling_status_type.serialize_cbor(
            value["status_filter"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_cbor(data: dict) -> DescribeScalingPoliciesInput:
    out: DescribeScalingPoliciesInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("StatusFilter") is not None:
        import capo_gamelift.types.scaling_status_type

        out["status_filter"] = capo_gamelift.types.scaling_status_type.deserialize_cbor(
            data["StatusFilter"]
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
