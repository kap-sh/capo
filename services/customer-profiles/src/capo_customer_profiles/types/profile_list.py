"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.profile

ProfileList: TypeAlias = list["capo_customer_profiles.types.profile.Profile"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileList) -> list:
    import capo_customer_profiles.types.profile

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileList:
    import capo_customer_profiles.types.profile

    out: ProfileList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_customer_profiles.types.profile.deserialize_json(item))
    return out


def redact_sensitive(value: ProfileList) -> list[Any]:
    import capo_customer_profiles.types.profile

    return [
        capo_customer_profiles.types.profile.redact_sensitive(item) for item in value
    ]
