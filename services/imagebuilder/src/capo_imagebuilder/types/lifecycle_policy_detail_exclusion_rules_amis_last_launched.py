"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailExclusionRulesAmisLastLaunched``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched_value
    import capo_imagebuilder.types.lifecycle_policy_time_unit


class LifecyclePolicyDetailExclusionRulesAmisLastLaunched(TypedDict, closed=True):
    value: "capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched_value.LifecyclePolicyDetailExclusionRulesAmisLastLaunchedValue"
    """<p>The integer number of units for the time period. For example <code>6</code> (months).</p>"""
    unit: "capo_imagebuilder.types.lifecycle_policy_time_unit.LifecyclePolicyTimeUnit"
    """<p>Defines the unit of time that the lifecycle policy uses to calculate elapsed time since the last launch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailExclusionRulesAmisLastLaunched) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    import capo_imagebuilder.types.lifecycle_policy_time_unit

    out["unit"] = capo_imagebuilder.types.lifecycle_policy_time_unit.serialize_json(
        value["unit"]
    )
    return out


def deserialize_json(data: dict) -> LifecyclePolicyDetailExclusionRulesAmisLastLaunched:
    out: LifecyclePolicyDetailExclusionRulesAmisLastLaunched = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    if data.get("unit") is not None:
        import capo_imagebuilder.types.lifecycle_policy_time_unit

        out["unit"] = (
            capo_imagebuilder.types.lifecycle_policy_time_unit.deserialize_json(
                data["unit"]
            )
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_imagebuilder.types.lifecycle_policy_time_unit.LifecyclePolicyTimeUnit",
            "",
        )
    return out
