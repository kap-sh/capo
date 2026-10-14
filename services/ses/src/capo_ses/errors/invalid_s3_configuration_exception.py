"""Generated from Smithy shape ``com.amazonaws.ses#InvalidS3ConfigurationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.error_message
    import capo_ses.types.s3_bucket_name


class InvalidS3ConfigurationException_(TypedDict, closed=True):
    bucket: NotRequired["capo_ses.types.s3_bucket_name.S3BucketName"]
    """<p>Indicated that the S3 Bucket was not found.</p>"""
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidS3ConfigurationException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "bucket" in value:
        pairs.append((f"{key_prefix}Bucket", str(value["bucket"])))
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidS3ConfigurationException_:
    out: InvalidS3ConfigurationException_ = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidS3ConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#InvalidS3ConfigurationException``."""

    code: str | None = "InvalidS3ConfigurationException"

    def __init__(
        self,
        data: InvalidS3ConfigurationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidS3ConfigurationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidS3ConfigurationException":
        return cls(deserialize_query(el), message, response=response)
