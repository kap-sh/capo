"""Generated from Smithy shape ``com.amazonaws.mwaa#RestApiClientException``."""

from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mwaa.errors import ServiceError

if TYPE_CHECKING:
    import capo_mwaa.types.rest_api_response


class RestApiClientException_(TypedDict, closed=True):
    rest_api_status_code: NotRequired["int"]
    """<p>The HTTP status code returned by the Apache Airflow REST API call.</p>"""
    rest_api_response: NotRequired["capo_mwaa.types.rest_api_response.RestApiResponse"]
    """<p>The error response data from the Apache Airflow REST API call, provided as a JSON object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestApiClientException_) -> dict:
    out: dict = {}
    if "rest_api_status_code" in value:
        out["RestApiStatusCode"] = value["rest_api_status_code"]
    if "rest_api_response" in value:
        out["RestApiResponse"] = value["rest_api_response"]
    return out


def deserialize_json(data: dict) -> RestApiClientException_:
    out: RestApiClientException_ = {}  # type: ignore[typeddict-item]
    if data.get("RestApiStatusCode") is not None:
        out["rest_api_status_code"] = data["RestApiStatusCode"]
    if data.get("RestApiResponse") is not None:
        out["rest_api_response"] = data["RestApiResponse"]
    return out


class RestApiClientException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mwaa#RestApiClientException``."""

    code: str | None = "RestApiClientException"

    def __init__(
        self,
        data: RestApiClientException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RestApiClientException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RestApiClientException":
        return cls(deserialize_json(data), message, response=response)


def redact_sensitive(value: RestApiClientException_) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rest_api_response" in value:
        out["rest_api_response"] = "*** Sensitive Data Redacted ***"
    return out
