"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.destination_type
    import capo_cloudtrail.types.location


class Destination(TypedDict, closed=True):
    type: "capo_cloudtrail.types.destination_type.DestinationType"
    """<p>The type of destination for events arriving from a channel. For channels used for a CloudTrail Lake integration, the value is <code>EVENT_DATA_STORE</code>. For service-linked channels, the value is <code>AWS_SERVICE</code>. </p>"""
    location: "capo_cloudtrail.types.location.Location"
    """<p> For channels used for a CloudTrail Lake integration, the location is the ARN of an event data store that receives events from a channel. For service-linked channels, the location is the name of the Amazon Web Services service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Destination) -> dict:
    out: dict = {}
    import capo_cloudtrail.types.destination_type

    out["Type"] = capo_cloudtrail.types.destination_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_cloudtrail.types.destination_type

        out["type"] = capo_cloudtrail.types.destination_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cloudtrail.types.destination_type.DestinationType", ""
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    else:
        out["location"] = ""
    return out
