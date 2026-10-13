"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DetectedProfileObjectTypes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.detected_profile_object_type

DetectedProfileObjectTypes: TypeAlias = list[
    "capo_customer_profiles.types.detected_profile_object_type.DetectedProfileObjectType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectedProfileObjectTypes) -> list:
    import capo_customer_profiles.types.detected_profile_object_type

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.detected_profile_object_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DetectedProfileObjectTypes:
    import capo_customer_profiles.types.detected_profile_object_type

    out: DetectedProfileObjectTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_customer_profiles.types.detected_profile_object_type.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: DetectedProfileObjectTypes) -> list[Any]:
    import capo_customer_profiles.types.detected_profile_object_type

    return [
        capo_customer_profiles.types.detected_profile_object_type.redact_sensitive(item)
        for item in value
    ]
