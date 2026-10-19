"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelEnforcement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.excluded_models_list
    import capo_bedrock.types.included_models_list


class ModelEnforcement(TypedDict, closed=True):
    included_models: "capo_bedrock.types.included_models_list.IncludedModelsList"
    """<p>Models to enforce the guardrail on.</p>"""
    excluded_models: "capo_bedrock.types.excluded_models_list.ExcludedModelsList"
    """<p>Models to exclude from enforcement of the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelEnforcement) -> dict:
    out: dict = {}
    import capo_bedrock.types.included_models_list

    out["includedModels"] = capo_bedrock.types.included_models_list.serialize_json(
        value["included_models"]
    )
    import capo_bedrock.types.excluded_models_list

    out["excludedModels"] = capo_bedrock.types.excluded_models_list.serialize_json(
        value["excluded_models"]
    )
    return out


def deserialize_json(data: dict) -> ModelEnforcement:
    out: ModelEnforcement = {}  # type: ignore[typeddict-item]
    if data.get("includedModels") is not None:
        import capo_bedrock.types.included_models_list

        out["included_models"] = (
            capo_bedrock.types.included_models_list.deserialize_json(
                data["includedModels"]
            )
        )
    else:
        out["included_models"] = []
    if data.get("excludedModels") is not None:
        import capo_bedrock.types.excluded_models_list

        out["excluded_models"] = (
            capo_bedrock.types.excluded_models_list.deserialize_json(
                data["excludedModels"]
            )
        )
    else:
        out["excluded_models"] = []
    return out
