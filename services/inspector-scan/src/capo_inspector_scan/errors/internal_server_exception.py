"""Generated from Smithy shape ``com.amazonaws.inspectorscan#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_inspector_scan.errors import ServiceError

if TYPE_CHECKING:
    import capo_inspector_scan.types.internal_server_exception_reason


class InternalServerException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_inspector_scan.types.internal_server_exception_reason.InternalServerExceptionReason"
    """<p>The reason for the validation failure.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_inspector_scan.types.internal_server_exception_reason

    out["reason"] = (
        capo_inspector_scan.types.internal_server_exception_reason.serialize_json(
            value["reason"]
        )
    )
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("reason") is not None:
        import capo_inspector_scan.types.internal_server_exception_reason

        out["reason"] = (
            capo_inspector_scan.types.internal_server_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_inspector_scan.types.internal_server_exception_reason.InternalServerExceptionReason",
            "",
        )
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspectorscan#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_json(data), message, response=response)
