"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationExclusionOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.country_code_list


class WaypointOptimizationExclusionOptions(TypedDict, closed=True):
    countries: "capo_geo_routes.types.country_code_list.CountryCodeList"
    """<p>List of countries to be avoided defined by two-letter or three-letter country codes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationExclusionOptions) -> dict:
    out: dict = {}
    import capo_geo_routes.types.country_code_list

    out["Countries"] = capo_geo_routes.types.country_code_list.serialize_json(
        value["countries"]
    )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationExclusionOptions:
    out: WaypointOptimizationExclusionOptions = {}  # type: ignore[typeddict-item]
    if data.get("Countries") is not None:
        import capo_geo_routes.types.country_code_list

        out["countries"] = capo_geo_routes.types.country_code_list.deserialize_json(
            data["Countries"]
        )
    else:
        out["countries"] = []
    return out


def redact_sensitive(value: WaypointOptimizationExclusionOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "countries" in value:
        import capo_geo_routes.types.country_code_list

        out["countries"] = capo_geo_routes.types.country_code_list.redact_sensitive(
            value["countries"]
        )
    return out
