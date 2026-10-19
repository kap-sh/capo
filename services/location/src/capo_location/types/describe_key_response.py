"""Generated from Smithy shape ``com.amazonaws.location#DescribeKeyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.api_key_restrictions
    import capo_location.types.arn
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map
    import capo_location.types.timestamp


class DescribeKeyResponse(TypedDict, closed=True):
    key: "capo_location.types.api_key.ApiKey"
    """<p>The key value/string of an API key.</p>"""
    key_arn: "capo_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:key/ExampleKey</code> </p> </li> </ul>"""
    key_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the API key resource.</p>"""
    restrictions: "capo_location.types.api_key_restrictions.ApiKeyRestrictions"
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the API key resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    expire_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the API key resource was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    description: NotRequired[
        "capo_location.types.resource_description.ResourceDescription"
    ]
    """<p>The optional description for the API key resource.</p>"""
    tags: NotRequired["capo_location.types.tag_map.TagMap"]
    """<p>Tags associated with the API key resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeKeyResponse) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["KeyArn"] = value["key_arn"]
    out["KeyName"] = value["key_name"]
    import capo_location.types.api_key_restrictions

    out["Restrictions"] = capo_location.types.api_key_restrictions.serialize_json(
        value["restrictions"]
    )
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_location.types.timestamp

    out["ExpireTime"] = capo_location.types.timestamp.serialize_json(
        value["expire_time"]
    )
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_location.types.tag_map

        out["Tags"] = capo_location.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeKeyResponse:
    out: DescribeKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        out["key_arn"] = ""
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    else:
        out["key_name"] = ""
    if data.get("Restrictions") is not None:
        import capo_location.types.api_key_restrictions

        out["restrictions"] = capo_location.types.api_key_restrictions.deserialize_json(
            data["Restrictions"]
        )
    else:
        raise DeserializationError("DescribeKeyResponse.restrictions required")
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ExpireTime") is not None:
        import capo_location.types.timestamp

        out["expire_time"] = capo_location.types.timestamp.deserialize_json(
            data["ExpireTime"]
        )
    else:
        import datetime

        out["expire_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_location.types.tag_map

        out["tags"] = capo_location.types.tag_map.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: DescribeKeyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key" in value:
        out["key"] = "*** Sensitive Data Redacted ***"
    if "restrictions" in value:
        import capo_location.types.api_key_restrictions

        out["restrictions"] = capo_location.types.api_key_restrictions.redact_sensitive(
            value["restrictions"]
        )
    if "create_time" in value:
        out["create_time"] = "*** Sensitive Data Redacted ***"
    if "expire_time" in value:
        out["expire_time"] = "*** Sensitive Data Redacted ***"
    if "update_time" in value:
        out["update_time"] = "*** Sensitive Data Redacted ***"
    return out
