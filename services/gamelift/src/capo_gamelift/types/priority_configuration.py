"""Generated from Smithy shape ``com.amazonaws.gamelift#PriorityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.location_list
    import capo_gamelift.types.priority_type_list


class PriorityConfiguration(TypedDict, closed=True):
    priority_order: NotRequired[
        "capo_gamelift.types.priority_type_list.PriorityTypeList"
    ]
    """<p>A custom sequence to use when prioritizing where to place new game sessions. Each priority type is listed once.</p> <ul> <li> <p> <code>LATENCY</code> -- Amazon GameLift Servers prioritizes locations where the average player latency is lowest. Player latency data is provided in each game session placement request.</p> </li> <li> <p> <code>COST</code> -- Amazon GameLift Servers prioritizes queue destinations with the lowest current hosting costs. Cost is evaluated based on the destination's location, instance type, and fleet type (Spot or On-Demand).</p> </li> <li> <p> <code>DESTINATION</code> -- Amazon GameLift Servers prioritizes based on the list order of destinations in the queue configuration.</p> </li> <li> <p> <code>LOCATION</code> -- Amazon GameLift Servers prioritizes based on the provided order of locations, as defined in <code>LocationOrder</code>. </p> </li> </ul>"""
    location_order: NotRequired["capo_gamelift.types.location_list.LocationList"]
    """<p>The prioritization order to use for fleet locations, when the <code>PriorityOrder</code> property includes <code>LOCATION</code>. Locations can include Amazon Web Services Region codes (such as <code>us-west-2</code>), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html">Amazon GameLift Servers service locations.</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriorityConfiguration) -> dict:
    out: dict = {}
    if "priority_order" in value:
        import capo_gamelift.types.priority_type_list

        out["PriorityOrder"] = (
            capo_gamelift.types.priority_type_list.serialize_aws_json_1_1(
                value["priority_order"]
            )
        )
    if "location_order" in value:
        import capo_gamelift.types.location_list

        out["LocationOrder"] = capo_gamelift.types.location_list.serialize_aws_json_1_1(
            value["location_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PriorityConfiguration:
    out: PriorityConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PriorityOrder") is not None:
        import capo_gamelift.types.priority_type_list

        out["priority_order"] = (
            capo_gamelift.types.priority_type_list.deserialize_aws_json_1_1(
                data["PriorityOrder"]
            )
        )
    if data.get("LocationOrder") is not None:
        import capo_gamelift.types.location_list

        out["location_order"] = (
            capo_gamelift.types.location_list.deserialize_aws_json_1_1(
                data["LocationOrder"]
            )
        )
    return out
