"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KMSKeyNotAccessibleFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_database_migration_service.types.exception_message


class KMSKeyNotAccessibleFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_database_migration_service.types.exception_message.ExceptionMessage"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSKeyNotAccessibleFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSKeyNotAccessibleFault_:
    out: KMSKeyNotAccessibleFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class KMSKeyNotAccessibleFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#KMSKeyNotAccessibleFault``."""

    code: str | None = "KMSKeyNotAccessibleFault"

    def __init__(
        self,
        data: KMSKeyNotAccessibleFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSKeyNotAccessibleFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KMSKeyNotAccessibleFault":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
