"""Generated from Smithy shape ``com.amazonaws.location#CreateGeofenceCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.arn
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class CreateGeofenceCollectionResponse(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name for the geofence collection.</p>"""
    collection_arn: "capo_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all Amazon Web Services. </p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection</code> </p> </li> </ul>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence collection was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGeofenceCollectionResponse) -> dict:
    out: dict = {}
    out["CollectionName"] = value["collection_name"]
    out["CollectionArn"] = value["collection_arn"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateGeofenceCollectionResponse:
    out: CreateGeofenceCollectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("CollectionName") is not None:
        out["collection_name"] = data["CollectionName"]
    else:
        raise DeserializationError(
            "CreateGeofenceCollectionResponse.collection_name required"
        )
    if data.get("CollectionArn") is not None:
        out["collection_arn"] = data["CollectionArn"]
    else:
        raise DeserializationError(
            "CreateGeofenceCollectionResponse.collection_arn required"
        )
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError(
            "CreateGeofenceCollectionResponse.create_time required"
        )
    return out
