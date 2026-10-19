"""Generated from Smithy shape ``com.amazonaws.wafv2#RateLimitJA3Fingerprint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.fallback_behavior


class RateLimitJA3Fingerprint(TypedDict, closed=True):
    fallback_behavior: "capo_wafv2.types.fallback_behavior.FallbackBehavior"
    """<p>The match status to assign to the web request if there is insufficient TSL Client Hello information to compute the JA3 fingerprint.</p> <p>You can specify the following fallback behaviors:</p> <ul> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateLimitJA3Fingerprint) -> dict:
    out: dict = {}
    import capo_wafv2.types.fallback_behavior

    out["FallbackBehavior"] = capo_wafv2.types.fallback_behavior.serialize_aws_json_1_1(
        value["fallback_behavior"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RateLimitJA3Fingerprint:
    out: RateLimitJA3Fingerprint = {}  # type: ignore[typeddict-item]
    if data.get("FallbackBehavior") is not None:
        import capo_wafv2.types.fallback_behavior

        out["fallback_behavior"] = (
            capo_wafv2.types.fallback_behavior.deserialize_aws_json_1_1(
                data["FallbackBehavior"]
            )
        )
    else:
        import typing

        out["fallback_behavior"] = typing.cast(
            "capo_wafv2.types.fallback_behavior.FallbackBehavior", ""
        )
    return out
