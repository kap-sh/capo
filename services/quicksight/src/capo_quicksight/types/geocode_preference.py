"""Generated from Smithy shape ``com.amazonaws.quicksight#GeocodePreference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.geocode_preference_value
    import capo_quicksight.types.geocoder_hierarchy


class GeocodePreference(TypedDict, closed=True):
    request_key: "capo_quicksight.types.geocoder_hierarchy.GeocoderHierarchy"
    """<p>The unique request key for the geocode preference.</p>"""
    preference: "capo_quicksight.types.geocode_preference_value.GeocodePreferenceValue"
    """<p>The preference definition for the geocode preference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocodePreference) -> dict:
    out: dict = {}
    import capo_quicksight.types.geocoder_hierarchy

    out["RequestKey"] = capo_quicksight.types.geocoder_hierarchy.serialize_json(
        value["request_key"]
    )
    import capo_quicksight.types.geocode_preference_value

    out["Preference"] = capo_quicksight.types.geocode_preference_value.serialize_json(
        value["preference"]
    )
    return out


def deserialize_json(data: dict) -> GeocodePreference:
    out: GeocodePreference = {}  # type: ignore[typeddict-item]
    if data.get("RequestKey") is not None:
        import capo_quicksight.types.geocoder_hierarchy

        out["request_key"] = capo_quicksight.types.geocoder_hierarchy.deserialize_json(
            data["RequestKey"]
        )
    else:
        raise DeserializationError("GeocodePreference.request_key required")
    if data.get("Preference") is not None:
        import capo_quicksight.types.geocode_preference_value

        out["preference"] = (
            capo_quicksight.types.geocode_preference_value.deserialize_json(
                data["Preference"]
            )
        )
    else:
        out["preference"] = {"$unknown": {"name": ""}}
    return out
