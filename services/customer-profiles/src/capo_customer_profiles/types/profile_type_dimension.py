"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileTypeDimension``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.profile_type_dimension_type
    import capo_customer_profiles.types.profile_type_values


class ProfileTypeDimension(TypedDict, closed=True):
    dimension_type: "capo_customer_profiles.types.profile_type_dimension_type.ProfileTypeDimensionType"
    """<p>The action to segment on.</p>"""
    values: "capo_customer_profiles.types.profile_type_values.ProfileTypeValues"
    """<p>The values to apply the DimensionType on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTypeDimension) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.profile_type_dimension_type

    out["DimensionType"] = (
        capo_customer_profiles.types.profile_type_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import capo_customer_profiles.types.profile_type_values

    out["Values"] = capo_customer_profiles.types.profile_type_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> ProfileTypeDimension:
    out: ProfileTypeDimension = {}  # type: ignore[typeddict-item]
    if data.get("DimensionType") is not None:
        import capo_customer_profiles.types.profile_type_dimension_type

        out["dimension_type"] = (
            capo_customer_profiles.types.profile_type_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        import typing

        out["dimension_type"] = typing.cast(
            "capo_customer_profiles.types.profile_type_dimension_type.ProfileTypeDimensionType",
            "",
        )
    if data.get("Values") is not None:
        import capo_customer_profiles.types.profile_type_values

        out["values"] = (
            capo_customer_profiles.types.profile_type_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out


def redact_sensitive(value: ProfileTypeDimension) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_customer_profiles.types.profile_type_values

        out["values"] = (
            capo_customer_profiles.types.profile_type_values.redact_sensitive(
                value["values"]
            )
        )
    return out
