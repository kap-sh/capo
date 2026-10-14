"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerRunningException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.message_string


class CrawlerRunningException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerRunningException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CrawlerRunningException_:
    out: CrawlerRunningException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CrawlerRunningException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#CrawlerRunningException``."""

    code: str | None = "CrawlerRunningException"

    def __init__(
        self,
        data: CrawlerRunningException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CrawlerRunningException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CrawlerRunningException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
