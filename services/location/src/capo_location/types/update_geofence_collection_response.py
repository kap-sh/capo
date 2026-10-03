"""Generated from Smithy shape ``com.amazonaws.location#UpdateGeofenceCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.arn
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class UpdateGeofenceCollectionResponse(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the updated geofence collection.</p>"""
    collection_arn: "capo_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the updated geofence collection. Used to specify a resource across Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection</code> </p> </li> </ul>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The time when the geofence collection was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGeofenceCollectionResponse) -> dict:
    out: dict = {}
    out["CollectionName"] = value["collection_name"]
    out["CollectionArn"] = value["collection_arn"]
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateGeofenceCollectionResponse:
    out: UpdateGeofenceCollectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("CollectionName") is not None:
        out["collection_name"] = data["CollectionName"]
    else:
        raise DeserializationError(
            "UpdateGeofenceCollectionResponse.collection_name required"
        )
    if data.get("CollectionArn") is not None:
        out["collection_arn"] = data["CollectionArn"]
    else:
        raise DeserializationError(
            "UpdateGeofenceCollectionResponse.collection_arn required"
        )
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError(
            "UpdateGeofenceCollectionResponse.update_time required"
        )
    return out
