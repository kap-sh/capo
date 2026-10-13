"""Generated from Smithy shape ``com.amazonaws.datazone#BatchPutAttributesMetadataInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.attribute_entity_type
    import capo_datazone.types.attributes
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.entity_id


class BatchPutAttributesMetadataInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The domain ID where you want to write the attribute metadata.</p>"""
    entity_type: "capo_datazone.types.attribute_entity_type.AttributeEntityType"
    """<p>The entity type for which you want to write the attribute metadata.</p>"""
    entity_identifier: "capo_datazone.types.entity_id.EntityId"
    """<p>The entity ID for which you want to write the attribute metadata.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""
    attributes: "capo_datazone.types.attributes.Attributes"
    """<p>The attributes of the metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAttributesMetadataInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_datazone.types.attributes

    out["attributes"] = capo_datazone.types.attributes.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutAttributesMetadataInput:
    out: BatchPutAttributesMetadataInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("attributes") is not None:
        import capo_datazone.types.attributes

        out["attributes"] = capo_datazone.types.attributes.deserialize_json(
            data["attributes"]
        )
    else:
        raise DeserializationError(
            "BatchPutAttributesMetadataInput.attributes required"
        )
    return out


def redact_sensitive(value: BatchPutAttributesMetadataInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attributes" in value:
        import capo_datazone.types.attributes

        out["attributes"] = capo_datazone.types.attributes.redact_sensitive(
            value["attributes"]
        )
    return out
