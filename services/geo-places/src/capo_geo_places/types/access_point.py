"""Generated from Smithy shape ``com.amazonaws.geoplaces#AccessPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.access_point_type
    import capo_geo_places.types.position
    import capo_geo_places.types.sensitive_boolean
    import capo_geo_places.types.sensitive_string


class AccessPoint(TypedDict, closed=True):
    position: NotRequired["capo_geo_places.types.position.Position"]
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    type: NotRequired["capo_geo_places.types.access_point_type.AccessPointType"]
    """<p>The type of access point, indicating its intended use. Only applies to results of type place.</p>"""
    primary: NotRequired["capo_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Set to <code>true</code> for the primary access position when the place has more than one access point.</p>"""
    label: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>A short textual description of the access point, such as <code>"North Entrance"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPoint) -> dict:
    out: dict = {}
    if "position" in value:
        import capo_geo_places.types.position

        out["Position"] = capo_geo_places.types.position.serialize_json(
            value["position"]
        )
    if "type" in value:
        import capo_geo_places.types.access_point_type

        out["Type"] = capo_geo_places.types.access_point_type.serialize_json(
            value["type"]
        )
    if "primary" in value:
        out["Primary"] = value["primary"]
    if "label" in value:
        out["Label"] = value["label"]
    return out


def deserialize_json(data: dict) -> AccessPoint:
    out: AccessPoint = {}  # type: ignore[typeddict-item]
    if data.get("Position") is not None:
        import capo_geo_places.types.position

        out["position"] = capo_geo_places.types.position.deserialize_json(
            data["Position"]
        )
    if data.get("Type") is not None:
        import capo_geo_places.types.access_point_type

        out["type"] = capo_geo_places.types.access_point_type.deserialize_json(
            data["Type"]
        )
    if data.get("Primary") is not None:
        out["primary"] = data["Primary"]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    return out
