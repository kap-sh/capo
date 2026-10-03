"""Generated from Smithy shape ``com.amazonaws.location#CreateTrackerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.arn
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class CreateTrackerResponse(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource.</p>"""
    tracker_arn: "capo_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the tracker resource. Used when you need to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:tracker/ExampleTracker</code> </p> </li> </ul>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the tracker resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrackerResponse) -> dict:
    out: dict = {}
    out["TrackerName"] = value["tracker_name"]
    out["TrackerArn"] = value["tracker_arn"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateTrackerResponse:
    out: CreateTrackerResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrackerName") is not None:
        out["tracker_name"] = data["TrackerName"]
    else:
        raise DeserializationError("CreateTrackerResponse.tracker_name required")
    if data.get("TrackerArn") is not None:
        out["tracker_arn"] = data["TrackerArn"]
    else:
        raise DeserializationError("CreateTrackerResponse.tracker_arn required")
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("CreateTrackerResponse.create_time required")
    return out
