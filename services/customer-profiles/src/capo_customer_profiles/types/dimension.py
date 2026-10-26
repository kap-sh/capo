"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Dimension``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError, SerializationError
from capo_customer_profiles.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_customer_profiles.types.calculated_custom_attributes
    import capo_customer_profiles.types.profile_attributes


class _Dimension_ProfileAttributes(TypedDict, closed=True):
    ProfileAttributes: (
        "capo_customer_profiles.types.profile_attributes.ProfileAttributes"
    )


class _Dimension_CalculatedAttributes(TypedDict, closed=True):
    CalculatedAttributes: "capo_customer_profiles.types.calculated_custom_attributes.CalculatedCustomAttributes"


Dimension: TypeAlias = (
    _Dimension_ProfileAttributes | _Dimension_CalculatedAttributes | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Dimension) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Dimension: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ProfileAttributes" in value:
        import capo_customer_profiles.types.profile_attributes

        return {
            "ProfileAttributes": capo_customer_profiles.types.profile_attributes.serialize_json(
                value["ProfileAttributes"]
            )
        }
    elif "CalculatedAttributes" in value:
        import capo_customer_profiles.types.calculated_custom_attributes

        return {
            "CalculatedAttributes": capo_customer_profiles.types.calculated_custom_attributes.serialize_json(
                value["CalculatedAttributes"]
            )
        }
    else:
        raise SerializationError("Dimension: no variant present")


def deserialize_json(data: dict) -> Dimension:
    if data.get("ProfileAttributes") is not None:
        import capo_customer_profiles.types.profile_attributes

        return {
            "ProfileAttributes": capo_customer_profiles.types.profile_attributes.deserialize_json(
                data["ProfileAttributes"]
            )
        }
    elif data.get("CalculatedAttributes") is not None:
        import capo_customer_profiles.types.calculated_custom_attributes

        return {
            "CalculatedAttributes": capo_customer_profiles.types.calculated_custom_attributes.deserialize_json(
                data["CalculatedAttributes"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Dimension: no recognized variant key")


def redact_sensitive(value: Dimension) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ProfileAttributes" in value:
        out["ProfileAttributes"] = "*** Sensitive Data Redacted ***"
    if "CalculatedAttributes" in value:
        import capo_customer_profiles.types.calculated_custom_attributes

        out["CalculatedAttributes"] = (
            capo_customer_profiles.types.calculated_custom_attributes.redact_sensitive(
                value["CalculatedAttributes"]
            )
        )
    return out
