"""Generated from Smithy shape ``com.amazonaws.inspector#AgentsAlreadyRunningAssessmentException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_inspector.errors import ServiceError

if TYPE_CHECKING:
    import capo_inspector.types.agent_already_running_assessment_list
    import capo_inspector.types.bool
    import capo_inspector.types.error_message


class AgentsAlreadyRunningAssessmentException_(TypedDict, closed=True):
    message: "capo_inspector.types.error_message.ErrorMessage"
    """<p>Details of the exception error.</p>"""
    agents: "capo_inspector.types.agent_already_running_assessment_list.AgentAlreadyRunningAssessmentList"
    """<p></p>"""
    agents_truncated: "capo_inspector.types.bool.Bool"
    """<p></p>"""
    can_retry: "capo_inspector.types.bool.Bool"
    """<p>You can immediately retry your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentsAlreadyRunningAssessmentException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_inspector.types.agent_already_running_assessment_list

    out["agents"] = (
        capo_inspector.types.agent_already_running_assessment_list.serialize_aws_json_1_1(
            value["agents"]
        )
    )
    out["agentsTruncated"] = value["agents_truncated"]
    out["canRetry"] = value["can_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentsAlreadyRunningAssessmentException_:
    out: AgentsAlreadyRunningAssessmentException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("agents") is not None:
        import capo_inspector.types.agent_already_running_assessment_list

        out["agents"] = (
            capo_inspector.types.agent_already_running_assessment_list.deserialize_aws_json_1_1(
                data["agents"]
            )
        )
    else:
        out["agents"] = []
    if data.get("agentsTruncated") is not None:
        out["agents_truncated"] = data["agentsTruncated"]
    else:
        out["agents_truncated"] = False
    if data.get("canRetry") is not None:
        out["can_retry"] = data["canRetry"]
    else:
        out["can_retry"] = False
    return out


class AgentsAlreadyRunningAssessmentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#AgentsAlreadyRunningAssessmentException``."""

    code: str | None = "AgentsAlreadyRunningAssessmentException"

    def __init__(
        self,
        data: AgentsAlreadyRunningAssessmentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AgentsAlreadyRunningAssessmentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AgentsAlreadyRunningAssessmentException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
