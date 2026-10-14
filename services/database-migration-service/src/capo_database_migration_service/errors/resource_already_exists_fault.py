"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ResourceAlreadyExistsFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_database_migration_service.types.exception_message
    import capo_database_migration_service.types.resource_arn


class ResourceAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_database_migration_service.types.exception_message.ExceptionMessage"
    ]
    """<p></p>"""
    resource_arn: NotRequired[
        "capo_database_migration_service.types.resource_arn.ResourceArn"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAlreadyExistsFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceAlreadyExistsFault_:
    out: ResourceAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    return out


class ResourceAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#ResourceAlreadyExistsFault``."""

    code: str | None = "ResourceAlreadyExistsFault"

    def __init__(
        self,
        data: ResourceAlreadyExistsFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistsFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceAlreadyExistsFault":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
