"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#PropertyFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.property


class PropertyFilter(TypedDict, closed=True):
    property: "capo_sagemaker_geospatial.types.property.Property"
    """<p>Represents a single property to match with when searching a raster data collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyFilter) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial.types.property

    out["Property"] = capo_sagemaker_geospatial.types.property.serialize_json(
        value["property"]
    )
    return out


def deserialize_json(data: dict) -> PropertyFilter:
    out: PropertyFilter = {}  # type: ignore[typeddict-item]
    if data.get("Property") is not None:
        import capo_sagemaker_geospatial.types.property

        out["property"] = capo_sagemaker_geospatial.types.property.deserialize_json(
            data["Property"]
        )
    else:
        import capo_sagemaker_geospatial.types._unknown

        out["property"] = capo_sagemaker_geospatial.types._unknown.UnknownUnionMember(
            ""
        )
    return out
