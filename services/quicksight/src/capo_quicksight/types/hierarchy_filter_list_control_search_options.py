"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyFilterListControlSearchOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visibility


class HierarchyFilterListControlSearchOptions(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility configuration of the search options in a hierarchy list control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyFilterListControlSearchOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> HierarchyFilterListControlSearchOptions:
    out: HierarchyFilterListControlSearchOptions = {}  # type: ignore[typeddict-item]
    if data.get("Visibility") is not None:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out
