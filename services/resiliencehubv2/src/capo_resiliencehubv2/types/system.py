"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#System``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.kms_key_id
    import capo_resiliencehubv2.types.organization_id
    import capo_resiliencehubv2.types.ou_id
    import capo_resiliencehubv2.types.system_id
    import capo_resiliencehubv2.types.tag_map


class System(TypedDict, closed=True):
    system_arn: "capo_resiliencehubv2.types.arn.Arn"
    system_id: "capo_resiliencehubv2.types.system_id.SystemId"
    name: "capo_resiliencehubv2.types.entity_name.EntityName"
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    sharing_enabled: NotRequired["bool"]
    """<p>Indicates whether cross-account sharing is enabled.</p>"""
    tags: NotRequired["capo_resiliencehubv2.types.tag_map.TagMap"]
    kms_key_id: NotRequired["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    organization_id: NotRequired[
        "capo_resiliencehubv2.types.organization_id.OrganizationId"
    ]
    """<p>The AWS Organizations identifier for the system.</p>"""
    ou_id: NotRequired["capo_resiliencehubv2.types.ou_id.OuId"]
    """<p>The organizational unit (OU) identifier for the system.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the system was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the system was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: System) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    out["systemId"] = value["system_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sharing_enabled" in value:
        out["sharingEnabled"] = value["sharing_enabled"]
    if "tags" in value:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.serialize_json(value["tags"])
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    if "ou_id" in value:
        out["ouId"] = value["ou_id"]
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> System:
    out: System = {}  # type: ignore[typeddict-item]
    if data.get("systemArn") is not None:
        out["system_arn"] = data["systemArn"]
    else:
        out["system_arn"] = ""
    if data.get("systemId") is not None:
        out["system_id"] = data["systemId"]
    else:
        out["system_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("sharingEnabled") is not None:
        out["sharing_enabled"] = data["sharingEnabled"]
    if data.get("tags") is not None:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.deserialize_json(data["tags"])
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("organizationId") is not None:
        out["organization_id"] = data["organizationId"]
    if data.get("ouId") is not None:
        out["ou_id"] = data["ouId"]
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out


def redact_sensitive(value: System) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
