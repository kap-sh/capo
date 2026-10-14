"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunInProgressException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_inspector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_inspector.types.assessment_run_in_progress_arn_list
    import capo_inspector.types.bool
    import capo_inspector.types.error_message


class AssessmentRunInProgressException_(TypedDict, closed=True):
    message: "capo_inspector.types.error_message.ErrorMessage"
    """<p>Details of the exception error.</p>"""
    assessment_run_arns: "capo_inspector.types.assessment_run_in_progress_arn_list.AssessmentRunInProgressArnList"
    """<p>The ARNs of the assessment runs that are currently in progress.</p>"""
    assessment_run_arns_truncated: "capo_inspector.types.bool.Bool"
    """<p>Boolean value that indicates whether the ARN list of the assessment runs is truncated.</p>"""
    can_retry: "capo_inspector.types.bool.Bool"
    """<p>You can immediately retry your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunInProgressException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_inspector.types.assessment_run_in_progress_arn_list

    out["assessmentRunArns"] = (
        capo_inspector.types.assessment_run_in_progress_arn_list.serialize_aws_json_1_1(
            value["assessment_run_arns"]
        )
    )
    out["assessmentRunArnsTruncated"] = value["assessment_run_arns_truncated"]
    out["canRetry"] = value["can_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentRunInProgressException_:
    out: AssessmentRunInProgressException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AssessmentRunInProgressException_.message required")
    if data.get("assessmentRunArns") is not None:
        import capo_inspector.types.assessment_run_in_progress_arn_list

        out["assessment_run_arns"] = (
            capo_inspector.types.assessment_run_in_progress_arn_list.deserialize_aws_json_1_1(
                data["assessmentRunArns"]
            )
        )
    else:
        raise DeserializationError(
            "AssessmentRunInProgressException_.assessment_run_arns required"
        )
    if data.get("assessmentRunArnsTruncated") is not None:
        out["assessment_run_arns_truncated"] = data["assessmentRunArnsTruncated"]
    else:
        raise DeserializationError(
            "AssessmentRunInProgressException_.assessment_run_arns_truncated required"
        )
    if data.get("canRetry") is not None:
        out["can_retry"] = data["canRetry"]
    else:
        raise DeserializationError(
            "AssessmentRunInProgressException_.can_retry required"
        )
    return out


class AssessmentRunInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#AssessmentRunInProgressException``."""

    code: str | None = "AssessmentRunInProgressException"

    def __init__(
        self,
        data: AssessmentRunInProgressException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AssessmentRunInProgressException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AssessmentRunInProgressException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
