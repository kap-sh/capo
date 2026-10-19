"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobAnalysisOverrideParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name


class AssetBundleImportJobAnalysisOverrideParameters(TypedDict, closed=True):
    analysis_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the analysis that you ant to apply overrides to.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobAnalysisOverrideParameters) -> dict:
    out: dict = {}
    out["AnalysisId"] = value["analysis_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobAnalysisOverrideParameters:
    out: AssetBundleImportJobAnalysisOverrideParameters = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisId") is not None:
        out["analysis_id"] = data["AnalysisId"]
    else:
        out["analysis_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
