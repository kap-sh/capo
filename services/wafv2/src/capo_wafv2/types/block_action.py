"""Generated from Smithy shape ``com.amazonaws.wafv2#BlockAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.custom_response


class BlockAction(TypedDict, closed=True):
    custom_response: NotRequired["capo_wafv2.types.custom_response.CustomResponse"]
    """<p>Defines a custom response for the web request.</p> <p>For information about customizing web requests and responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockAction) -> dict:
    out: dict = {}
    if "custom_response" in value:
        import capo_wafv2.types.custom_response

        out["CustomResponse"] = capo_wafv2.types.custom_response.serialize_aws_json_1_1(
            value["custom_response"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BlockAction:
    out: BlockAction = {}  # type: ignore[typeddict-item]
    if data.get("CustomResponse") is not None:
        import capo_wafv2.types.custom_response

        out["custom_response"] = (
            capo_wafv2.types.custom_response.deserialize_aws_json_1_1(
                data["CustomResponse"]
            )
        )
    return out
