"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetAttributesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_attributes_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeFleetAttributesOutput(TypedDict, closed=True):
    fleet_attributes: NotRequired[
        "capo_gamelift.types.fleet_attributes_list.FleetAttributesList"
    ]
    """<p>A collection of objects containing attribute metadata for each requested fleet ID. Attribute objects are returned only for fleets that currently exist.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetAttributesOutput) -> dict:
    out: dict = {}
    if "fleet_attributes" in value:
        import capo_gamelift.types.fleet_attributes_list

        out["FleetAttributes"] = (
            capo_gamelift.types.fleet_attributes_list.serialize_aws_json_1_1(
                value["fleet_attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetAttributesOutput:
    out: DescribeFleetAttributesOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetAttributes") is not None:
        import capo_gamelift.types.fleet_attributes_list

        out["fleet_attributes"] = (
            capo_gamelift.types.fleet_attributes_list.deserialize_aws_json_1_1(
                data["FleetAttributes"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFleetAttributesOutput) -> dict:
    out: dict = {}
    if "fleet_attributes" in value:
        import capo_gamelift.types.fleet_attributes_list

        out["FleetAttributes"] = (
            capo_gamelift.types.fleet_attributes_list.serialize_cbor(
                value["fleet_attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeFleetAttributesOutput:
    out: DescribeFleetAttributesOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetAttributes") is not None:
        import capo_gamelift.types.fleet_attributes_list

        out["fleet_attributes"] = (
            capo_gamelift.types.fleet_attributes_list.deserialize_cbor(
                data["FleetAttributes"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
