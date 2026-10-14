"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DashboardInvalidInputError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element
from capo_cloudwatch.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch.types.dashboard_error_message
    import capo_cloudwatch.types.dashboard_validation_messages


class DashboardInvalidInputError_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cloudwatch.types.dashboard_error_message.DashboardErrorMessage"
    ]
    dashboard_validation_messages: NotRequired[
        "capo_cloudwatch.types.dashboard_validation_messages.DashboardValidationMessages"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardInvalidInputError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "dashboard_validation_messages" in value:
        import capo_cloudwatch.types.dashboard_validation_messages

        out["dashboardValidationMessages"] = (
            capo_cloudwatch.types.dashboard_validation_messages.serialize_aws_json_1_0(
                value["dashboard_validation_messages"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DashboardInvalidInputError_:
    out: DashboardInvalidInputError_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("dashboardValidationMessages") is not None:
        import capo_cloudwatch.types.dashboard_validation_messages

        out["dashboard_validation_messages"] = (
            capo_cloudwatch.types.dashboard_validation_messages.deserialize_aws_json_1_0(
                data["dashboardValidationMessages"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DashboardInvalidInputError_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))
    if "dashboard_validation_messages" in value:
        import capo_cloudwatch.types.dashboard_validation_messages

        capo_cloudwatch.types.dashboard_validation_messages.serialize_query(
            value["dashboard_validation_messages"],
            pairs,
            f"{key_prefix}dashboardValidationMessages",
        )


def deserialize_query(el: Element) -> DashboardInvalidInputError_:
    out: DashboardInvalidInputError_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_dashboard_validation_messages = el.find("dashboardValidationMessages")
    if child_dashboard_validation_messages is not None:
        import capo_cloudwatch.types.dashboard_validation_messages

        out["dashboard_validation_messages"] = (
            capo_cloudwatch.types.dashboard_validation_messages.deserialize_query(
                child_dashboard_validation_messages
            )
        )
    return out


class DashboardInvalidInputError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatch#DashboardInvalidInputError``."""

    code: str | None = "DashboardInvalidInputError"

    def __init__(
        self,
        data: DashboardInvalidInputError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DashboardInvalidInputError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DashboardInvalidInputError":
        return cls(deserialize_aws_json_1_0(data), message, response=response)

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "DashboardInvalidInputError":
        return cls(deserialize_query(el), message, response=response)
