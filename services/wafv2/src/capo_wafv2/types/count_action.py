"""Generated from Smithy shape ``com.amazonaws.wafv2#CountAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.custom_request_handling


class CountAction(TypedDict, closed=True):
    custom_request_handling: NotRequired[
        "capo_wafv2.types.custom_request_handling.CustomRequestHandling"
    ]
    """<p>Defines custom handling for the web request.</p> <p>For information about customizing web requests and responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CountAction) -> dict:
    out: dict = {}
    if "custom_request_handling" in value:
        import capo_wafv2.types.custom_request_handling

        out["CustomRequestHandling"] = (
            capo_wafv2.types.custom_request_handling.serialize_aws_json_1_1(
                value["custom_request_handling"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CountAction:
    out: CountAction = {}  # type: ignore[typeddict-item]
    if data.get("CustomRequestHandling") is not None:
        import capo_wafv2.types.custom_request_handling

        out["custom_request_handling"] = (
            capo_wafv2.types.custom_request_handling.deserialize_aws_json_1_1(
                data["CustomRequestHandling"]
            )
        )
    return out
