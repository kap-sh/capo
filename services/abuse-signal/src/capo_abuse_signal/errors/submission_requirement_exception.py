"""Generated from Smithy shape ``com.amazonaws.abusesignal#SubmissionRequirementException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_abuse_signal.errors import ServiceError

if TYPE_CHECKING:
    import capo_abuse_signal.types.submission_requirement_list


class SubmissionRequirementException_(TypedDict, closed=True):
    message: "str"
    """<p>A summary of the unmet submission requirements.</p>"""
    unmet_requirements: NotRequired[
        "capo_abuse_signal.types.submission_requirement_list.SubmissionRequirementList"
    ]
    """<p>A list of the specific submission requirements that the report did not meet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmissionRequirementException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "unmet_requirements" in value:
        import capo_abuse_signal.types.submission_requirement_list

        out["unmetRequirements"] = (
            capo_abuse_signal.types.submission_requirement_list.serialize_json(
                value["unmet_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubmissionRequirementException_:
    out: SubmissionRequirementException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("unmetRequirements") is not None:
        import capo_abuse_signal.types.submission_requirement_list

        out["unmet_requirements"] = (
            capo_abuse_signal.types.submission_requirement_list.deserialize_json(
                data["unmetRequirements"]
            )
        )
    return out


class SubmissionRequirementException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.abusesignal#SubmissionRequirementException``."""

    code: str | None = "SubmissionRequirementException"

    def __init__(
        self,
        data: SubmissionRequirementException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SubmissionRequirementException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SubmissionRequirementException":
        return cls(deserialize_json(data), message, response=response)
