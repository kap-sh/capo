"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ElasticBeanstalkServiceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element
from capo_elastic_beanstalk.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.exception_message


class ElasticBeanstalkServiceException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_beanstalk.types.exception_message.ExceptionMessage"
    ]
    """<p>The exception error message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ElasticBeanstalkServiceException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> ElasticBeanstalkServiceException_:
    out: ElasticBeanstalkServiceException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ElasticBeanstalkServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticbeanstalk#ElasticBeanstalkServiceException``."""

    code: str | None = "ElasticBeanstalkServiceException"

    def __init__(
        self,
        data: ElasticBeanstalkServiceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ElasticBeanstalkServiceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ElasticBeanstalkServiceException":
        return cls(deserialize_query(el), message, response=response)
