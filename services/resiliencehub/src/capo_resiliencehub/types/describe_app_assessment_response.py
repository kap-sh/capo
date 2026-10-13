"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeAppAssessmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_assessment


class DescribeAppAssessmentResponse(TypedDict, closed=True):
    assessment: "capo_resiliencehub.types.app_assessment.AppAssessment"
    """<p>The assessment for an Resilience Hub application, returned as an object. This object includes Amazon Resource Names (ARNs), compliance information, compliance status, cost, messages, resiliency scores, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppAssessmentResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.app_assessment

    out["assessment"] = capo_resiliencehub.types.app_assessment.serialize_json(
        value["assessment"]
    )
    return out


def deserialize_json(data: dict) -> DescribeAppAssessmentResponse:
    out: DescribeAppAssessmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessment") is not None:
        import capo_resiliencehub.types.app_assessment

        out["assessment"] = capo_resiliencehub.types.app_assessment.deserialize_json(
            data["assessment"]
        )
    else:
        raise DeserializationError("DescribeAppAssessmentResponse.assessment required")
    return out


def redact_sensitive(value: DescribeAppAssessmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment" in value:
        import capo_resiliencehub.types.app_assessment

        out["assessment"] = capo_resiliencehub.types.app_assessment.redact_sensitive(
            value["assessment"]
        )
    return out
