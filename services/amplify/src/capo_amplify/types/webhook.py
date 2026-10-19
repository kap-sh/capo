"""Generated from Smithy shape ``com.amazonaws.amplify#Webhook``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.app_id
    import capo_amplify.types.branch_name
    import capo_amplify.types.create_time
    import capo_amplify.types.description
    import capo_amplify.types.update_time
    import capo_amplify.types.webhook_arn
    import capo_amplify.types.webhook_id
    import capo_amplify.types.webhook_url


class Webhook(TypedDict, closed=True):
    webhook_arn: "capo_amplify.types.webhook_arn.WebhookArn"
    """<p>The Amazon Resource Name (ARN) for the webhook. </p>"""
    webhook_id: "capo_amplify.types.webhook_id.WebhookId"
    """<p>The ID of the webhook. </p>"""
    webhook_url: "capo_amplify.types.webhook_url.WebhookUrl"
    """<p>The URL of the webhook. </p>"""
    app_id: NotRequired["capo_amplify.types.app_id.AppId"]
    """<p>The unique ID of an Amplify app.</p>"""
    branch_name: "capo_amplify.types.branch_name.BranchName"
    """<p>The name for a branch that is part of an Amplify app. </p>"""
    description: "capo_amplify.types.description.Description"
    """<p>The description for a webhook. </p>"""
    create_time: "capo_amplify.types.create_time.CreateTime"
    """<p>A timestamp of when Amplify created the webhook in your Git repository.</p>"""
    update_time: "capo_amplify.types.update_time.UpdateTime"
    """<p>A timestamp of when Amplify updated the webhook in your Git repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Webhook) -> dict:
    out: dict = {}
    out["webhookArn"] = value["webhook_arn"]
    out["webhookId"] = value["webhook_id"]
    out["webhookUrl"] = value["webhook_url"]
    if "app_id" in value:
        out["appId"] = value["app_id"]
    out["branchName"] = value["branch_name"]
    out["description"] = value["description"]
    import capo_amplify.types.create_time

    out["createTime"] = capo_amplify.types.create_time.serialize_json(
        value["create_time"]
    )
    import capo_amplify.types.update_time

    out["updateTime"] = capo_amplify.types.update_time.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> Webhook:
    out: Webhook = {}  # type: ignore[typeddict-item]
    if data.get("webhookArn") is not None:
        out["webhook_arn"] = data["webhookArn"]
    else:
        out["webhook_arn"] = ""
    if data.get("webhookId") is not None:
        out["webhook_id"] = data["webhookId"]
    else:
        out["webhook_id"] = ""
    if data.get("webhookUrl") is not None:
        out["webhook_url"] = data["webhookUrl"]
    else:
        out["webhook_url"] = ""
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    else:
        out["branch_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("createTime") is not None:
        import capo_amplify.types.create_time

        out["create_time"] = capo_amplify.types.create_time.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import capo_amplify.types.update_time

        out["update_time"] = capo_amplify.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
