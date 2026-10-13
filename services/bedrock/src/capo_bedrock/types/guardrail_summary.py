"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_arn
    import capo_bedrock.types.guardrail_cross_region_details
    import capo_bedrock.types.guardrail_description
    import capo_bedrock.types.guardrail_id
    import capo_bedrock.types.guardrail_name
    import capo_bedrock.types.guardrail_status
    import capo_bedrock.types.guardrail_version
    import capo_bedrock.types.timestamp


class GuardrailSummary(TypedDict, closed=True):
    id: "capo_bedrock.types.guardrail_id.GuardrailId"
    """<p>The unique identifier of the guardrail.</p>"""
    arn: "capo_bedrock.types.guardrail_arn.GuardrailArn"
    """<p>The ARN of the guardrail.</p>"""
    status: "capo_bedrock.types.guardrail_status.GuardrailStatus"
    """<p>The status of the guardrail.</p>"""
    name: "capo_bedrock.types.guardrail_name.GuardrailName"
    """<p>The name of the guardrail.</p>"""
    description: NotRequired[
        "capo_bedrock.types.guardrail_description.GuardrailDescription"
    ]
    """<p>A description of the guardrail.</p>"""
    version: "capo_bedrock.types.guardrail_version.GuardrailVersion"
    """<p>The version of the guardrail.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was created.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was last updated.</p>"""
    cross_region_details: NotRequired[
        "capo_bedrock.types.guardrail_cross_region_details.GuardrailCrossRegionDetails"
    ]
    """<p>Details about the system-defined guardrail profile that you're using with your guardrail, including the guardrail profile ID and Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_bedrock.types.guardrail_status

    out["status"] = capo_bedrock.types.guardrail_status.serialize_json(value["status"])
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["version"] = value["version"]
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
    if "cross_region_details" in value:
        import capo_bedrock.types.guardrail_cross_region_details

        out["crossRegionDetails"] = (
            capo_bedrock.types.guardrail_cross_region_details.serialize_json(
                value["cross_region_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailSummary:
    out: GuardrailSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GuardrailSummary.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GuardrailSummary.arn required")
    if data.get("status") is not None:
        import capo_bedrock.types.guardrail_status

        out["status"] = capo_bedrock.types.guardrail_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GuardrailSummary.status required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GuardrailSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("GuardrailSummary.version required")
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GuardrailSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GuardrailSummary.updated_at required")
    if data.get("crossRegionDetails") is not None:
        import capo_bedrock.types.guardrail_cross_region_details

        out["cross_region_details"] = (
            capo_bedrock.types.guardrail_cross_region_details.deserialize_json(
                data["crossRegionDetails"]
            )
        )
    return out


def redact_sensitive(value: GuardrailSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
