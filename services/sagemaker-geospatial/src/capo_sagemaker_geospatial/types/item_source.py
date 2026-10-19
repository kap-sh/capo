"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ItemSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_sagemaker_geospatial.types.assets_map
    import capo_sagemaker_geospatial.types.geometry
    import capo_sagemaker_geospatial.types.properties


class ItemSource(TypedDict, closed=True):
    id: "str"
    """<p>A unique Id for the source item.</p>"""
    geometry: "capo_sagemaker_geospatial.types.geometry.Geometry"
    """<p>The item Geometry in GeoJson format.</p>"""
    assets: NotRequired["capo_sagemaker_geospatial.types.assets_map.AssetsMap"]
    """<p>This is a dictionary of Asset Objects data associated with the Item that can be downloaded or streamed, each with a unique key.</p>"""
    date_time: "datetime.datetime"
    """<p>The searchable date and time of the item, in UTC.</p>"""
    properties: NotRequired["capo_sagemaker_geospatial.types.properties.Properties"]
    """<p>This field contains additional properties of the item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemSource) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_sagemaker_geospatial.types.geometry

    out["Geometry"] = capo_sagemaker_geospatial.types.geometry.serialize_json(
        value["geometry"]
    )
    if "assets" in value:
        import capo_sagemaker_geospatial.types.assets_map

        out["Assets"] = capo_sagemaker_geospatial.types.assets_map.serialize_json(
            value["assets"]
        )
    import capo_sagemaker_geospatial.types._prelude.timestamp

    out["DateTime"] = capo_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
        value["date_time"]
    )
    if "properties" in value:
        import capo_sagemaker_geospatial.types.properties

        out["Properties"] = capo_sagemaker_geospatial.types.properties.serialize_json(
            value["properties"]
        )
    return out


def deserialize_json(data: dict) -> ItemSource:
    out: ItemSource = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Geometry") is not None:
        import capo_sagemaker_geospatial.types.geometry

        out["geometry"] = capo_sagemaker_geospatial.types.geometry.deserialize_json(
            data["Geometry"]
        )
    else:
        raise DeserializationError("ItemSource.geometry required")
    if data.get("Assets") is not None:
        import capo_sagemaker_geospatial.types.assets_map

        out["assets"] = capo_sagemaker_geospatial.types.assets_map.deserialize_json(
            data["Assets"]
        )
    if data.get("DateTime") is not None:
        import capo_sagemaker_geospatial.types._prelude.timestamp

        out["date_time"] = (
            capo_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["DateTime"]
            )
        )
    else:
        import datetime

        out["date_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Properties") is not None:
        import capo_sagemaker_geospatial.types.properties

        out["properties"] = capo_sagemaker_geospatial.types.properties.deserialize_json(
            data["Properties"]
        )
    return out


def redact_sensitive(value: ItemSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "geometry" in value:
        import capo_sagemaker_geospatial.types.geometry

        out["geometry"] = capo_sagemaker_geospatial.types.geometry.redact_sensitive(
            value["geometry"]
        )
    return out
