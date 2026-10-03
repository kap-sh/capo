"""Generated from Smithy shape ``com.amazonaws.location#CreatePlaceIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.geo_arn
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class CreatePlaceIndexResponse(TypedDict, closed=True):
    index_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name for the place index resource.</p>"""
    index_arn: "capo_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across Amazon Web Services. </p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:place-index/ExamplePlaceIndex</code> </p> </li> </ul>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the place index resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePlaceIndexResponse) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    out["IndexArn"] = value["index_arn"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    return out


def deserialize_json(data: dict) -> CreatePlaceIndexResponse:
    out: CreatePlaceIndexResponse = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError("CreatePlaceIndexResponse.index_name required")
    if data.get("IndexArn") is not None:
        out["index_arn"] = data["IndexArn"]
    else:
        raise DeserializationError("CreatePlaceIndexResponse.index_arn required")
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("CreatePlaceIndexResponse.create_time required")
    return out
