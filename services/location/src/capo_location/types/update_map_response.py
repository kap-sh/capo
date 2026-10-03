"""Generated from Smithy shape ``com.amazonaws.location#UpdateMapResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.geo_arn
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class UpdateMapResponse(TypedDict, closed=True):
    map_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the updated map resource.</p>"""
    map_arn: "capo_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) of the updated map resource. Used to specify a resource across AWS.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:map/ExampleMap</code> </p> </li> </ul>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the map resource was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMapResponse) -> dict:
    out: dict = {}
    out["MapName"] = value["map_name"]
    out["MapArn"] = value["map_arn"]
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateMapResponse:
    out: UpdateMapResponse = {}  # type: ignore[typeddict-item]
    if data.get("MapName") is not None:
        out["map_name"] = data["MapName"]
    else:
        raise DeserializationError("UpdateMapResponse.map_name required")
    if data.get("MapArn") is not None:
        out["map_arn"] = data["MapArn"]
    else:
        raise DeserializationError("UpdateMapResponse.map_arn required")
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("UpdateMapResponse.update_time required")
    return out
