"""Generated from Smithy shape ``com.amazonaws.route53domains#RetrieveDomainAuthCodeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_auth_code


class RetrieveDomainAuthCodeResponse(TypedDict, closed=True):
    auth_code: NotRequired[
        "capo_route_53_domains.types.domain_auth_code.DomainAuthCode"
    ]
    """<p>The authorization code for the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetrieveDomainAuthCodeResponse) -> dict:
    out: dict = {}
    if "auth_code" in value:
        out["AuthCode"] = value["auth_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetrieveDomainAuthCodeResponse:
    out: RetrieveDomainAuthCodeResponse = {}  # type: ignore[typeddict-item]
    if data.get("AuthCode") is not None:
        out["auth_code"] = data["AuthCode"]
    return out


def redact_sensitive(value: RetrieveDomainAuthCodeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_code" in value:
        out["auth_code"] = "*** Sensitive Data Redacted ***"
    return out
