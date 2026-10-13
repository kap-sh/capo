"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAssessmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment
    import capo_auditmanager.types.role


class GetAssessmentResponse(TypedDict, closed=True):
    assessment: NotRequired["capo_auditmanager.types.assessment.Assessment"]
    user_role: NotRequired["capo_auditmanager.types.role.Role"]


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentResponse) -> dict:
    out: dict = {}
    if "assessment" in value:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.serialize_json(
            value["assessment"]
        )
    if "user_role" in value:
        import capo_auditmanager.types.role

        out["userRole"] = capo_auditmanager.types.role.serialize_json(
            value["user_role"]
        )
    return out


def deserialize_json(data: dict) -> GetAssessmentResponse:
    out: GetAssessmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessment") is not None:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.deserialize_json(
            data["assessment"]
        )
    if data.get("userRole") is not None:
        import capo_auditmanager.types.role

        out["user_role"] = capo_auditmanager.types.role.deserialize_json(
            data["userRole"]
        )
    return out


def redact_sensitive(value: GetAssessmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment" in value:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.redact_sensitive(
            value["assessment"]
        )
    return out
