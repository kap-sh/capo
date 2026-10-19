"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateSecurityRequirementPackInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.kms_key_id
    import capo_securityagent.types.security_requirement_pack_name
    import capo_securityagent.types.security_requirement_pack_status
    import capo_securityagent.types.tag_map


class CreateSecurityRequirementPackInput(TypedDict, closed=True):
    name: "capo_securityagent.types.security_requirement_pack_name.SecurityRequirementPackName"
    """<p>The name of the security requirement pack.</p>"""
    description: NotRequired["str"]
    """<p>A description of the security requirement pack.</p>"""
    status: NotRequired[
        "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
    ]
    """<p>The status of the pack. Defaults to ENABLED if not provided.</p>"""
    kms_key_id: NotRequired["capo_securityagent.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the AWS KMS key used to encrypt pack contents.</p>"""
    tags: NotRequired["capo_securityagent.types.tag_map.TagMap"]
    """<p>The tags to associate with the security requirement pack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityRequirementPackInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_securityagent.types.security_requirement_pack_status

        out["status"] = (
            capo_securityagent.types.security_requirement_pack_status.serialize_json(
                value["status"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSecurityRequirementPackInput:
    out: CreateSecurityRequirementPackInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_securityagent.types.security_requirement_pack_status

        out["status"] = (
            capo_securityagent.types.security_requirement_pack_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.deserialize_json(data["tags"])
    return out
