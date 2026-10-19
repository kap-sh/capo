"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksContentFilterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config_list


class GuardrailChecksContentFilterConfig(TypedDict, closed=True):
    categories: "capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config_list.GuardrailChecksContentFilterCategoryConfigList"
    """<p>The content filter categories to evaluate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksContentFilterConfig) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config_list

    out["categories"] = (
        capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config_list.serialize_json(
            value["categories"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksContentFilterConfig:
    out: GuardrailChecksContentFilterConfig = {}  # type: ignore[typeddict-item]
    if data.get("categories") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config_list

        out["categories"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        out["categories"] = []
    return out
