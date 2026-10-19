"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributeDimension``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_dimension_type
    import capo_customer_profiles.types.condition_overrides
    import capo_customer_profiles.types.values


class CalculatedAttributeDimension(TypedDict, closed=True):
    dimension_type: (
        "capo_customer_profiles.types.attribute_dimension_type.AttributeDimensionType"
    )
    """<p>The action to segment with.</p>"""
    values: "capo_customer_profiles.types.values.Values"
    """<p>The values to apply the DimensionType with. To reference a calculated attribute or profile attribute as a dynamic value, use handlebar notation: <code>{{_profile.ProfileAttributeName}}</code> or <code>{{_calculated_attribute.CalculatedAttributeName}}</code>.</p>"""
    condition_overrides: NotRequired[
        "capo_customer_profiles.types.condition_overrides.ConditionOverrides"
    ]
    """<p>Applies the given condition over the initial Calculated Attribute's definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributeDimension) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.attribute_dimension_type

    out["DimensionType"] = (
        capo_customer_profiles.types.attribute_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import capo_customer_profiles.types.values

    out["Values"] = capo_customer_profiles.types.values.serialize_json(value["values"])
    if "condition_overrides" in value:
        import capo_customer_profiles.types.condition_overrides

        out["ConditionOverrides"] = (
            capo_customer_profiles.types.condition_overrides.serialize_json(
                value["condition_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> CalculatedAttributeDimension:
    out: CalculatedAttributeDimension = {}  # type: ignore[typeddict-item]
    if data.get("DimensionType") is not None:
        import capo_customer_profiles.types.attribute_dimension_type

        out["dimension_type"] = (
            capo_customer_profiles.types.attribute_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        import typing

        out["dimension_type"] = typing.cast(
            "capo_customer_profiles.types.attribute_dimension_type.AttributeDimensionType",
            "",
        )
    if data.get("Values") is not None:
        import capo_customer_profiles.types.values

        out["values"] = capo_customer_profiles.types.values.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    if data.get("ConditionOverrides") is not None:
        import capo_customer_profiles.types.condition_overrides

        out["condition_overrides"] = (
            capo_customer_profiles.types.condition_overrides.deserialize_json(
                data["ConditionOverrides"]
            )
        )
    return out


def redact_sensitive(value: CalculatedAttributeDimension) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "condition_overrides" in value:
        out["condition_overrides"] = "*** Sensitive Data Redacted ***"
    return out
