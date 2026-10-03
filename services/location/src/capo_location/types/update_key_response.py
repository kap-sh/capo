"""Generated from Smithy shape ``com.amazonaws.location#UpdateKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.arn
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class UpdateKeyResponse(TypedDict, closed=True):
    key_arn: "capo_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:key/ExampleKey</code> </p> </li> </ul>"""
    key_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the API key resource.</p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the API key resource was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKeyResponse) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["KeyName"] = value["key_name"]
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateKeyResponse:
    out: UpdateKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        raise DeserializationError("UpdateKeyResponse.key_arn required")
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    else:
        raise DeserializationError("UpdateKeyResponse.key_name required")
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("UpdateKeyResponse.update_time required")
    return out
