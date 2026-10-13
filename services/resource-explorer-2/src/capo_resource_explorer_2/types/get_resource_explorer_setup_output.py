"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetResourceExplorerSetupOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.region_status_list


class GetResourceExplorerSetupOutput(TypedDict, closed=True):
    regions: NotRequired[
        "capo_resource_explorer_2.types.region_status_list.RegionStatusList"
    ]
    """<p>A list of Region status objects that describe the current state of Resource Explorer configuration in each Region.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token to use in a subsequent <code>GetResourceExplorerSetup</code> request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceExplorerSetupOutput) -> dict:
    out: dict = {}
    if "regions" in value:
        import capo_resource_explorer_2.types.region_status_list

        out["Regions"] = (
            capo_resource_explorer_2.types.region_status_list.serialize_json(
                value["regions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourceExplorerSetupOutput:
    out: GetResourceExplorerSetupOutput = {}  # type: ignore[typeddict-item]
    if data.get("Regions") is not None:
        import capo_resource_explorer_2.types.region_status_list

        out["regions"] = (
            capo_resource_explorer_2.types.region_status_list.deserialize_json(
                data["Regions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: GetResourceExplorerSetupOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "regions" in value:
        import capo_resource_explorer_2.types.region_status_list

        out["regions"] = (
            capo_resource_explorer_2.types.region_status_list.redact_sensitive(
                value["regions"]
            )
        )
    return out
