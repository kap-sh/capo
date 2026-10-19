"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.filter_action
    import capo_inspector2.types.filter_criteria
    import capo_inspector2.types.filter_description
    import capo_inspector2.types.filter_name
    import capo_inspector2.types.filter_reason
    import capo_inspector2.types.tag_map


class CreateFilterRequest(TypedDict, closed=True):
    action: "capo_inspector2.types.filter_action.FilterAction"
    """<p>Defines the action that is to be applied to the findings that match the filter.</p>"""
    description: NotRequired[
        "capo_inspector2.types.filter_description.FilterDescription"
    ]
    """<p>A description of the filter.</p>"""
    filter_criteria: "capo_inspector2.types.filter_criteria.FilterCriteria"
    """<p>Defines the criteria to be used in the filter for querying findings.</p>"""
    name: "capo_inspector2.types.filter_name.FilterName"
    """<p>The name of the filter. Minimum length of 3. Maximum length of 64. Valid characters include alphanumeric characters, dot (.), underscore (_), and dash (-). Spaces are not allowed.</p>"""
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>A list of tags for the filter.</p>"""
    reason: NotRequired["capo_inspector2.types.filter_reason.FilterReason"]
    """<p>The reason for creating the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFilterRequest) -> dict:
    out: dict = {}
    out["action"] = value["action"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_inspector2.types.filter_criteria

    out["filterCriteria"] = capo_inspector2.types.filter_criteria.serialize_json(
        value["filter_criteria"]
    )
    out["name"] = value["name"]
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CreateFilterRequest:
    out: CreateFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("filterCriteria") is not None:
        import capo_inspector2.types.filter_criteria

        out["filter_criteria"] = capo_inspector2.types.filter_criteria.deserialize_json(
            data["filterCriteria"]
        )
    else:
        raise DeserializationError("CreateFilterRequest.filter_criteria required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
