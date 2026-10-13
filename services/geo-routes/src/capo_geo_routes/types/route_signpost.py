"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSignpost``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_signpost_label_list


class RouteSignpost(TypedDict, closed=True):
    labels: "capo_geo_routes.types.route_signpost_label_list.RouteSignpostLabelList"
    """<p>Labels present on the sign post.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSignpost) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_signpost_label_list

    out["Labels"] = capo_geo_routes.types.route_signpost_label_list.serialize_json(
        value["labels"]
    )
    return out


def deserialize_json(data: dict) -> RouteSignpost:
    out: RouteSignpost = {}  # type: ignore[typeddict-item]
    if data.get("Labels") is not None:
        import capo_geo_routes.types.route_signpost_label_list

        out["labels"] = (
            capo_geo_routes.types.route_signpost_label_list.deserialize_json(
                data["Labels"]
            )
        )
    else:
        raise DeserializationError("RouteSignpost.labels required")
    return out


def redact_sensitive(value: RouteSignpost) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "labels" in value:
        import capo_geo_routes.types.route_signpost_label_list

        out["labels"] = (
            capo_geo_routes.types.route_signpost_label_list.redact_sensitive(
                value["labels"]
            )
        )
    return out
