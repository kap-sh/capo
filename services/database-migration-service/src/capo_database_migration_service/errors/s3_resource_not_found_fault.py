"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#S3ResourceNotFoundFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_database_migration_service.types.exception_message


class S3ResourceNotFoundFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_database_migration_service.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ResourceNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ResourceNotFoundFault_:
    out: S3ResourceNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class S3ResourceNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#S3ResourceNotFoundFault``."""

    code: str | None = "S3ResourceNotFoundFault"

    def __init__(
        self,
        data: S3ResourceNotFoundFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="S3ResourceNotFoundFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "S3ResourceNotFoundFault":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
