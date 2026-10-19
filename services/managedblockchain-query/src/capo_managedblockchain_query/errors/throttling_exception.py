"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain_query.errors import ServiceError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.exception_message
    import capo_managedblockchain_query.types.quota_code
    import capo_managedblockchain_query.types.service_code


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_managedblockchain_query.types.exception_message.ExceptionMessage"
    """<p>The container for the exception message.</p>"""
    service_code: "capo_managedblockchain_query.types.service_code.ServiceCode"
    """<p>The container for the <code>serviceCode</code>.</p>"""
    quota_code: "capo_managedblockchain_query.types.quota_code.QuotaCode"
    """<p>The container for the <code>quotaCode</code>.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>The container of the <code>retryAfterSeconds</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["serviceCode"] = value["service_code"]
    out["quotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        out["service_code"] = ""
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    else:
        out["quota_code"] = ""
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchainquery#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_json(data), message, response=response)
