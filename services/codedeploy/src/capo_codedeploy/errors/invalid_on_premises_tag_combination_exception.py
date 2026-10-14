"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidOnPremisesTagCombinationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import capo_codedeploy.types.message


class InvalidOnPremisesTagCombinationException_(TypedDict, closed=True):
    message: NotRequired["capo_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidOnPremisesTagCombinationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidOnPremisesTagCombinationException_:
    out: InvalidOnPremisesTagCombinationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidOnPremisesTagCombinationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidOnPremisesTagCombinationException``."""

    code: str | None = "InvalidOnPremisesTagCombinationException"

    def __init__(
        self,
        data: InvalidOnPremisesTagCombinationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidOnPremisesTagCombinationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidOnPremisesTagCombinationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
