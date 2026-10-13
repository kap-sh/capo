"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DetectProfileObjectTypeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.detected_profile_object_types


class DetectProfileObjectTypeResponse(TypedDict, closed=True):
    detected_profile_object_types: NotRequired[
        "capo_customer_profiles.types.detected_profile_object_types.DetectedProfileObjectTypes"
    ]
    """<p>Detected <code>ProfileObjectType</code> mappings from given objects. A maximum of one mapping is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectProfileObjectTypeResponse) -> dict:
    out: dict = {}
    if "detected_profile_object_types" in value:
        import capo_customer_profiles.types.detected_profile_object_types

        out["DetectedProfileObjectTypes"] = (
            capo_customer_profiles.types.detected_profile_object_types.serialize_json(
                value["detected_profile_object_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectProfileObjectTypeResponse:
    out: DetectProfileObjectTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("DetectedProfileObjectTypes") is not None:
        import capo_customer_profiles.types.detected_profile_object_types

        out["detected_profile_object_types"] = (
            capo_customer_profiles.types.detected_profile_object_types.deserialize_json(
                data["DetectedProfileObjectTypes"]
            )
        )
    return out


def redact_sensitive(value: DetectProfileObjectTypeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "detected_profile_object_types" in value:
        import capo_customer_profiles.types.detected_profile_object_types

        out["detected_profile_object_types"] = (
            capo_customer_profiles.types.detected_profile_object_types.redact_sensitive(
                value["detected_profile_object_types"]
            )
        )
    return out
