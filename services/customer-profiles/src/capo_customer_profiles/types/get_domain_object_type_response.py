"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetDomainObjectTypeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.domain_object_type_fields
    import capo_customer_profiles.types.encryption_key
    import capo_customer_profiles.types.sensitive_string1_to10000
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.type_name


class GetDomainObjectTypeResponse(TypedDict, closed=True):
    object_type_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the domain object type.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to10000.sensitiveString1To10000"
    ]
    """<p>The description of the domain object type.</p>"""
    encryption_key: NotRequired[
        "capo_customer_profiles.types.encryption_key.encryptionKey"
    ]
    """<p>The customer provided KMS key used to encrypt this type of domain object.</p>"""
    fields: NotRequired[
        "capo_customer_profiles.types.domain_object_type_fields.DomainObjectTypeFields"
    ]
    """<p>A map of field names to their corresponding domain object type field definitions.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the domain object type was created.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the domain object type was most recently edited.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainObjectTypeResponse) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "encryption_key" in value:
        out["EncryptionKey"] = value["encryption_key"]
    if "fields" in value:
        import capo_customer_profiles.types.domain_object_type_fields

        out["Fields"] = (
            capo_customer_profiles.types.domain_object_type_fields.serialize_json(
                value["fields"]
            )
        )
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


def deserialize_json(data: dict) -> GetDomainObjectTypeResponse:
    out: GetDomainObjectTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("ObjectTypeName") is not None:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        raise DeserializationError(
            "GetDomainObjectTypeResponse.object_type_name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EncryptionKey") is not None:
        out["encryption_key"] = data["EncryptionKey"]
    if data.get("Fields") is not None:
        import capo_customer_profiles.types.domain_object_type_fields

        out["fields"] = (
            capo_customer_profiles.types.domain_object_type_fields.deserialize_json(
                data["Fields"]
            )
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


def redact_sensitive(value: GetDomainObjectTypeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
