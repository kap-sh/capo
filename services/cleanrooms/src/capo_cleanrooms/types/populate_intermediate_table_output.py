"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PopulateIntermediateTableOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_identifier
    import capo_cleanrooms.types.populate_intermediate_table_analysis_type
    import capo_cleanrooms.types.uuid


class PopulateIntermediateTableOutput(TypedDict, closed=True):
    analysis_id: "capo_cleanrooms.types.analysis_identifier.AnalysisIdentifier"
    """<p>The identifier for the protected query execution that populated the intermediate table.</p>"""
    analysis_type: "capo_cleanrooms.types.populate_intermediate_table_analysis_type.PopulateIntermediateTableAnalysisType"
    """<p>The type of analysis performed to populate the intermediate table.</p>"""
    version_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the version created by this population operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PopulateIntermediateTableOutput) -> dict:
    out: dict = {}
    out["analysisId"] = value["analysis_id"]
    import capo_cleanrooms.types.populate_intermediate_table_analysis_type

    out["analysisType"] = (
        capo_cleanrooms.types.populate_intermediate_table_analysis_type.serialize_json(
            value["analysis_type"]
        )
    )
    out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> PopulateIntermediateTableOutput:
    out: PopulateIntermediateTableOutput = {}  # type: ignore[typeddict-item]
    if data.get("analysisId") is not None:
        out["analysis_id"] = data["analysisId"]
    else:
        out["analysis_id"] = ""
    if data.get("analysisType") is not None:
        import capo_cleanrooms.types.populate_intermediate_table_analysis_type

        out["analysis_type"] = (
            capo_cleanrooms.types.populate_intermediate_table_analysis_type.deserialize_json(
                data["analysisType"]
            )
        )
    else:
        import typing

        out["analysis_type"] = typing.cast(
            "capo_cleanrooms.types.populate_intermediate_table_analysis_type.PopulateIntermediateTableAnalysisType",
            "",
        )
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        out["version_id"] = ""
    return out
