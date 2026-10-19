"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetSecurityRequirementResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.security_requirement_name
    import capo_securityagent.types.security_requirement_pack_id


class BatchGetSecurityRequirementResult(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the pack containing the security requirement.</p>"""
    name: "capo_securityagent.types.security_requirement_name.SecurityRequirementName"
    """<p>The name of the security requirement.</p>"""
    description: "str"
    """<p>A description of the security requirement.</p>"""
    domain: "str"
    """<p>The security domain the requirement belongs to.</p>"""
    evaluation: "str"
    """<p>The evaluation criteria used to assess compliance with this requirement.</p>"""
    remediation: NotRequired["str"]
    """<p>The recommended remediation steps when the requirement is not met.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the security requirement was created, in UTC format.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time the security requirement was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSecurityRequirementResult) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["domain"] = value["domain"]
    out["evaluation"] = value["evaluation"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    import capo_securityagent._protocol.serialize

    out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_securityagent._protocol.serialize

    out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetSecurityRequirementResult:
    out: BatchGetSecurityRequirementResult = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("evaluation") is not None:
        out["evaluation"] = data["evaluation"]
    else:
        out["evaluation"] = ""
    if data.get("remediation") is not None:
        out["remediation"] = data["remediation"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
