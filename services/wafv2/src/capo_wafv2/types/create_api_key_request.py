"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateAPIKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.api_key_token_domains
    import capo_wafv2.types.scope


class CreateAPIKeyRequest(TypedDict, closed=True):
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    token_domains: "capo_wafv2.types.api_key_token_domains.APIKeyTokenDomains"
    """<p>The client application domains that you want to use this API key for. </p> <p>Example JSON: <code>"TokenDomains": ["abc.com", "store.abc.com"]</code> </p> <p>Public suffixes aren't allowed. For example, you can't use <code>gov.au</code> or <code>co.uk</code> as token domains.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAPIKeyRequest) -> dict:
    out: dict = {}
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    import capo_wafv2.types.api_key_token_domains

    out["TokenDomains"] = capo_wafv2.types.api_key_token_domains.serialize_aws_json_1_1(
        value["token_domains"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAPIKeyRequest:
    out: CreateAPIKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("CreateAPIKeyRequest.scope required")
    if data.get("TokenDomains") is not None:
        import capo_wafv2.types.api_key_token_domains

        out["token_domains"] = (
            capo_wafv2.types.api_key_token_domains.deserialize_aws_json_1_1(
                data["TokenDomains"]
            )
        )
    else:
        raise DeserializationError("CreateAPIKeyRequest.token_domains required")
    return out
