"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFEntityMigrationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_waf_regional.errors import ServiceError

if TYPE_CHECKING:
    import capo_waf_regional.types.error_message
    import capo_waf_regional.types.error_reason
    import capo_waf_regional.types.migration_error_type


class WAFEntityMigrationException_(TypedDict, closed=True):
    message: NotRequired["capo_waf_regional.types.error_message.errorMessage"]
    migration_error_type: NotRequired[
        "capo_waf_regional.types.migration_error_type.MigrationErrorType"
    ]
    migration_error_reason: NotRequired[
        "capo_waf_regional.types.error_reason.ErrorReason"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFEntityMigrationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "migration_error_type" in value:
        import capo_waf_regional.types.migration_error_type

        out["MigrationErrorType"] = (
            capo_waf_regional.types.migration_error_type.serialize_aws_json_1_1(
                value["migration_error_type"]
            )
        )
    if "migration_error_reason" in value:
        out["MigrationErrorReason"] = value["migration_error_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFEntityMigrationException_:
    out: WAFEntityMigrationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("MigrationErrorType") is not None:
        import capo_waf_regional.types.migration_error_type

        out["migration_error_type"] = (
            capo_waf_regional.types.migration_error_type.deserialize_aws_json_1_1(
                data["MigrationErrorType"]
            )
        )
    if data.get("MigrationErrorReason") is not None:
        out["migration_error_reason"] = data["MigrationErrorReason"]
    return out


class WAFEntityMigrationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFEntityMigrationException``."""

    code: str | None = "WAFEntityMigrationException"

    def __init__(
        self,
        data: WAFEntityMigrationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFEntityMigrationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "WAFEntityMigrationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
