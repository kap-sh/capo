"""Generated from Smithy shape ``com.amazonaws.location#CreateKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.api_key_restrictions
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map
    import capo_location.types.timestamp


class CreateKeyRequest(TypedDict, closed=True):
    key_name: "capo_location.types.resource_name.ResourceName"
    """<p>A custom name for the API key resource.</p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). </p> </li> <li> <p>Must be a unique API key name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleAPIKey</code>.</p> </li> </ul>"""
    restrictions: "capo_location.types.api_key_restrictions.ApiKeyRestrictions"
    """<p>The API key restrictions for the API key resource.</p>"""
    description: NotRequired[
        "capo_location.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description for the API key resource.</p>"""
    expire_time: NotRequired["capo_location.types.timestamp.Timestamp"]
    """<p>The optional timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. One of <code>NoExpiry</code> or <code>ExpireTime</code> must be set.</p>"""
    no_expiry: NotRequired["bool"]
    """<p>Optionally set to <code>true</code> to set no expiration time for the API key. One of <code>NoExpiry</code> or <code>ExpireTime</code> must be set.</p>"""
    tags: NotRequired["capo_location.types.tag_map.TagMap"]
    """<p>Applies one or more tags to the map resource. A tag is a key-value pair that helps manage, identify, search, and filter your resources by labelling them.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKeyRequest) -> dict:
    out: dict = {}
    out["KeyName"] = value["key_name"]
    import capo_location.types.api_key_restrictions

    out["Restrictions"] = capo_location.types.api_key_restrictions.serialize_json(
        value["restrictions"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "expire_time" in value:
        import capo_location.types.timestamp

        out["ExpireTime"] = capo_location.types.timestamp.serialize_json(
            value["expire_time"]
        )
    if "no_expiry" in value:
        out["NoExpiry"] = value["no_expiry"]
    if "tags" in value:
        import capo_location.types.tag_map

        out["Tags"] = capo_location.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateKeyRequest:
    out: CreateKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    else:
        raise DeserializationError("CreateKeyRequest.key_name required")
    if data.get("Restrictions") is not None:
        import capo_location.types.api_key_restrictions

        out["restrictions"] = capo_location.types.api_key_restrictions.deserialize_json(
            data["Restrictions"]
        )
    else:
        raise DeserializationError("CreateKeyRequest.restrictions required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ExpireTime") is not None:
        import capo_location.types.timestamp

        out["expire_time"] = capo_location.types.timestamp.deserialize_json(
            data["ExpireTime"]
        )
    if data.get("NoExpiry") is not None:
        out["no_expiry"] = data["NoExpiry"]
    if data.get("Tags") is not None:
        import capo_location.types.tag_map

        out["tags"] = capo_location.types.tag_map.deserialize_json(data["Tags"])
    return out
