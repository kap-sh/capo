"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileTypeValues``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.profile_type

ProfileTypeValues: TypeAlias = list[
    "capo_customer_profiles.types.profile_type.ProfileType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTypeValues) -> list:
    import capo_customer_profiles.types.profile_type

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.profile_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileTypeValues:
    import capo_customer_profiles.types.profile_type

    out: ProfileTypeValues = []
    for item in data:
        if item is None:
            continue
        out.append(capo_customer_profiles.types.profile_type.deserialize_json(item))
    return out


def redact_sensitive(value: ProfileTypeValues) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
