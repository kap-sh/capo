"""Generated from Smithy shape ``com.amazonaws.georoutes#DistanceThresholdList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters

DistanceThresholdList: TypeAlias = list[
    "capo_geo_routes.types.distance_meters.DistanceMeters"
]


# --- restJson1 ser/de ---
def serialize_json(value: DistanceThresholdList) -> list:
    return list(value)


def deserialize_json(data: list) -> DistanceThresholdList:
    return [item for item in data if item is not None]


def redact_sensitive(value: DistanceThresholdList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
