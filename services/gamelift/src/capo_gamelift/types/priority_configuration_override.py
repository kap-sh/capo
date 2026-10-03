"""Generated from Smithy shape ``com.amazonaws.gamelift#PriorityConfigurationOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.location_order_override_list
    import capo_gamelift.types.placement_fallback_strategy


class PriorityConfigurationOverride(TypedDict, closed=True):
    placement_fallback_strategy: NotRequired[
        "capo_gamelift.types.placement_fallback_strategy.PlacementFallbackStrategy"
    ]
    """<p>Instructions for how to proceed if placement fails in every location on the priority override list. Valid strategies include: </p> <ul> <li> <p> <code>DEFAULT_AFTER_SINGLE_PASS</code> -- After attempting to place a new game session in every location on the priority override list, try to place a game session in queue's other locations. This is the default behavior.</p> </li> <li> <p> <code>NONE</code> -- Limit placements to locations on the priority override list only. </p> </li> </ul>"""
    location_order: NotRequired[
        "capo_gamelift.types.location_order_override_list.LocationOrderOverrideList"
    ]
    """<p>A prioritized list of hosting locations. The list can include Amazon Web Services Regions (such as <code>us-west-2</code>), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html">Amazon GameLift Servers service locations.</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriorityConfigurationOverride) -> dict:
    out: dict = {}
    if "placement_fallback_strategy" in value:
        import capo_gamelift.types.placement_fallback_strategy

        out["PlacementFallbackStrategy"] = (
            capo_gamelift.types.placement_fallback_strategy.serialize_aws_json_1_1(
                value["placement_fallback_strategy"]
            )
        )
    if "location_order" in value:
        import capo_gamelift.types.location_order_override_list

        out["LocationOrder"] = (
            capo_gamelift.types.location_order_override_list.serialize_aws_json_1_1(
                value["location_order"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PriorityConfigurationOverride:
    out: PriorityConfigurationOverride = {}  # type: ignore[typeddict-item]
    if data.get("PlacementFallbackStrategy") is not None:
        import capo_gamelift.types.placement_fallback_strategy

        out["placement_fallback_strategy"] = (
            capo_gamelift.types.placement_fallback_strategy.deserialize_aws_json_1_1(
                data["PlacementFallbackStrategy"]
            )
        )
    if data.get("LocationOrder") is not None:
        import capo_gamelift.types.location_order_override_list

        out["location_order"] = (
            capo_gamelift.types.location_order_override_list.deserialize_aws_json_1_1(
                data["LocationOrder"]
            )
        )
    return out
