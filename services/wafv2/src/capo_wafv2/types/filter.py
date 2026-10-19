"""Generated from Smithy shape ``com.amazonaws.wafv2#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.conditions
    import capo_wafv2.types.filter_behavior
    import capo_wafv2.types.filter_requirement


class Filter(TypedDict, closed=True):
    behavior: "capo_wafv2.types.filter_behavior.FilterBehavior"
    """<p>How to handle logs that satisfy the filter's conditions and requirement. </p>"""
    requirement: "capo_wafv2.types.filter_requirement.FilterRequirement"
    """<p>Logic to apply to the filtering conditions. You can specify that, in order to satisfy the filter, a log must match all conditions or must match at least one condition.</p>"""
    conditions: "capo_wafv2.types.conditions.Conditions"
    """<p>Match conditions for the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    import capo_wafv2.types.filter_behavior

    out["Behavior"] = capo_wafv2.types.filter_behavior.serialize_aws_json_1_1(
        value["behavior"]
    )
    import capo_wafv2.types.filter_requirement

    out["Requirement"] = capo_wafv2.types.filter_requirement.serialize_aws_json_1_1(
        value["requirement"]
    )
    import capo_wafv2.types.conditions

    out["Conditions"] = capo_wafv2.types.conditions.serialize_aws_json_1_1(
        value["conditions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Behavior") is not None:
        import capo_wafv2.types.filter_behavior

        out["behavior"] = capo_wafv2.types.filter_behavior.deserialize_aws_json_1_1(
            data["Behavior"]
        )
    else:
        import typing

        out["behavior"] = typing.cast(
            "capo_wafv2.types.filter_behavior.FilterBehavior", ""
        )
    if data.get("Requirement") is not None:
        import capo_wafv2.types.filter_requirement

        out["requirement"] = (
            capo_wafv2.types.filter_requirement.deserialize_aws_json_1_1(
                data["Requirement"]
            )
        )
    else:
        import typing

        out["requirement"] = typing.cast(
            "capo_wafv2.types.filter_requirement.FilterRequirement", ""
        )
    if data.get("Conditions") is not None:
        import capo_wafv2.types.conditions

        out["conditions"] = capo_wafv2.types.conditions.deserialize_aws_json_1_1(
            data["Conditions"]
        )
    else:
        out["conditions"] = []
    return out
