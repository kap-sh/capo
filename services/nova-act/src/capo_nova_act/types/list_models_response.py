"""Generated from Smithy shape ``com.amazonaws.novaact#ListModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.compatibility_information
    import capo_nova_act.types.model_aliases
    import capo_nova_act.types.model_summaries


class ListModelsResponse(TypedDict, closed=True):
    model_summaries: "capo_nova_act.types.model_summaries.ModelSummaries"
    """<p>A list of available AI models with their status and compatibility information.</p>"""
    model_aliases: "capo_nova_act.types.model_aliases.ModelAliases"
    """<p>A list of model aliases that provide stable references to model versions.</p>"""
    compatibility_information: (
        "capo_nova_act.types.compatibility_information.CompatibilityInformation"
    )
    """<p>Information about client compatibility and supported models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelsResponse) -> dict:
    out: dict = {}
    import capo_nova_act.types.model_summaries

    out["modelSummaries"] = capo_nova_act.types.model_summaries.serialize_json(
        value["model_summaries"]
    )
    import capo_nova_act.types.model_aliases

    out["modelAliases"] = capo_nova_act.types.model_aliases.serialize_json(
        value["model_aliases"]
    )
    import capo_nova_act.types.compatibility_information

    out["compatibilityInformation"] = (
        capo_nova_act.types.compatibility_information.serialize_json(
            value["compatibility_information"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListModelsResponse:
    out: ListModelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("modelSummaries") is not None:
        import capo_nova_act.types.model_summaries

        out["model_summaries"] = capo_nova_act.types.model_summaries.deserialize_json(
            data["modelSummaries"]
        )
    else:
        out["model_summaries"] = []
    if data.get("modelAliases") is not None:
        import capo_nova_act.types.model_aliases

        out["model_aliases"] = capo_nova_act.types.model_aliases.deserialize_json(
            data["modelAliases"]
        )
    else:
        out["model_aliases"] = []
    if data.get("compatibilityInformation") is not None:
        import capo_nova_act.types.compatibility_information

        out["compatibility_information"] = (
            capo_nova_act.types.compatibility_information.deserialize_json(
                data["compatibilityInformation"]
            )
        )
    else:
        raise DeserializationError(
            "ListModelsResponse.compatibility_information required"
        )
    return out
