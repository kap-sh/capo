"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateLimitRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.description
    import capo_deadline.types.farm_id
    import capo_deadline.types.limit_id
    import capo_deadline.types.max_count
    import capo_deadline.types.resource_name


class UpdateLimitRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the limit.</p>"""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit to update.</p>"""
    display_name: NotRequired["capo_deadline.types.resource_name.ResourceName"]
    """<p>The new display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The new description of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    max_count: NotRequired["capo_deadline.types.max_count.MaxCount"]
    """<p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>If more than the new maximum number is currently in use, running jobs finish but no new jobs are started until the number of resources in use is below the new maximum number.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLimitRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "max_count" in value:
        out["maxCount"] = value["max_count"]
    return out


def deserialize_json(data: dict) -> UpdateLimitRequest:
    out: UpdateLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("maxCount") is not None:
        out["max_count"] = data["maxCount"]
    return out


def redact_sensitive(value: UpdateLimitRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
