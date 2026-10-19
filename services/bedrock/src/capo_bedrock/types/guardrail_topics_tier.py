"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicsTier``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_topics_tier_name


class GuardrailTopicsTier(TypedDict, closed=True):
    tier_name: "capo_bedrock.types.guardrail_topics_tier_name.GuardrailTopicsTierName"
    """<p>The tier that your guardrail uses for denied topic filters. Valid values include:</p> <ul> <li> <p> <code>CLASSIC</code> tier – Provides established guardrails functionality supporting English, French, and Spanish languages.</p> </li> <li> <p> <code>STANDARD</code> tier – Provides a more robust solution than the <code>CLASSIC</code> tier and has more comprehensive language support. This tier requires that your guardrail use <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html">cross-Region inference</a>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicsTier) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_topics_tier_name

    out["tierName"] = capo_bedrock.types.guardrail_topics_tier_name.serialize_json(
        value["tier_name"]
    )
    return out


def deserialize_json(data: dict) -> GuardrailTopicsTier:
    out: GuardrailTopicsTier = {}  # type: ignore[typeddict-item]
    if data.get("tierName") is not None:
        import capo_bedrock.types.guardrail_topics_tier_name

        out["tier_name"] = (
            capo_bedrock.types.guardrail_topics_tier_name.deserialize_json(
                data["tierName"]
            )
        )
    else:
        import typing

        out["tier_name"] = typing.cast(
            "capo_bedrock.types.guardrail_topics_tier_name.GuardrailTopicsTierName", ""
        )
    return out


def redact_sensitive(value: GuardrailTopicsTier) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tier_name" in value:
        out["tier_name"] = "*** Sensitive Data Redacted ***"
    return out
