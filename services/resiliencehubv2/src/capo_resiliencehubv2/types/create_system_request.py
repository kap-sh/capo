"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateSystemRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.kms_key_id
    import capo_resiliencehubv2.types.tag_map


class CreateSystemRequest(TypedDict, closed=True):
    name: "capo_resiliencehubv2.types.entity_name.EntityName"
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    sharing_enabled: NotRequired["bool"]
    """<p>Indicates whether cross-account sharing is enabled for the system.</p>"""
    kms_key_id: NotRequired["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    tags: NotRequired["capo_resiliencehubv2.types.tag_map.TagMap"]
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateSystemRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sharing_enabled" in value:
        out["sharingEnabled"] = value["sharing_enabled"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSystemRequest:
    out: CreateSystemRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSystemRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("sharingEnabled") is not None:
        out["sharing_enabled"] = data["sharingEnabled"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateSystemRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
