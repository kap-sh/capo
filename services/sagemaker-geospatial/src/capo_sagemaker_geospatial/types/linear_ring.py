"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#LinearRing``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.position

LinearRing: TypeAlias = list["capo_sagemaker_geospatial.types.position.Position"]


# --- restJson1 ser/de ---
def serialize_json(value: LinearRing) -> list:
    import capo_sagemaker_geospatial.types.position

    out: list = []
    for item in value:
        out.append(capo_sagemaker_geospatial.types.position.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinearRing:
    import capo_sagemaker_geospatial.types.position

    out: LinearRing = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sagemaker_geospatial.types.position.deserialize_json(item))
    return out


def redact_sensitive(value: LinearRing) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
