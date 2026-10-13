"""Generated from Smithy shape ``com.amazonaws.resiliencehub#StartAppAssessmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_assessment


class StartAppAssessmentResponse(TypedDict, closed=True):
    assessment: "capo_resiliencehub.types.app_assessment.AppAssessment"
    """<p>The assessment created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAppAssessmentResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.app_assessment

    out["assessment"] = capo_resiliencehub.types.app_assessment.serialize_json(
        value["assessment"]
    )
    return out


def deserialize_json(data: dict) -> StartAppAssessmentResponse:
    out: StartAppAssessmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessment") is not None:
        import capo_resiliencehub.types.app_assessment

        out["assessment"] = capo_resiliencehub.types.app_assessment.deserialize_json(
            data["assessment"]
        )
    else:
        raise DeserializationError("StartAppAssessmentResponse.assessment required")
    return out


def redact_sensitive(value: StartAppAssessmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment" in value:
        import capo_resiliencehub.types.app_assessment

        out["assessment"] = capo_resiliencehub.types.app_assessment.redact_sensitive(
            value["assessment"]
        )
    return out
