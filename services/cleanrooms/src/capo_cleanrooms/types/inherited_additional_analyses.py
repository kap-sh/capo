"""Generated from Smithy shape ``com.amazonaws.cleanrooms#InheritedAdditionalAnalyses``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.additional_analyses
    import capo_cleanrooms.types.inherited_additional_analyses_source_list


class InheritedAdditionalAnalyses(TypedDict, closed=True):
    value: "capo_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    """<p>The effective additional analyses setting inherited from parent tables.</p>"""
    sources: "capo_cleanrooms.types.inherited_additional_analyses_source_list.InheritedAdditionalAnalysesSourceList"
    """<p>The list of parent tables that contribute to this inherited constraint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InheritedAdditionalAnalyses) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.additional_analyses

    out["value"] = capo_cleanrooms.types.additional_analyses.serialize_json(
        value["value"]
    )
    import capo_cleanrooms.types.inherited_additional_analyses_source_list

    out["sources"] = (
        capo_cleanrooms.types.inherited_additional_analyses_source_list.serialize_json(
            value["sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> InheritedAdditionalAnalyses:
    out: InheritedAdditionalAnalyses = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_cleanrooms.types.additional_analyses

        out["value"] = capo_cleanrooms.types.additional_analyses.deserialize_json(
            data["value"]
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_cleanrooms.types.additional_analyses.AdditionalAnalyses", ""
        )
    if data.get("sources") is not None:
        import capo_cleanrooms.types.inherited_additional_analyses_source_list

        out["sources"] = (
            capo_cleanrooms.types.inherited_additional_analyses_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    return out
