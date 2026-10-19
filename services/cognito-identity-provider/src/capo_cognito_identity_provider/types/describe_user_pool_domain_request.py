"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeUserPoolDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.domain_type


class DescribeUserPoolDomainRequest(TypedDict, closed=True):
    domain: "capo_cognito_identity_provider.types.domain_type.DomainType"
    """<p>The domain that you want to describe. For custom domains, this is the fully-qualified domain name, such as <code>auth.example.com</code>. For Amazon Cognito prefix domains, this is the prefix alone, such as <code>auth</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserPoolDomainRequest) -> dict:
    out: dict = {}
    out["Domain"] = value["domain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserPoolDomainRequest:
    out: DescribeUserPoolDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        out["domain"] = ""
    return out
