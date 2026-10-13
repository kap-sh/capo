"""Generated from Smithy shape ``com.amazonaws.geoplaces#OpeningHours``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.category_list
    import capo_geo_places.types.opening_hours_components_list
    import capo_geo_places.types.opening_hours_display_list
    import capo_geo_places.types.sensitive_boolean


class OpeningHours(TypedDict, closed=True):
    display: NotRequired[
        "capo_geo_places.types.opening_hours_display_list.OpeningHoursDisplayList"
    ]
    """<p>List of opening hours in the format they are displayed in. This can vary by result and in most cases represents how the result uniquely formats their opening hours. </p>"""
    open_now: NotRequired["capo_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Boolean which indicates if the result/place is currently open. </p>"""
    components: NotRequired[
        "capo_geo_places.types.opening_hours_components_list.OpeningHoursComponentsList"
    ]
    """<p>Components of the opening hours object.</p>"""
    categories: NotRequired["capo_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong too.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpeningHours) -> dict:
    out: dict = {}
    if "display" in value:
        import capo_geo_places.types.opening_hours_display_list

        out["Display"] = (
            capo_geo_places.types.opening_hours_display_list.serialize_json(
                value["display"]
            )
        )
    if "open_now" in value:
        out["OpenNow"] = value["open_now"]
    if "components" in value:
        import capo_geo_places.types.opening_hours_components_list

        out["Components"] = (
            capo_geo_places.types.opening_hours_components_list.serialize_json(
                value["components"]
            )
        )
    if "categories" in value:
        import capo_geo_places.types.category_list

        out["Categories"] = capo_geo_places.types.category_list.serialize_json(
            value["categories"]
        )
    return out


def deserialize_json(data: dict) -> OpeningHours:
    out: OpeningHours = {}  # type: ignore[typeddict-item]
    if data.get("Display") is not None:
        import capo_geo_places.types.opening_hours_display_list

        out["display"] = (
            capo_geo_places.types.opening_hours_display_list.deserialize_json(
                data["Display"]
            )
        )
    if data.get("OpenNow") is not None:
        out["open_now"] = data["OpenNow"]
    if data.get("Components") is not None:
        import capo_geo_places.types.opening_hours_components_list

        out["components"] = (
            capo_geo_places.types.opening_hours_components_list.deserialize_json(
                data["Components"]
            )
        )
    if data.get("Categories") is not None:
        import capo_geo_places.types.category_list

        out["categories"] = capo_geo_places.types.category_list.deserialize_json(
            data["Categories"]
        )
    return out


def redact_sensitive(value: OpeningHours) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display" in value:
        import capo_geo_places.types.opening_hours_display_list

        out["display"] = (
            capo_geo_places.types.opening_hours_display_list.redact_sensitive(
                value["display"]
            )
        )
    if "open_now" in value:
        out["open_now"] = "*** Sensitive Data Redacted ***"
    if "components" in value:
        import capo_geo_places.types.opening_hours_components_list

        out["components"] = (
            capo_geo_places.types.opening_hours_components_list.redact_sensitive(
                value["components"]
            )
        )
    if "categories" in value:
        import capo_geo_places.types.category_list

        out["categories"] = capo_geo_places.types.category_list.redact_sensitive(
            value["categories"]
        )
    return out
