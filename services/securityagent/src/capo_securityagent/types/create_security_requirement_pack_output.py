"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateSecurityRequirementPackOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.kms_key_id
    import capo_securityagent.types.security_requirement_pack_id
    import capo_securityagent.types.security_requirement_pack_status


class CreateSecurityRequirementPackOutput(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the created security requirement pack.</p>"""
    status: "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
    """<p>The status of the created security requirement pack.</p>"""
    kms_key_id: NotRequired["capo_securityagent.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the AWS KMS key used to encrypt pack contents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityRequirementPackOutput) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    import capo_securityagent.types.security_requirement_pack_status

    out["status"] = (
        capo_securityagent.types.security_requirement_pack_status.serialize_json(
            value["status"]
        )
    )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> CreateSecurityRequirementPackOutput:
    out: CreateSecurityRequirementPackOutput = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    if data.get("status") is not None:
        import capo_securityagent.types.security_requirement_pack_status

        out["status"] = (
            capo_securityagent.types.security_requirement_pack_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus",
            "",
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
