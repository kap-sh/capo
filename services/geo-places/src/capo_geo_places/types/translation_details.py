"""Generated from Smithy shape ``com.amazonaws.geoplaces#TranslationDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.admin_names_list


class TranslationDetails(TypedDict, closed=True):
    locality: NotRequired["capo_geo_places.types.admin_names_list.AdminNamesList"]
    """<p>A list of administrative names and translations for the locality address component.</p>"""
    region: NotRequired["capo_geo_places.types.admin_names_list.AdminNamesList"]
    """<p>A list of administrative names and translations for the region address component.</p>"""
    district: NotRequired["capo_geo_places.types.admin_names_list.AdminNamesList"]
    """<p>A list of administrative names and translations for the district address component.</p>"""
    sub_region: NotRequired["capo_geo_places.types.admin_names_list.AdminNamesList"]
    """<p>A list of administrative names and translations for the sub-region address component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranslationDetails) -> dict:
    out: dict = {}
    if "locality" in value:
        import capo_geo_places.types.admin_names_list

        out["Locality"] = capo_geo_places.types.admin_names_list.serialize_json(
            value["locality"]
        )
    if "region" in value:
        import capo_geo_places.types.admin_names_list

        out["Region"] = capo_geo_places.types.admin_names_list.serialize_json(
            value["region"]
        )
    if "district" in value:
        import capo_geo_places.types.admin_names_list

        out["District"] = capo_geo_places.types.admin_names_list.serialize_json(
            value["district"]
        )
    if "sub_region" in value:
        import capo_geo_places.types.admin_names_list

        out["SubRegion"] = capo_geo_places.types.admin_names_list.serialize_json(
            value["sub_region"]
        )
    return out


def deserialize_json(data: dict) -> TranslationDetails:
    out: TranslationDetails = {}  # type: ignore[typeddict-item]
    if data.get("Locality") is not None:
        import capo_geo_places.types.admin_names_list

        out["locality"] = capo_geo_places.types.admin_names_list.deserialize_json(
            data["Locality"]
        )
    if data.get("Region") is not None:
        import capo_geo_places.types.admin_names_list

        out["region"] = capo_geo_places.types.admin_names_list.deserialize_json(
            data["Region"]
        )
    if data.get("District") is not None:
        import capo_geo_places.types.admin_names_list

        out["district"] = capo_geo_places.types.admin_names_list.deserialize_json(
            data["District"]
        )
    if data.get("SubRegion") is not None:
        import capo_geo_places.types.admin_names_list

        out["sub_region"] = capo_geo_places.types.admin_names_list.deserialize_json(
            data["SubRegion"]
        )
    return out


def redact_sensitive(value: TranslationDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "locality" in value:
        import capo_geo_places.types.admin_names_list

        out["locality"] = capo_geo_places.types.admin_names_list.redact_sensitive(
            value["locality"]
        )
    if "region" in value:
        import capo_geo_places.types.admin_names_list

        out["region"] = capo_geo_places.types.admin_names_list.redact_sensitive(
            value["region"]
        )
    if "district" in value:
        import capo_geo_places.types.admin_names_list

        out["district"] = capo_geo_places.types.admin_names_list.redact_sensitive(
            value["district"]
        )
    if "sub_region" in value:
        import capo_geo_places.types.admin_names_list

        out["sub_region"] = capo_geo_places.types.admin_names_list.redact_sensitive(
            value["sub_region"]
        )
    return out
