"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetResourcePositionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.geo_json_payload


class GetResourcePositionResponse(TypedDict, closed=True):
    geo_json_payload: NotRequired[
        "capo_iot_wireless.types.geo_json_payload.GeoJsonPayload"
    ]
    """<p>The position information of the resource, displayed as a JSON payload. The payload uses the GeoJSON format, which a format that's used to encode geographic data structures. For more information, see <a href="https://geojson.org/">GeoJSON</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePositionResponse) -> dict:
    out: dict = {}
    if "geo_json_payload" in value:
        import capo_iot_wireless.types.geo_json_payload

        out["GeoJsonPayload"] = capo_iot_wireless.types.geo_json_payload.serialize_json(
            value["geo_json_payload"]
        )
    return out


def deserialize_json(data: dict) -> GetResourcePositionResponse:
    out: GetResourcePositionResponse = {}  # type: ignore[typeddict-item]
    if data.get("GeoJsonPayload") is not None:
        import capo_iot_wireless.types.geo_json_payload

        out["geo_json_payload"] = (
            capo_iot_wireless.types.geo_json_payload.deserialize_json(
                data["GeoJsonPayload"]
            )
        )
    return out
