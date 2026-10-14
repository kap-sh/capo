"""Generated from Smithy shape ``com.amazonaws.ses#InvalidSnsTopicException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.error_message


class InvalidSnsTopicException_(TypedDict, closed=True):
    topic: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>Indicates that the topic does not exist.</p>"""
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidSnsTopicException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "topic" in value:
        pairs.append((f"{key_prefix}Topic", str(value["topic"])))
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidSnsTopicException_:
    out: InvalidSnsTopicException_ = {}  # type: ignore[typeddict-item]
    child_topic = el.find("Topic")
    if child_topic is not None:
        out["topic"] = str(child_topic.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidSnsTopicException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#InvalidSnsTopicException``."""

    code: str | None = "InvalidSnsTopicException"

    def __init__(
        self,
        data: InvalidSnsTopicException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSnsTopicException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidSnsTopicException":
        return cls(deserialize_query(el), message, response=response)
