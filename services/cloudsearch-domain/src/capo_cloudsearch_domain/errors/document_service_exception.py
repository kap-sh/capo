"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#DocumentServiceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch_domain.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.string


class DocumentServiceException_(TypedDict, closed=True):
    status: NotRequired["capo_cloudsearch_domain.types.string.String"]
    """<p>The return status of a document upload request, <code>error</code> or <code>success</code>.</p>"""
    message: NotRequired["capo_cloudsearch_domain.types.string.String"]
    """<p>The description of the errors returned by the document service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentServiceException_) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DocumentServiceException_:
    out: DocumentServiceException_ = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DocumentServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudsearchdomain#DocumentServiceException``."""

    code: str | None = "DocumentServiceException"

    def __init__(
        self,
        data: DocumentServiceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DocumentServiceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DocumentServiceException":
        return cls(deserialize_json(data), message, response=response)
