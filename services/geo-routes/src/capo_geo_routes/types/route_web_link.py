"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWebLink``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_web_link_device_type
    import capo_geo_routes.types.sensitive_string


class RouteWebLink(TypedDict, closed=True):
    anchor_text: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The interactive or clickable portion of the text.</p>"""
    description: "capo_geo_routes.types.sensitive_string.SensitiveString"
    """<p>Text describing the URL.</p>"""
    device_type: NotRequired[
        "capo_geo_routes.types.route_web_link_device_type.RouteWebLinkDeviceType"
    ]
    """<p>Device type for which the link is intended.</p>"""
    url: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The URL of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteWebLink) -> dict:
    out: dict = {}
    if "anchor_text" in value:
        out["AnchorText"] = value["anchor_text"]
    out["Description"] = value["description"]
    if "device_type" in value:
        import capo_geo_routes.types.route_web_link_device_type

        out["DeviceType"] = (
            capo_geo_routes.types.route_web_link_device_type.serialize_json(
                value["device_type"]
            )
        )
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RouteWebLink:
    out: RouteWebLink = {}  # type: ignore[typeddict-item]
    if data.get("AnchorText") is not None:
        out["anchor_text"] = data["AnchorText"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("DeviceType") is not None:
        import capo_geo_routes.types.route_web_link_device_type

        out["device_type"] = (
            capo_geo_routes.types.route_web_link_device_type.deserialize_json(
                data["DeviceType"]
            )
        )
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out


def redact_sensitive(value: RouteWebLink) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "anchor_text" in value:
        out["anchor_text"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "device_type" in value:
        out["device_type"] = "*** Sensitive Data Redacted ***"
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
