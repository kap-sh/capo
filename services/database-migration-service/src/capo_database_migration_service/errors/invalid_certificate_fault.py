"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#InvalidCertificateFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_database_migration_service.types.exception_message


class InvalidCertificateFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_database_migration_service.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidCertificateFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidCertificateFault_:
    out: InvalidCertificateFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidCertificateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#InvalidCertificateFault``."""

    code: str | None = "InvalidCertificateFault"

    def __init__(
        self,
        data: InvalidCertificateFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCertificateFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidCertificateFault":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
