"""Generated from Smithy shape ``com.amazonaws.amplify#CreateWebhookRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.app_id
    import capo_amplify.types.branch_name
    import capo_amplify.types.description


class CreateWebhookRequest(TypedDict, closed=True):
    app_id: "capo_amplify.types.app_id.AppId"
    """<p>The unique ID for an Amplify app. </p>"""
    branch_name: "capo_amplify.types.branch_name.BranchName"
    """<p>The name for a branch that is part of an Amplify app. </p>"""
    description: NotRequired["capo_amplify.types.description.Description"]
    """<p>The description for a webhook. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebhookRequest) -> dict:
    out: dict = {}
    out["branchName"] = value["branch_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateWebhookRequest:
    out: CreateWebhookRequest = {}  # type: ignore[typeddict-item]
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    else:
        out["branch_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
