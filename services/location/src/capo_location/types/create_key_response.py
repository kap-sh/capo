"""Generated from Smithy shape ``com.amazonaws.location#CreateKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.arn
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class CreateKeyResponse(TypedDict, closed=True):
    key: "capo_location.types.api_key.ApiKey"
    """<p>The key value/string of an API key. This value is used when making API calls to authorize the call. For example, see <a href="https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapGlyphs.html">GetMapGlyphs</a>.</p>"""
    key_arn: "capo_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:key/ExampleKey</code> </p> </li> </ul>"""
    key_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the API key resource.</p>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the API key resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKeyResponse) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["KeyArn"] = value["key_arn"]
    out["KeyName"] = value["key_name"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateKeyResponse:
    out: CreateKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("CreateKeyResponse.key required")
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        raise DeserializationError("CreateKeyResponse.key_arn required")
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    else:
        raise DeserializationError("CreateKeyResponse.key_name required")
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("CreateKeyResponse.create_time required")
    return out
