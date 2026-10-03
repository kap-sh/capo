"""Generated from Smithy shape ``com.amazonaws.rtbfabric#AssociateCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.acm_certificate_arn
    import capo_rtbfabric.types.gateway_id


class AssociateCertificateRequest(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn"
    """<p>The Amazon Resource Name (ARN) of the ACM certificate to associate.</p>"""
    client_token: "str"
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateCertificateRequest) -> dict:
    out: dict = {}
    out["acmCertificateArn"] = value["acm_certificate_arn"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateCertificateRequest:
    out: AssociateCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("acmCertificateArn") is not None:
        out["acm_certificate_arn"] = data["acmCertificateArn"]
    else:
        raise DeserializationError(
            "AssociateCertificateRequest.acm_certificate_arn required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("AssociateCertificateRequest.client_token required")
    return out
