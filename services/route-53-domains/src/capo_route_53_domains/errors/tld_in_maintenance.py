"""Generated from Smithy shape ``com.amazonaws.route53domains#TLDInMaintenance``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import capo_route_53_domains.types.error_message
    import capo_route_53_domains.types.tld_name


class TLDInMaintenance_(TypedDict, closed=True):
    message: NotRequired["capo_route_53_domains.types.error_message.ErrorMessage"]
    """<p>The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.</p>"""
    tld: NotRequired["capo_route_53_domains.types.tld_name.TldName"]
    """<p>The top-level domain that is currently undergoing maintenance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TLDInMaintenance_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "tld" in value:
        out["tld"] = value["tld"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TLDInMaintenance_:
    out: TLDInMaintenance_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("tld") is not None:
        out["tld"] = data["tld"]
    return out


class TLDInMaintenance(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#TLDInMaintenance``."""

    code: str | None = "TLDInMaintenance"

    def __init__(
        self,
        data: TLDInMaintenance_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TLDInMaintenance",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TLDInMaintenance":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
