"""Generated from Smithy shape ``com.amazonaws.quicksight#GeocodePreferenceValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.coordinate
    import capo_quicksight.types.geocoder_hierarchy


class _GeocodePreferenceValue_GeocoderHierarchy(TypedDict, closed=True):
    GeocoderHierarchy: "capo_quicksight.types.geocoder_hierarchy.GeocoderHierarchy"


class _GeocodePreferenceValue_Coordinate(TypedDict, closed=True):
    Coordinate: "capo_quicksight.types.coordinate.Coordinate"


GeocodePreferenceValue: TypeAlias = (
    _GeocodePreferenceValue_GeocoderHierarchy
    | _GeocodePreferenceValue_Coordinate
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GeocodePreferenceValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GeocodePreferenceValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "GeocoderHierarchy" in value:
        import capo_quicksight.types.geocoder_hierarchy

        return {
            "GeocoderHierarchy": capo_quicksight.types.geocoder_hierarchy.serialize_json(
                value["GeocoderHierarchy"]
            )
        }
    elif "Coordinate" in value:
        import capo_quicksight.types.coordinate

        return {
            "Coordinate": capo_quicksight.types.coordinate.serialize_json(
                value["Coordinate"]
            )
        }
    else:
        raise SerializationError("GeocodePreferenceValue: no variant present")


def deserialize_json(data: dict) -> GeocodePreferenceValue:
    if data.get("GeocoderHierarchy") is not None:
        import capo_quicksight.types.geocoder_hierarchy

        return {
            "GeocoderHierarchy": capo_quicksight.types.geocoder_hierarchy.deserialize_json(
                data["GeocoderHierarchy"]
            )
        }
    elif data.get("Coordinate") is not None:
        import capo_quicksight.types.coordinate

        return {
            "Coordinate": capo_quicksight.types.coordinate.deserialize_json(
                data["Coordinate"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GeocodePreferenceValue: no recognized variant key")
