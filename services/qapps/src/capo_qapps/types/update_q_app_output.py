"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.app_arn
    import capo_qapps.types.app_required_capabilities
    import capo_qapps.types.app_status
    import capo_qapps.types.app_version
    import capo_qapps.types.description
    import capo_qapps.types.initial_prompt
    import capo_qapps.types.q_apps_timestamp
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class UpdateQAppOutput(TypedDict, closed=True):
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the updated Q App.</p>"""
    app_arn: "capo_qapps.types.app_arn.AppArn"
    """<p>The Amazon Resource Name (ARN) of the updated Q App.</p>"""
    title: "capo_qapps.types.title.Title"
    """<p>The new title of the updated Q App.</p>"""
    description: NotRequired["capo_qapps.types.description.Description"]
    """<p>The new description of the updated Q App.</p>"""
    initial_prompt: NotRequired["capo_qapps.types.initial_prompt.InitialPrompt"]
    """<p>The initial prompt for the updated Q App.</p>"""
    app_version: "capo_qapps.types.app_version.AppVersion"
    """<p>The new version of the updated Q App.</p>"""
    status: "capo_qapps.types.app_status.AppStatus"
    """<p>The status of the updated Q App.</p>"""
    created_at: "capo_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the Q App was originally created.</p>"""
    created_by: "str"
    """<p>The user who originally created the Q App.</p>"""
    updated_at: "capo_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the Q App was last updated.</p>"""
    updated_by: "str"
    """<p>The user who last updated the Q App.</p>"""
    required_capabilities: NotRequired[
        "capo_qapps.types.app_required_capabilities.AppRequiredCapabilities"
    ]
    """<p>The capabilities required for the updated Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppOutput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appArn"] = value["app_arn"]
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "initial_prompt" in value:
        out["initialPrompt"] = value["initial_prompt"]
    out["appVersion"] = value["app_version"]
    import capo_qapps.types.app_status

    out["status"] = capo_qapps.types.app_status.serialize_json(value["status"])
    import capo_qapps.types.q_apps_timestamp

    out["createdAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    import capo_qapps.types.q_apps_timestamp

    out["updatedAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
        value["updated_at"]
    )
    out["updatedBy"] = value["updated_by"]
    if "required_capabilities" in value:
        import capo_qapps.types.app_required_capabilities

        out["requiredCapabilities"] = (
            capo_qapps.types.app_required_capabilities.serialize_json(
                value["required_capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateQAppOutput:
    out: UpdateQAppOutput = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        out["app_arn"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("initialPrompt") is not None:
        out["initial_prompt"] = data["initialPrompt"]
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        out["app_version"] = 0
    if data.get("status") is not None:
        import capo_qapps.types.app_status

        out["status"] = capo_qapps.types.app_status.deserialize_json(data["status"])
    else:
        import typing

        out["status"] = typing.cast("capo_qapps.types.app_status.AppStatus", "")
    if data.get("createdAt") is not None:
        import capo_qapps.types.q_apps_timestamp

        out["created_at"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("updatedAt") is not None:
        import capo_qapps.types.q_apps_timestamp

        out["updated_at"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    else:
        out["updated_by"] = ""
    if data.get("requiredCapabilities") is not None:
        import capo_qapps.types.app_required_capabilities

        out["required_capabilities"] = (
            capo_qapps.types.app_required_capabilities.deserialize_json(
                data["requiredCapabilities"]
            )
        )
    return out
