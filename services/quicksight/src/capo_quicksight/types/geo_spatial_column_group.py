"""Generated from Smithy shape ``com.amazonaws.quicksight#GeoSpatialColumnGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_group_name
    import capo_quicksight.types.column_list
    import capo_quicksight.types.geo_spatial_country_code


class GeoSpatialColumnGroup(TypedDict, closed=True):
    name: "capo_quicksight.types.column_group_name.ColumnGroupName"
    """<p>A display name for the hierarchy.</p>"""
    country_code: NotRequired[
        "capo_quicksight.types.geo_spatial_country_code.GeoSpatialCountryCode"
    ]
    """<p>Country code.</p>"""
    columns: "capo_quicksight.types.column_list.ColumnList"
    """<p>Columns in this hierarchy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoSpatialColumnGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "country_code" in value:
        import capo_quicksight.types.geo_spatial_country_code

        out["CountryCode"] = (
            capo_quicksight.types.geo_spatial_country_code.serialize_json(
                value["country_code"]
            )
        )
    import capo_quicksight.types.column_list

    out["Columns"] = capo_quicksight.types.column_list.serialize_json(value["columns"])
    return out


def deserialize_json(data: dict) -> GeoSpatialColumnGroup:
    out: GeoSpatialColumnGroup = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("CountryCode") is not None:
        import capo_quicksight.types.geo_spatial_country_code

        out["country_code"] = (
            capo_quicksight.types.geo_spatial_country_code.deserialize_json(
                data["CountryCode"]
            )
        )
    if data.get("Columns") is not None:
        import capo_quicksight.types.column_list

        out["columns"] = capo_quicksight.types.column_list.deserialize_json(
            data["Columns"]
        )
    else:
        out["columns"] = []
    return out
