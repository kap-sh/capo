"""Generated from Smithy shape ``com.amazonaws.cleanrooms#InheritedAllowedAdditionalAnalyses``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.allowed_additional_analyses
    import capo_cleanrooms.types.inherited_allowed_additional_analyses_source_list


class InheritedAllowedAdditionalAnalyses(TypedDict, closed=True):
    value: "capo_cleanrooms.types.allowed_additional_analyses.AllowedAdditionalAnalyses"
    """<p>The effective list of allowed additional analyses inherited from parent tables.</p>"""
    sources: "capo_cleanrooms.types.inherited_allowed_additional_analyses_source_list.InheritedAllowedAdditionalAnalysesSourceList"
    """<p>The list of parent tables that contribute to this inherited constraint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InheritedAllowedAdditionalAnalyses) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.allowed_additional_analyses

    out["value"] = capo_cleanrooms.types.allowed_additional_analyses.serialize_json(
        value["value"]
    )
    import capo_cleanrooms.types.inherited_allowed_additional_analyses_source_list

    out["sources"] = (
        capo_cleanrooms.types.inherited_allowed_additional_analyses_source_list.serialize_json(
            value["sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> InheritedAllowedAdditionalAnalyses:
    out: InheritedAllowedAdditionalAnalyses = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_cleanrooms.types.allowed_additional_analyses

        out["value"] = (
            capo_cleanrooms.types.allowed_additional_analyses.deserialize_json(
                data["value"]
            )
        )
    else:
        out["value"] = []
    if data.get("sources") is not None:
        import capo_cleanrooms.types.inherited_allowed_additional_analyses_source_list

        out["sources"] = (
            capo_cleanrooms.types.inherited_allowed_additional_analyses_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    return out
