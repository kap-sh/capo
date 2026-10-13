"""Generated from Smithy shape ``com.amazonaws.deadline#CreateLimitRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.amount_requirement_name
    import capo_deadline.types.client_token
    import capo_deadline.types.description
    import capo_deadline.types.farm_id
    import capo_deadline.types.max_count
    import capo_deadline.types.resource_name


class CreateLimitRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm that contains the limit.</p>"""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    amount_requirement_name: (
        "capo_deadline.types.amount_requirement_name.AmountRequirementName"
    )
    """<p>The value that you specify as the <code>name</code> in the <code>amounts</code> field of the <code>hostRequirements</code> in a step of a job template to declare the limit requirement.</p>"""
    max_count: "capo_deadline.types.max_count.MaxCount"
    """<p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>"""
    description: "capo_deadline.types.description.Description"
    """<p>A description of the limit. A description helps you identify the purpose of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLimitRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    out["amountRequirementName"] = value["amount_requirement_name"]
    out["maxCount"] = value["max_count"]
    out["description"] = value.get("description", "")
    return out


def deserialize_json(data: dict) -> CreateLimitRequest:
    out: CreateLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateLimitRequest.display_name required")
    if data.get("amountRequirementName") is not None:
        out["amount_requirement_name"] = data["amountRequirementName"]
    else:
        raise DeserializationError(
            "CreateLimitRequest.amount_requirement_name required"
        )
    if data.get("maxCount") is not None:
        out["max_count"] = data["maxCount"]
    else:
        raise DeserializationError("CreateLimitRequest.max_count required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out


def redact_sensitive(value: CreateLimitRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
