"""Generated from Smithy shape ``com.amazonaws.geoplaces#AdminNames``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.admin_names_preference
    import capo_geo_places.types.translation_name_list


class AdminNames(TypedDict, closed=True):
    names: "capo_geo_places.types.translation_name_list.TranslationNameList"
    """<p>A list of translation names for the administrative address component, including name variants and translations in available languages.</p>"""
    preference: NotRequired[
        "capo_geo_places.types.admin_names_preference.AdminNamesPreference"
    ]
    """<p>Indicates the preference level of the administrative name. Valid values are <code>Primary</code> and <code>Alternative</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminNames) -> dict:
    out: dict = {}
    import capo_geo_places.types.translation_name_list

    out["Names"] = capo_geo_places.types.translation_name_list.serialize_json(
        value["names"]
    )
    if "preference" in value:
        import capo_geo_places.types.admin_names_preference

        out["Preference"] = capo_geo_places.types.admin_names_preference.serialize_json(
            value["preference"]
        )
    return out


def deserialize_json(data: dict) -> AdminNames:
    out: AdminNames = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_geo_places.types.translation_name_list

        out["names"] = capo_geo_places.types.translation_name_list.deserialize_json(
            data["Names"]
        )
    else:
        out["names"] = []
    if data.get("Preference") is not None:
        import capo_geo_places.types.admin_names_preference

        out["preference"] = (
            capo_geo_places.types.admin_names_preference.deserialize_json(
                data["Preference"]
            )
        )
    return out


def redact_sensitive(value: AdminNames) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "names" in value:
        import capo_geo_places.types.translation_name_list

        out["names"] = capo_geo_places.types.translation_name_list.redact_sensitive(
            value["names"]
        )
    return out
