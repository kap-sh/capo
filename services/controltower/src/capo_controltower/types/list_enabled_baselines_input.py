"""Generated from Smithy shape ``com.amazonaws.controltower#ListEnabledBaselinesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_filter
    import capo_controltower.types.list_enabled_baselines_max_results
    import capo_controltower.types.list_enabled_baselines_next_token


class ListEnabledBaselinesInput(TypedDict, closed=True):
    filter: NotRequired[
        "capo_controltower.types.enabled_baseline_filter.EnabledBaselineFilter"
    ]
    """<p>A filter applied on the <code>ListEnabledBaseline</code> operation. Allowed filters are <code>baselineIdentifiers</code> and <code>targetIdentifiers</code>. The filter can be applied for either, or both.</p>"""
    next_token: NotRequired[
        "capo_controltower.types.list_enabled_baselines_next_token.ListEnabledBaselinesNextToken"
    ]
    """<p>A pagination token.</p>"""
    max_results: NotRequired[
        "capo_controltower.types.list_enabled_baselines_max_results.ListEnabledBaselinesMaxResults"
    ]
    """<p>The maximum number of results to be shown.</p>"""
    include_children: NotRequired["bool"]
    """<p>A value that can be set to include the child enabled baselines in responses. The default value is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnabledBaselinesInput) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_controltower.types.enabled_baseline_filter

        out["filter"] = capo_controltower.types.enabled_baseline_filter.serialize_json(
            value["filter"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "include_children" in value:
        out["includeChildren"] = value["include_children"]
    return out


def deserialize_json(data: dict) -> ListEnabledBaselinesInput:
    out: ListEnabledBaselinesInput = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_controltower.types.enabled_baseline_filter

        out["filter"] = (
            capo_controltower.types.enabled_baseline_filter.deserialize_json(
                data["filter"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("includeChildren") is not None:
        out["include_children"] = data["includeChildren"]
    return out
