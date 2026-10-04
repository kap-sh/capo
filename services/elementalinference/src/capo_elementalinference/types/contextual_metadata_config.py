"""Generated from Smithy shape ``com.amazonaws.elementalinference#ContextualMetadataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.extended_analysis_mode
    import capo_elementalinference.types.summary_generation_mode


class ContextualMetadataConfig(TypedDict, closed=True):
    summary_generation: NotRequired[
        "capo_elementalinference.types.summary_generation_mode.SummaryGenerationMode"
    ]
    """<p>Specifies whether Elemental Inference generates a descriptive summary of the media content for this output, along with the objects and actions that it detects. This setting is independent of <code>extendedAnalysis</code>. </p> <p>Valid values:</p> <ul> <li> <p>ENABLED (default) – Elemental Inference populates the summary, objects, and actions fields, along with the IAB taxonomy and GARM suitability classifications. </p> </li> <li> <p>DISABLED – Elemental Inference doesn't populate the summary, objects, and actions fields. </p> </li> </ul>"""
    extended_analysis: NotRequired[
        "capo_elementalinference.types.extended_analysis_mode.ExtendedAnalysisMode"
    ]
    """<p>Specifies whether Elemental Inference generates extended analysis of the media content for this output. Extended analysis identifies the people, environments, brands, and on-screen text in the media content. This setting is independent of <code>summaryGeneration</code>. </p> <p>Valid values:</p> <ul> <li> <p>ENABLED (default) – Elemental Inference populates the people, environments, brands, and on-screen text fields. </p> </li> <li> <p>DISABLED – Elemental Inference doesn't populate the people, environments, brands, and on-screen text fields. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextualMetadataConfig) -> dict:
    out: dict = {}
    if "summary_generation" in value:
        import capo_elementalinference.types.summary_generation_mode

        out["summaryGeneration"] = (
            capo_elementalinference.types.summary_generation_mode.serialize_json(
                value["summary_generation"]
            )
        )
    if "extended_analysis" in value:
        import capo_elementalinference.types.extended_analysis_mode

        out["extendedAnalysis"] = (
            capo_elementalinference.types.extended_analysis_mode.serialize_json(
                value["extended_analysis"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContextualMetadataConfig:
    out: ContextualMetadataConfig = {}  # type: ignore[typeddict-item]
    if data.get("summaryGeneration") is not None:
        import capo_elementalinference.types.summary_generation_mode

        out["summary_generation"] = (
            capo_elementalinference.types.summary_generation_mode.deserialize_json(
                data["summaryGeneration"]
            )
        )
    if data.get("extendedAnalysis") is not None:
        import capo_elementalinference.types.extended_analysis_mode

        out["extended_analysis"] = (
            capo_elementalinference.types.extended_analysis_mode.deserialize_json(
                data["extendedAnalysis"]
            )
        )
    return out
