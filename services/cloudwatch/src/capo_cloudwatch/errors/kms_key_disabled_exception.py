"""Generated from Smithy shape ``com.amazonaws.cloudwatch#KmsKeyDisabledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element
from capo_cloudwatch.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch.types.string


class KmsKeyDisabledException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudwatch.types.string.String"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsKeyDisabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsKeyDisabledException_:
    out: KmsKeyDisabledException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: KmsKeyDisabledException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> KmsKeyDisabledException_:
    out: KmsKeyDisabledException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class KmsKeyDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatch#KmsKeyDisabledException``."""

    code: str | None = "KmsKeyDisabledException"

    def __init__(
        self,
        data: KmsKeyDisabledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsKeyDisabledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KmsKeyDisabledException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "KmsKeyDisabledException":
        return cls(deserialize_query(el), message, response=response)
