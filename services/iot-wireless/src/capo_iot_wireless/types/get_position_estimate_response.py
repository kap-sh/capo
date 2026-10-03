"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetPositionEstimateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.geo_json_payload


class GetPositionEstimateResponse(TypedDict, closed=True):
    geo_json_payload: NotRequired[
        "capo_iot_wireless.types.geo_json_payload.GeoJsonPayload"
    ]
    """<p>The position information of the resource, displayed as a JSON payload. The payload is of type blob and uses the <a href="https://geojson.org/">GeoJSON</a> format, which a format that's used to encode geographic data structures. A sample payload contains the timestamp information, the WGS84 coordinates of the location, and the accuracy and confidence level. For more information and examples, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/location-resolve-console.html">Resolve device location (console)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPositionEstimateResponse) -> dict:
    out: dict = {}
    if "geo_json_payload" in value:
        import capo_iot_wireless.types.geo_json_payload

        out["GeoJsonPayload"] = capo_iot_wireless.types.geo_json_payload.serialize_json(
            value["geo_json_payload"]
        )
    return out


def deserialize_json(data: dict) -> GetPositionEstimateResponse:
    out: GetPositionEstimateResponse = {}  # type: ignore[typeddict-item]
    if data.get("GeoJsonPayload") is not None:
        import capo_iot_wireless.types.geo_json_payload

        out["geo_json_payload"] = (
            capo_iot_wireless.types.geo_json_payload.deserialize_json(
                data["GeoJsonPayload"]
            )
        )
    return out
