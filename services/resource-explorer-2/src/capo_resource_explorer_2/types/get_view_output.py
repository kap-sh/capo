"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetViewOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.tag_map
    import capo_resource_explorer_2.types.view


class GetViewOutput(TypedDict, closed=True):
    view: NotRequired["capo_resource_explorer_2.types.view.View"]
    """<p>A structure that contains the details for the requested view.</p>"""
    tags: NotRequired["capo_resource_explorer_2.types.tag_map.TagMap"]
    """<p>Tag key and value pairs that are attached to the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetViewOutput) -> dict:
    out: dict = {}
    if "view" in value:
        import capo_resource_explorer_2.types.view

        out["View"] = capo_resource_explorer_2.types.view.serialize_json(value["view"])
    if "tags" in value:
        import capo_resource_explorer_2.types.tag_map

        out["Tags"] = capo_resource_explorer_2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetViewOutput:
    out: GetViewOutput = {}  # type: ignore[typeddict-item]
    if data.get("View") is not None:
        import capo_resource_explorer_2.types.view

        out["view"] = capo_resource_explorer_2.types.view.deserialize_json(data["View"])
    if data.get("Tags") is not None:
        import capo_resource_explorer_2.types.tag_map

        out["tags"] = capo_resource_explorer_2.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetViewOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "view" in value:
        import capo_resource_explorer_2.types.view

        out["view"] = capo_resource_explorer_2.types.view.redact_sensitive(
            value["view"]
        )
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
