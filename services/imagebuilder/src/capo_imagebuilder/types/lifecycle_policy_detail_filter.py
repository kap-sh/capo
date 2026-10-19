"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_policy_detail_filter_retain_at_least
    import capo_imagebuilder.types.lifecycle_policy_detail_filter_type
    import capo_imagebuilder.types.lifecycle_policy_detail_filter_value
    import capo_imagebuilder.types.lifecycle_policy_time_unit


class LifecyclePolicyDetailFilter(TypedDict, closed=True):
    type: "capo_imagebuilder.types.lifecycle_policy_detail_filter_type.LifecyclePolicyDetailFilterType"
    """<p>Filter resources based on either <code>AGE</code> or <code>COUNT</code>. You can only use the count filter with the <code>DELETE</code> action type.</p>"""
    value: "capo_imagebuilder.types.lifecycle_policy_detail_filter_value.LifecyclePolicyDetailFilterValue"
    """<p>The number of units for the time period or for the count. For example, a value of <code>6</code> might refer to six months or six AMIs.</p> <note> <p>For count-based filters, this value represents the minimum number of resources to keep on hand. If you have fewer resources than this number, the resource is excluded from lifecycle actions.</p> </note>"""
    unit: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_time_unit.LifecyclePolicyTimeUnit"
    ]
    """<p>Defines the unit of time that the lifecycle policy uses to determine impacted resources. This is required for age-based rules.</p>"""
    retain_at_least: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_detail_filter_retain_at_least.LifecyclePolicyDetailFilterRetainAtLeast"
    ]
    """<p>For age-based filters, this is the number of resources to keep on hand after the lifecycle <code>DELETE</code> action is applied. Impacted resources are only deleted if you have more than this number of resources. If you have fewer resources than this number, the impacted resource is not deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailFilter) -> dict:
    out: dict = {}
    import capo_imagebuilder.types.lifecycle_policy_detail_filter_type

    out["type"] = (
        capo_imagebuilder.types.lifecycle_policy_detail_filter_type.serialize_json(
            value["type"]
        )
    )
    out["value"] = value["value"]
    if "unit" in value:
        import capo_imagebuilder.types.lifecycle_policy_time_unit

        out["unit"] = capo_imagebuilder.types.lifecycle_policy_time_unit.serialize_json(
            value["unit"]
        )
    if "retain_at_least" in value:
        out["retainAtLeast"] = value["retain_at_least"]
    return out


def deserialize_json(data: dict) -> LifecyclePolicyDetailFilter:
    out: LifecyclePolicyDetailFilter = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_imagebuilder.types.lifecycle_policy_detail_filter_type

        out["type"] = (
            capo_imagebuilder.types.lifecycle_policy_detail_filter_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_imagebuilder.types.lifecycle_policy_detail_filter_type.LifecyclePolicyDetailFilterType",
            "",
        )
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
    if data.get("retainAtLeast") is not None:
        out["retain_at_least"] = data["retainAtLeast"]
    return out
