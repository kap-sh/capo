"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CapacityProviderStrategyItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.capacity_provider
    import capo_cloudwatch_events.types.capacity_provider_strategy_item_base
    import capo_cloudwatch_events.types.capacity_provider_strategy_item_weight


class CapacityProviderStrategyItem(TypedDict, closed=True):
    capacity_provider: "capo_cloudwatch_events.types.capacity_provider.CapacityProvider"
    """<p>The short name of the capacity provider.</p>"""
    weight: "capo_cloudwatch_events.types.capacity_provider_strategy_item_weight.CapacityProviderStrategyItemWeight"
    """<p>The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The weight value is taken into consideration after the base value, if defined, is satisfied.</p>"""
    base: "capo_cloudwatch_events.types.capacity_provider_strategy_item_base.CapacityProviderStrategyItemBase"
    """<p>The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of 0 is used. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityProviderStrategyItem) -> dict:
    out: dict = {}
    out["capacityProvider"] = value["capacity_provider"]
    out["weight"] = value.get("weight", 0)
    out["base"] = value.get("base", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityProviderStrategyItem:
    out: CapacityProviderStrategyItem = {}  # type: ignore[typeddict-item]
    if data.get("capacityProvider") is not None:
        out["capacity_provider"] = data["capacityProvider"]
    else:
        out["capacity_provider"] = ""
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    else:
        out["weight"] = 0
    if data.get("base") is not None:
        out["base"] = data["base"]
    else:
        out["base"] = 0
    return out
