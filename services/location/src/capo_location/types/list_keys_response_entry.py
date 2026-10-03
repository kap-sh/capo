"""Generated from Smithy shape ``com.amazonaws.location#ListKeysResponseEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.api_key_restrictions
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class ListKeysResponseEntry(TypedDict, closed=True):
    key_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the API key resource.</p>"""
    expire_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the API key resource will expire, in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""
    description: NotRequired[
        "capo_location.types.resource_description.ResourceDescription"
    ]
    """<p>The optional description for the API key resource.</p>"""
    restrictions: "capo_location.types.api_key_restrictions.ApiKeyRestrictions"
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp of when the API key was created, in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp of when the API key was last updated, in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKeysResponseEntry) -> dict:
    out: dict = {}
    out["KeyName"] = value["key_name"]
    import capo_location.types.timestamp

    out["ExpireTime"] = capo_location.types.timestamp.serialize_json(
        value["expire_time"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_location.types.api_key_restrictions

    out["Restrictions"] = capo_location.types.api_key_restrictions.serialize_json(
        value["restrictions"]
    )
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> ListKeysResponseEntry:
    out: ListKeysResponseEntry = {}  # type: ignore[typeddict-item]
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    else:
        raise DeserializationError("ListKeysResponseEntry.key_name required")
    if data.get("ExpireTime") is not None:
        import capo_location.types.timestamp

        out["expire_time"] = capo_location.types.timestamp.deserialize_json(
            data["ExpireTime"]
        )
    else:
        raise DeserializationError("ListKeysResponseEntry.expire_time required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Restrictions") is not None:
        import capo_location.types.api_key_restrictions

        out["restrictions"] = capo_location.types.api_key_restrictions.deserialize_json(
            data["Restrictions"]
        )
    else:
        raise DeserializationError("ListKeysResponseEntry.restrictions required")
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("ListKeysResponseEntry.create_time required")
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("ListKeysResponseEntry.update_time required")
    return out
