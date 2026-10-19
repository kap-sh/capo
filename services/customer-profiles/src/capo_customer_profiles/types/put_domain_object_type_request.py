"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PutDomainObjectTypeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.domain_object_type_fields
    import capo_customer_profiles.types.encryption_key
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.sensitive_string1_to10000
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.type_name


class PutDomainObjectTypeRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
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
    fields: (
        "capo_customer_profiles.types.domain_object_type_fields.DomainObjectTypeFields"
    )
    """<p>A map of field names to their corresponding domain object type field definitions.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDomainObjectTypeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "encryption_key" in value:
        out["EncryptionKey"] = value["encryption_key"]
    import capo_customer_profiles.types.domain_object_type_fields

    out["Fields"] = (
        capo_customer_profiles.types.domain_object_type_fields.serialize_json(
            value["fields"]
        )
    )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PutDomainObjectTypeRequest:
    out: PutDomainObjectTypeRequest = {}  # type: ignore[typeddict-item]
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
    else:
        out["fields"] = {}
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: PutDomainObjectTypeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
