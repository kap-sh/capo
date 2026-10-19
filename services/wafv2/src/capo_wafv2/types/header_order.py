"""Generated from Smithy shape ``com.amazonaws.wafv2#HeaderOrder``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.oversize_handling


class HeaderOrder(TypedDict, closed=True):
    oversize_handling: "capo_wafv2.types.oversize_handling.OversizeHandling"
    """<p>What WAF should do if the headers determined by your match scope are more numerous or larger than WAF can inspect. WAF does not support inspecting the entire contents of request headers when they exceed 8 KB (8192 bytes) or 200 total headers. The underlying host service forwards a maximum of 200 headers and at most 8 KB of header contents to WAF. </p> <p>The options for oversize handling are the following:</p> <ul> <li> <p> <code>CONTINUE</code> - Inspect the available headers normally, according to the rule inspection criteria. </p> </li> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HeaderOrder) -> dict:
    out: dict = {}
    import capo_wafv2.types.oversize_handling

    out["OversizeHandling"] = capo_wafv2.types.oversize_handling.serialize_aws_json_1_1(
        value["oversize_handling"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> HeaderOrder:
    out: HeaderOrder = {}  # type: ignore[typeddict-item]
    if data.get("OversizeHandling") is not None:
        import capo_wafv2.types.oversize_handling

        out["oversize_handling"] = (
            capo_wafv2.types.oversize_handling.deserialize_aws_json_1_1(
                data["OversizeHandling"]
            )
        )
    else:
        import typing

        out["oversize_handling"] = typing.cast(
            "capo_wafv2.types.oversize_handling.OversizeHandling", ""
        )
    return out
