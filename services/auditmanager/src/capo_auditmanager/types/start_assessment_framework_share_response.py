"""Generated from Smithy shape ``com.amazonaws.auditmanager#StartAssessmentFrameworkShareResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_framework_share_request


class StartAssessmentFrameworkShareResponse(TypedDict, closed=True):
    assessment_framework_share_request: NotRequired[
        "capo_auditmanager.types.assessment_framework_share_request.AssessmentFrameworkShareRequest"
    ]
    """<p> The share request that's created by the <code>StartAssessmentFrameworkShare</code> API. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAssessmentFrameworkShareResponse) -> dict:
    out: dict = {}
    if "assessment_framework_share_request" in value:
        import capo_auditmanager.types.assessment_framework_share_request

        out["assessmentFrameworkShareRequest"] = (
            capo_auditmanager.types.assessment_framework_share_request.serialize_json(
                value["assessment_framework_share_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartAssessmentFrameworkShareResponse:
    out: StartAssessmentFrameworkShareResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessmentFrameworkShareRequest") is not None:
        import capo_auditmanager.types.assessment_framework_share_request

        out["assessment_framework_share_request"] = (
            capo_auditmanager.types.assessment_framework_share_request.deserialize_json(
                data["assessmentFrameworkShareRequest"]
            )
        )
    return out


def redact_sensitive(value: StartAssessmentFrameworkShareResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment_framework_share_request" in value:
        import capo_auditmanager.types.assessment_framework_share_request

        out["assessment_framework_share_request"] = (
            capo_auditmanager.types.assessment_framework_share_request.redact_sensitive(
                value["assessment_framework_share_request"]
            )
        )
    return out
