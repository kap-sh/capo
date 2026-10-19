"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksContentFilterCategoryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_category


class GuardrailChecksContentFilterCategoryConfig(TypedDict, closed=True):
    category: "capo_bedrock_runtime.types.guardrail_checks_content_filter_category.GuardrailChecksContentFilterCategory"
    """<p>The content filter category to evaluate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksContentFilterCategoryConfig) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_category

    out["category"] = (
        capo_bedrock_runtime.types.guardrail_checks_content_filter_category.serialize_json(
            value["category"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksContentFilterCategoryConfig:
    out: GuardrailChecksContentFilterCategoryConfig = {}  # type: ignore[typeddict-item]
    if data.get("category") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_content_filter_category

        out["category"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_filter_category.deserialize_json(
                data["category"]
            )
        )
    else:
        import typing

        out["category"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_checks_content_filter_category.GuardrailChecksContentFilterCategory",
            "",
        )
    return out
