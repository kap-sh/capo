"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixExclusionOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.country_code_list


class RouteMatrixExclusionOptions(TypedDict, closed=True):
    countries: "capo_geo_routes.types.country_code_list.CountryCodeList"
    """<p>List of countries to be avoided defined by two-letter or three-letter country codes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixExclusionOptions) -> dict:
    out: dict = {}
    import capo_geo_routes.types.country_code_list

    out["Countries"] = capo_geo_routes.types.country_code_list.serialize_json(
        value["countries"]
    )
    return out


def deserialize_json(data: dict) -> RouteMatrixExclusionOptions:
    out: RouteMatrixExclusionOptions = {}  # type: ignore[typeddict-item]
    if data.get("Countries") is not None:
        import capo_geo_routes.types.country_code_list

        out["countries"] = capo_geo_routes.types.country_code_list.deserialize_json(
            data["Countries"]
        )
    else:
        raise DeserializationError("RouteMatrixExclusionOptions.countries required")
    return out


def redact_sensitive(value: RouteMatrixExclusionOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "countries" in value:
        import capo_geo_routes.types.country_code_list

        out["countries"] = capo_geo_routes.types.country_code_list.redact_sensitive(
            value["countries"]
        )
    return out
