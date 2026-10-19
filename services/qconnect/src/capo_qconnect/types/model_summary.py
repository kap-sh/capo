"""Generated from Smithy shape ``com.amazonaws.qconnect#ModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.ai_prompt_type_list
    import capo_qconnect.types.cross_region_status
    import capo_qconnect.types.model_display_name
    import capo_qconnect.types.model_id
    import capo_qconnect.types.model_lifecycle


class ModelSummary(TypedDict, closed=True):
    model_id: "capo_qconnect.types.model_id.ModelId"
    """<p>The identifier of the model.</p>"""
    display_name: "capo_qconnect.types.model_display_name.ModelDisplayName"
    """<p>The display name of the model.</p>"""
    cross_region_status: NotRequired[
        "capo_qconnect.types.cross_region_status.CrossRegionStatus"
    ]
    """<p>The cross-region availability status of the model. <code>NONE</code> indicates the model is only available in a single region, <code>REGIONAL</code> indicates the model is available through regional inference, and <code>GLOBAL</code> indicates the model is available through global cross-region inference.</p>"""
    supports_prompt_caching: NotRequired["bool"]
    """<p>Whether the model supports prompt caching.</p>"""
    supported_ai_prompt_types: NotRequired[
        "capo_qconnect.types.ai_prompt_type_list.AIPromptTypeList"
    ]
    """<p>The list of AI Prompt types that the model supports.</p>"""
    model_lifecycle: NotRequired["capo_qconnect.types.model_lifecycle.ModelLifecycle"]
    """<p>The current lifecycle of the model. <code>ACTIVE</code> indicates the model is recommended for use and <code>LEGACY</code> indicates the model is still usable but is deprecated.</p>"""
    legacy_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the model lifecycle will transition from <code>ACTIVE</code> to <code>LEGACY</code>.</p>"""
    end_of_life_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the model will reach end of life and no longer be available for use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelSummary) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    out["displayName"] = value["display_name"]
    if "cross_region_status" in value:
        out["crossRegionStatus"] = value["cross_region_status"]
    if "supports_prompt_caching" in value:
        out["supportsPromptCaching"] = value["supports_prompt_caching"]
    if "supported_ai_prompt_types" in value:
        import capo_qconnect.types.ai_prompt_type_list

        out["supportedAIPromptTypes"] = (
            capo_qconnect.types.ai_prompt_type_list.serialize_json(
                value["supported_ai_prompt_types"]
            )
        )
    if "model_lifecycle" in value:
        out["modelLifecycle"] = value["model_lifecycle"]
    if "legacy_timestamp" in value:
        import capo_qconnect.types._prelude.timestamp

        out["legacyTimestamp"] = capo_qconnect.types._prelude.timestamp.serialize_json(
            value["legacy_timestamp"]
        )
    if "end_of_life_timestamp" in value:
        import capo_qconnect.types._prelude.timestamp

        out["endOfLifeTimestamp"] = (
            capo_qconnect.types._prelude.timestamp.serialize_json(
                value["end_of_life_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModelSummary:
    out: ModelSummary = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("crossRegionStatus") is not None:
        out["cross_region_status"] = data["crossRegionStatus"]
    if data.get("supportsPromptCaching") is not None:
        out["supports_prompt_caching"] = data["supportsPromptCaching"]
    if data.get("supportedAIPromptTypes") is not None:
        import capo_qconnect.types.ai_prompt_type_list

        out["supported_ai_prompt_types"] = (
            capo_qconnect.types.ai_prompt_type_list.deserialize_json(
                data["supportedAIPromptTypes"]
            )
        )
    if data.get("modelLifecycle") is not None:
        out["model_lifecycle"] = data["modelLifecycle"]
    if data.get("legacyTimestamp") is not None:
        import capo_qconnect.types._prelude.timestamp

        out["legacy_timestamp"] = (
            capo_qconnect.types._prelude.timestamp.deserialize_json(
                data["legacyTimestamp"]
            )
        )
    if data.get("endOfLifeTimestamp") is not None:
        import capo_qconnect.types._prelude.timestamp

        out["end_of_life_timestamp"] = (
            capo_qconnect.types._prelude.timestamp.deserialize_json(
                data["endOfLifeTimestamp"]
            )
        )
    return out
