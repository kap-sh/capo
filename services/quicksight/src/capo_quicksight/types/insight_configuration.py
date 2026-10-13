"""Generated from Smithy shape ``com.amazonaws.quicksight#InsightConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.computation_list
    import capo_quicksight.types.custom_narrative_options
    import capo_quicksight.types.visual_interaction_options


class InsightConfiguration(TypedDict, closed=True):
    computations: NotRequired["capo_quicksight.types.computation_list.ComputationList"]
    """<p>The computations configurations of the insight visual</p>"""
    custom_narrative: NotRequired[
        "capo_quicksight.types.custom_narrative_options.CustomNarrativeOptions"
    ]
    """<p>The custom narrative of the insight visual.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightConfiguration) -> dict:
    out: dict = {}
    if "computations" in value:
        import capo_quicksight.types.computation_list

        out["Computations"] = capo_quicksight.types.computation_list.serialize_json(
            value["computations"]
        )
    if "custom_narrative" in value:
        import capo_quicksight.types.custom_narrative_options

        out["CustomNarrative"] = (
            capo_quicksight.types.custom_narrative_options.serialize_json(
                value["custom_narrative"]
            )
        )
    if "interactions" in value:
        import capo_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> InsightConfiguration:
    out: InsightConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Computations") is not None:
        import capo_quicksight.types.computation_list

        out["computations"] = capo_quicksight.types.computation_list.deserialize_json(
            data["Computations"]
        )
    if data.get("CustomNarrative") is not None:
        import capo_quicksight.types.custom_narrative_options

        out["custom_narrative"] = (
            capo_quicksight.types.custom_narrative_options.deserialize_json(
                data["CustomNarrative"]
            )
        )
    if data.get("Interactions") is not None:
        import capo_quicksight.types.visual_interaction_options

        out["interactions"] = (
            capo_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out


def redact_sensitive(value: InsightConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "computations" in value:
        import capo_quicksight.types.computation_list

        out["computations"] = capo_quicksight.types.computation_list.redact_sensitive(
            value["computations"]
        )
    return out
