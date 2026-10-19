"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateGuardrailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_arn
    import capo_bedrock.types.guardrail_draft_version
    import capo_bedrock.types.guardrail_id
    import capo_bedrock.types.timestamp


class CreateGuardrailResponse(TypedDict, closed=True):
    guardrail_id: "capo_bedrock.types.guardrail_id.GuardrailId"
    """<p>The unique identifier of the guardrail that was created.</p>"""
    guardrail_arn: "capo_bedrock.types.guardrail_arn.GuardrailArn"
    """<p>The ARN of the guardrail.</p>"""
    version: "capo_bedrock.types.guardrail_draft_version.GuardrailDraftVersion"
    """<p>The version of the guardrail that was created. This value will always be <code>DRAFT</code>.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The time at which the guardrail was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGuardrailResponse) -> dict:
    out: dict = {}
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailArn"] = value["guardrail_arn"]
    out["version"] = value["version"]
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    return out


def deserialize_json(data: dict) -> CreateGuardrailResponse:
    out: CreateGuardrailResponse = {}  # type: ignore[typeddict-item]
    if data.get("guardrailId") is not None:
        out["guardrail_id"] = data["guardrailId"]
    else:
        out["guardrail_id"] = ""
    if data.get("guardrailArn") is not None:
        out["guardrail_arn"] = data["guardrailArn"]
    else:
        out["guardrail_arn"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
