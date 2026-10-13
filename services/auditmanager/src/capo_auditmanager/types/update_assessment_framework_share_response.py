"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkShareResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_framework_share_request


class UpdateAssessmentFrameworkShareResponse(TypedDict, closed=True):
    assessment_framework_share_request: NotRequired[
        "capo_auditmanager.types.assessment_framework_share_request.AssessmentFrameworkShareRequest"
    ]
    """<p> The updated share request that's returned by the <code>UpdateAssessmentFrameworkShare</code> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkShareResponse) -> dict:
    out: dict = {}
    if "assessment_framework_share_request" in value:
        import capo_auditmanager.types.assessment_framework_share_request

        out["assessmentFrameworkShareRequest"] = (
            capo_auditmanager.types.assessment_framework_share_request.serialize_json(
                value["assessment_framework_share_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentFrameworkShareResponse:
    out: UpdateAssessmentFrameworkShareResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessmentFrameworkShareRequest") is not None:
        import capo_auditmanager.types.assessment_framework_share_request

        out["assessment_framework_share_request"] = (
            capo_auditmanager.types.assessment_framework_share_request.deserialize_json(
                data["assessmentFrameworkShareRequest"]
            )
        )
    return out


def redact_sensitive(value: UpdateAssessmentFrameworkShareResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment_framework_share_request" in value:
        import capo_auditmanager.types.assessment_framework_share_request

        out["assessment_framework_share_request"] = (
            capo_auditmanager.types.assessment_framework_share_request.redact_sensitive(
                value["assessment_framework_share_request"]
            )
        )
    return out
