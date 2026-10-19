"""Generated from Smithy shape ``com.amazonaws.polly#ServiceQuotaExceededException``."""

import json
from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_polly._protocol.eventstream import HeaderValue, Message
from capo_polly.errors import ServiceError

if TYPE_CHECKING:
    import capo_polly.types.error_message
    import capo_polly.types.quota_code
    import capo_polly.types.service_code


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_polly.types.error_message.ErrorMessage"
    quota_code: "capo_polly.types.quota_code.QuotaCode"
    """<p>The quota code identifying the specific quota.</p>"""
    service_code: "capo_polly.types.service_code.ServiceCode"
    """<p>The service code identifying the originating service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_polly.types.quota_code

    out["quotaCode"] = capo_polly.types.quota_code.serialize_json(value["quota_code"])
    import capo_polly.types.service_code

    out["serviceCode"] = capo_polly.types.service_code.serialize_json(
        value["service_code"]
    )
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("quotaCode") is not None:
        import capo_polly.types.quota_code

        out["quota_code"] = capo_polly.types.quota_code.deserialize_json(
            data["quotaCode"]
        )
    else:
        import typing

        out["quota_code"] = typing.cast("capo_polly.types.quota_code.QuotaCode", "")
    if data.get("serviceCode") is not None:
        import capo_polly.types.service_code

        out["service_code"] = capo_polly.types.service_code.deserialize_json(
            data["serviceCode"]
        )
    else:
        import typing

        out["service_code"] = typing.cast(
            "capo_polly.types.service_code.ServiceCode", ""
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(
        self,
        data: ServiceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)


def serialize_event_json(value: ServiceQuotaExceededException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "ServiceQuotaExceededException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ServiceQuotaExceededException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
