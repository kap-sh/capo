"""Generated from Smithy shape ``com.amazonaws.gamelift#ListLocationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.location_model_list
    import capo_gamelift.types.non_zero_and_max_string


class ListLocationsOutput(TypedDict, closed=True):
    locations: NotRequired["capo_gamelift.types.location_model_list.LocationModelList"]
    """<p>A collection of locations, including both Amazon Web Services and custom locations. Each location includes a name and ping beacon information that can be used to measure network latency between player devices and the location.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLocationsOutput) -> dict:
    out: dict = {}
    if "locations" in value:
        import capo_gamelift.types.location_model_list

        out["Locations"] = (
            capo_gamelift.types.location_model_list.serialize_aws_json_1_1(
                value["locations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLocationsOutput:
    out: ListLocationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Locations") is not None:
        import capo_gamelift.types.location_model_list

        out["locations"] = (
            capo_gamelift.types.location_model_list.deserialize_aws_json_1_1(
                data["Locations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListLocationsOutput) -> dict:
    out: dict = {}
    if "locations" in value:
        import capo_gamelift.types.location_model_list

        out["Locations"] = capo_gamelift.types.location_model_list.serialize_cbor(
            value["locations"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListLocationsOutput:
    out: ListLocationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Locations") is not None:
        import capo_gamelift.types.location_model_list

        out["locations"] = capo_gamelift.types.location_model_list.deserialize_cbor(
            data["Locations"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
