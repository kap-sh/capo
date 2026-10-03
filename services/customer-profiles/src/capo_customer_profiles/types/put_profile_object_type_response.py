"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PutProfileObjectTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.boolean
    import capo_customer_profiles.types.encryption_key
    import capo_customer_profiles.types.expiration_days_integer
    import capo_customer_profiles.types.field_map
    import capo_customer_profiles.types.key_map
    import capo_customer_profiles.types.min_size0
    import capo_customer_profiles.types.min_size1
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.type_name


class PutProfileObjectTypeResponse(TypedDict, closed=True):
    object_type_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""
    description: "capo_customer_profiles.types.sensitive_text.sensitiveText"
    """<p>Description of the profile object type.</p>"""
    template_id: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>A unique identifier for the object template.</p>"""
    expiration_days: NotRequired[
        "capo_customer_profiles.types.expiration_days_integer.expirationDaysInteger"
    ]
    """<p>The number of days until the data in the object expires.</p>"""
    encryption_key: NotRequired[
        "capo_customer_profiles.types.encryption_key.encryptionKey"
    ]
    """<p>The customer-provided key to encrypt the profile object that will be created in this profile object type.</p>"""
    allow_profile_creation: "capo_customer_profiles.types.boolean.boolean"
    """<p>Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is <code>FALSE</code>. If the AllowProfileCreation flag is set to <code>FALSE</code>, then the service tries to fetch a standard profile and associate this object with the profile. If it is set to <code>TRUE</code>, and if no match is found, then the service creates a new standard profile.</p>"""
    source_last_updated_timestamp_format: NotRequired[
        "capo_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The format of your <code>sourceLastUpdatedTimestamp</code> that was previously set up in fields that were parsed using <a href="https://docs.oracle.com/javase/10/docs/api/java/text/SimpleDateFormat.html">SimpleDateFormat</a>. If you have <code>sourceLastUpdatedTimestamp</code> in your field, you must set up <code>sourceLastUpdatedTimestampFormat</code>.</p>"""
    max_profile_object_count: NotRequired[
        "capo_customer_profiles.types.min_size1.minSize1"
    ]
    """<p>The amount of profile object max count assigned to the object type.</p>"""
    max_available_profile_object_count: NotRequired[
        "capo_customer_profiles.types.min_size0.minSize0"
    ]
    """<p>The amount of provisioned profile object max count available.</p>"""
    source_priority: NotRequired["capo_customer_profiles.types.min_size1.minSize1"]
    """<p>An integer that determines the priority of this object type when data from multiple sources is ingested. Lower values take priority. Object types without a specified source priority default to the lowest priority.</p>"""
    fields: NotRequired["capo_customer_profiles.types.field_map.FieldMap"]
    """<p>A map of the name and ObjectType field.</p>"""
    keys: NotRequired["capo_customer_profiles.types.key_map.KeyMap"]
    """<p>A list of unique keys that can be used to map data to the profile.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the domain was created.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the domain was most recently edited.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutProfileObjectTypeResponse) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    out["Description"] = value["description"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "expiration_days" in value:
        out["ExpirationDays"] = value["expiration_days"]
    if "encryption_key" in value:
        out["EncryptionKey"] = value["encryption_key"]
    out["AllowProfileCreation"] = value.get("allow_profile_creation", False)
    if "source_last_updated_timestamp_format" in value:
        out["SourceLastUpdatedTimestampFormat"] = value[
            "source_last_updated_timestamp_format"
        ]
    if "max_profile_object_count" in value:
        out["MaxProfileObjectCount"] = value["max_profile_object_count"]
    if "max_available_profile_object_count" in value:
        out["MaxAvailableProfileObjectCount"] = value[
            "max_available_profile_object_count"
        ]
    if "source_priority" in value:
        out["SourcePriority"] = value["source_priority"]
    if "fields" in value:
        import capo_customer_profiles.types.field_map

        out["Fields"] = capo_customer_profiles.types.field_map.serialize_json(
            value["fields"]
        )
    if "keys" in value:
        import capo_customer_profiles.types.key_map

        out["Keys"] = capo_customer_profiles.types.key_map.serialize_json(value["keys"])
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PutProfileObjectTypeResponse:
    out: PutProfileObjectTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("ObjectTypeName") is not None:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        raise DeserializationError(
            "PutProfileObjectTypeResponse.object_type_name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("PutProfileObjectTypeResponse.description required")
    if data.get("TemplateId") is not None:
        out["template_id"] = data["TemplateId"]
    if data.get("ExpirationDays") is not None:
        out["expiration_days"] = data["ExpirationDays"]
    if data.get("EncryptionKey") is not None:
        out["encryption_key"] = data["EncryptionKey"]
    if data.get("AllowProfileCreation") is not None:
        out["allow_profile_creation"] = data["AllowProfileCreation"]
    else:
        out["allow_profile_creation"] = False
    if data.get("SourceLastUpdatedTimestampFormat") is not None:
        out["source_last_updated_timestamp_format"] = data[
            "SourceLastUpdatedTimestampFormat"
        ]
    if data.get("MaxProfileObjectCount") is not None:
        out["max_profile_object_count"] = data["MaxProfileObjectCount"]
    if data.get("MaxAvailableProfileObjectCount") is not None:
        out["max_available_profile_object_count"] = data[
            "MaxAvailableProfileObjectCount"
        ]
    if data.get("SourcePriority") is not None:
        out["source_priority"] = data["SourcePriority"]
    if data.get("Fields") is not None:
        import capo_customer_profiles.types.field_map

        out["fields"] = capo_customer_profiles.types.field_map.deserialize_json(
            data["Fields"]
        )
    if data.get("Keys") is not None:
        import capo_customer_profiles.types.key_map

        out["keys"] = capo_customer_profiles.types.key_map.deserialize_json(
            data["Keys"]
        )
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
