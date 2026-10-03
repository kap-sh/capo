"""Generated from Smithy shape ``com.amazonaws.controltower#ListEnabledControlsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.enabled_control_filter
    import capo_controltower.types.max_results
    import capo_controltower.types.target_identifier


class ListEnabledControlsInput(TypedDict, closed=True):
    target_identifier: NotRequired[
        "capo_controltower.types.target_identifier.TargetIdentifier"
    ]
    """<p>The ARN of the target. The value depends on the target type:</p> <ul> <li> <p>Organizational unit (OU) – Specify the ARN of the OU.</p> </li> <li> <p>Account – Specify the ARN of the account.</p> </li> </ul> <p>For information on how to find the <code>targetIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to continue the list from a previous API call with the same parameters.</p>"""
    max_results: NotRequired["capo_controltower.types.max_results.MaxResults"]
    """<p>How many results to return per API call.</p>"""
    filter: NotRequired[
        "capo_controltower.types.enabled_control_filter.EnabledControlFilter"
    ]
    """<p>An input filter for the <code>ListEnabledControls</code> API that lets you select the types of control operations to view.</p>"""
    include_children: "bool"
    """<p>Specifies whether to include enabled controls from child organizational units and child accounts in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnabledControlsInput) -> dict:
    out: dict = {}
    if "target_identifier" in value:
        out["targetIdentifier"] = value["target_identifier"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import capo_controltower.types.enabled_control_filter

        out["filter"] = capo_controltower.types.enabled_control_filter.serialize_json(
            value["filter"]
        )
    out["includeChildren"] = value.get("include_children", False)
    return out


def deserialize_json(data: dict) -> ListEnabledControlsInput:
    out: ListEnabledControlsInput = {}  # type: ignore[typeddict-item]
    if data.get("targetIdentifier") is not None:
        out["target_identifier"] = data["targetIdentifier"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filter") is not None:
        import capo_controltower.types.enabled_control_filter

        out["filter"] = capo_controltower.types.enabled_control_filter.deserialize_json(
            data["filter"]
        )
    if data.get("includeChildren") is not None:
        out["include_children"] = data["includeChildren"]
    else:
        out["include_children"] = False
    return out
