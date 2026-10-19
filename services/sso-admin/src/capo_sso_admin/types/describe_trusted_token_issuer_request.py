"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeTrustedTokenIssuerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.trusted_token_issuer_arn


class DescribeTrustedTokenIssuerRequest(TypedDict, closed=True):
    trusted_token_issuer_arn: (
        "capo_sso_admin.types.trusted_token_issuer_arn.TrustedTokenIssuerArn"
    )
    """<p>Specifies the ARN of the trusted token issuer configuration that you want details about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustedTokenIssuerRequest) -> dict:
    out: dict = {}
    out["TrustedTokenIssuerArn"] = value["trusted_token_issuer_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrustedTokenIssuerRequest:
    out: DescribeTrustedTokenIssuerRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrustedTokenIssuerArn") is not None:
        out["trusted_token_issuer_arn"] = data["TrustedTokenIssuerArn"]
    else:
        out["trusted_token_issuer_arn"] = ""
    return out
