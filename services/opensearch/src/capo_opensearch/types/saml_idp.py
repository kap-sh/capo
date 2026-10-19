"""Generated from Smithy shape ``com.amazonaws.opensearch#SAMLIdp``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.saml_entity_id
    import capo_opensearch.types.saml_metadata


class SAMLIdp(TypedDict, closed=True):
    metadata_content: "capo_opensearch.types.saml_metadata.SAMLMetadata"
    """<p>The metadata of the SAML application, in XML format.</p>"""
    entity_id: "capo_opensearch.types.saml_entity_id.SAMLEntityId"
    """<p>The unique entity ID of the application in the SAML identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAMLIdp) -> dict:
    out: dict = {}
    out["MetadataContent"] = value["metadata_content"]
    out["EntityId"] = value["entity_id"]
    return out


def deserialize_json(data: dict) -> SAMLIdp:
    out: SAMLIdp = {}  # type: ignore[typeddict-item]
    if data.get("MetadataContent") is not None:
        out["metadata_content"] = data["MetadataContent"]
    else:
        out["metadata_content"] = ""
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    else:
        out["entity_id"] = ""
    return out
