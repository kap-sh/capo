"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2ActionBlockDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_wafv2_custom_response_details


class AwsWafv2ActionBlockDetails(TypedDict, closed=True):
    custom_response: NotRequired[
        "capo_securityhub.types.aws_wafv2_custom_response_details.AwsWafv2CustomResponseDetails"
    ]
    """<p> Defines a custom response for the web request. For information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide.</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2ActionBlockDetails) -> dict:
    out: dict = {}
    if "custom_response" in value:
        import capo_securityhub.types.aws_wafv2_custom_response_details

        out["CustomResponse"] = (
            capo_securityhub.types.aws_wafv2_custom_response_details.serialize_json(
                value["custom_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2ActionBlockDetails:
    out: AwsWafv2ActionBlockDetails = {}  # type: ignore[typeddict-item]
    if data.get("CustomResponse") is not None:
        import capo_securityhub.types.aws_wafv2_custom_response_details

        out["custom_response"] = (
            capo_securityhub.types.aws_wafv2_custom_response_details.deserialize_json(
                data["CustomResponse"]
            )
        )
    return out
