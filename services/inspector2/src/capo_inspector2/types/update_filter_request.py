"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.filter_action
    import capo_inspector2.types.filter_arn
    import capo_inspector2.types.filter_criteria
    import capo_inspector2.types.filter_description
    import capo_inspector2.types.filter_name
    import capo_inspector2.types.filter_reason


class UpdateFilterRequest(TypedDict, closed=True):
    action: NotRequired["capo_inspector2.types.filter_action.FilterAction"]
    """<p>Specifies the action that is to be applied to the findings that match the filter.</p>"""
    description: NotRequired[
        "capo_inspector2.types.filter_description.FilterDescription"
    ]
    """<p>A description of the filter.</p>"""
    filter_criteria: NotRequired["capo_inspector2.types.filter_criteria.FilterCriteria"]
    """<p>Defines the criteria to be update in the filter.</p>"""
    name: NotRequired["capo_inspector2.types.filter_name.FilterName"]
    """<p>The name of the filter.</p>"""
    filter_arn: "capo_inspector2.types.filter_arn.FilterArn"
    """<p>The Amazon Resource Number (ARN) of the filter to update.</p>"""
    reason: NotRequired["capo_inspector2.types.filter_reason.FilterReason"]
    """<p>The reason the filter was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFilterRequest) -> dict:
    out: dict = {}
    if "action" in value:
        out["action"] = value["action"]
    if "description" in value:
        out["description"] = value["description"]
    if "filter_criteria" in value:
        import capo_inspector2.types.filter_criteria

        out["filterCriteria"] = capo_inspector2.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    if "name" in value:
        out["name"] = value["name"]
    out["filterArn"] = value["filter_arn"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> UpdateFilterRequest:
    out: UpdateFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        out["action"] = data["action"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("filterCriteria") is not None:
        import capo_inspector2.types.filter_criteria

        out["filter_criteria"] = capo_inspector2.types.filter_criteria.deserialize_json(
            data["filterCriteria"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("filterArn") is not None:
        out["filter_arn"] = data["filterArn"]
    else:
        out["filter_arn"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
