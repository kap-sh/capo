"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TagOptionNotMigratedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_catalog.types.error_message


class TagOptionNotMigratedException_(TypedDict, closed=True):
    message: NotRequired["capo_service_catalog.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOptionNotMigratedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagOptionNotMigratedException_:
    out: TagOptionNotMigratedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class TagOptionNotMigratedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicecatalog#TagOptionNotMigratedException``."""

    code: str | None = "TagOptionNotMigratedException"

    def __init__(
        self,
        data: TagOptionNotMigratedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagOptionNotMigratedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TagOptionNotMigratedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
