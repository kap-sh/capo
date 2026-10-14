"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RegistryNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ecr_public.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr_public.types.exception_message


class RegistryNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr_public.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistryNotFoundException_:
    out: RegistryNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class RegistryNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecrpublic#RegistryNotFoundException``."""

    code: str | None = "RegistryNotFoundException"

    def __init__(
        self,
        data: RegistryNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RegistryNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RegistryNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
