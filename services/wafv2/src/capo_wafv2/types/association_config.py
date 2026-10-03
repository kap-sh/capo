"""Generated from Smithy shape ``com.amazonaws.wafv2#AssociationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.request_body


class AssociationConfig(TypedDict, closed=True):
    request_body: NotRequired["capo_wafv2.types.request_body.RequestBody"]
    """<p>Customizes the maximum size of the request body that your protected CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access resources forward to WAF for inspection. The default size is 16 KB (16,384 bytes). You can change the setting for any of the available resource types. </p> <note> <p>You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see <a href="http://aws.amazon.com/waf/pricing/">WAF Pricing</a>.</p> </note> <p>Example JSON: <code> { "API_GATEWAY": "KB_48", "APP_RUNNER_SERVICE": "KB_32" }</code> </p> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationConfig) -> dict:
    out: dict = {}
    if "request_body" in value:
        import capo_wafv2.types.request_body

        out["RequestBody"] = capo_wafv2.types.request_body.serialize_aws_json_1_1(
            value["request_body"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationConfig:
    out: AssociationConfig = {}  # type: ignore[typeddict-item]
    if data.get("RequestBody") is not None:
        import capo_wafv2.types.request_body

        out["request_body"] = capo_wafv2.types.request_body.deserialize_aws_json_1_1(
            data["RequestBody"]
        )
    return out
