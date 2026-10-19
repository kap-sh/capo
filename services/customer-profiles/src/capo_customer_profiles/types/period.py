"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Period``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.boolean
    import capo_customer_profiles.types.max_size60
    import capo_customer_profiles.types.max_size1000
    import capo_customer_profiles.types.period_unit


class Period(TypedDict, closed=True):
    unit: "capo_customer_profiles.types.period_unit.PeriodUnit"
    """<p>The unit of time.</p>"""
    value: "capo_customer_profiles.types.max_size60.maxSize60"
    """<p>The amount of time of the specified unit.</p>"""
    max_invocations_per_profile: NotRequired[
        "capo_customer_profiles.types.max_size1000.maxSize1000"
    ]
    """<p>The maximum allowed number of destination invocations per profile.</p>"""
    unlimited: "capo_customer_profiles.types.boolean.boolean"
    """<p>If set to true, there is no limit on the number of destination invocations per profile. The default is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Period) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.period_unit

    out["Unit"] = capo_customer_profiles.types.period_unit.serialize_json(value["unit"])
    out["Value"] = value["value"]
    if "max_invocations_per_profile" in value:
        out["MaxInvocationsPerProfile"] = value["max_invocations_per_profile"]
    out["Unlimited"] = value.get("unlimited", False)
    return out


def deserialize_json(data: dict) -> Period:
    out: Period = {}  # type: ignore[typeddict-item]
    if data.get("Unit") is not None:
        import capo_customer_profiles.types.period_unit

        out["unit"] = capo_customer_profiles.types.period_unit.deserialize_json(
            data["Unit"]
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_customer_profiles.types.period_unit.PeriodUnit", ""
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if data.get("MaxInvocationsPerProfile") is not None:
        out["max_invocations_per_profile"] = data["MaxInvocationsPerProfile"]
    if data.get("Unlimited") is not None:
        out["unlimited"] = data["Unlimited"]
    else:
        out["unlimited"] = False
    return out
