"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#RegionStatus``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.index_status
    import capo_resource_explorer_2.types.view_status


class RegionStatus(TypedDict, closed=True):
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region for which this status information applies.</p>"""
    index: NotRequired["capo_resource_explorer_2.types.index_status.IndexStatus"]
    """<p>The status information for the Resource Explorer index in this Region.</p>"""
    view: NotRequired["capo_resource_explorer_2.types.view_status.ViewStatus"]
    """<p>The status information for the Resource Explorer view in this Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionStatus) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "index" in value:
        import capo_resource_explorer_2.types.index_status

        out["Index"] = capo_resource_explorer_2.types.index_status.serialize_json(
            value["index"]
        )
    if "view" in value:
        import capo_resource_explorer_2.types.view_status

        out["View"] = capo_resource_explorer_2.types.view_status.serialize_json(
            value["view"]
        )
    return out


def deserialize_json(data: dict) -> RegionStatus:
    out: RegionStatus = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("Index") is not None:
        import capo_resource_explorer_2.types.index_status

        out["index"] = capo_resource_explorer_2.types.index_status.deserialize_json(
            data["Index"]
        )
    if data.get("View") is not None:
        import capo_resource_explorer_2.types.view_status

        out["view"] = capo_resource_explorer_2.types.view_status.deserialize_json(
            data["View"]
        )
    return out


def redact_sensitive(value: RegionStatus) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "view" in value:
        import capo_resource_explorer_2.types.view_status

        out["view"] = capo_resource_explorer_2.types.view_status.redact_sensitive(
            value["view"]
        )
    return out
