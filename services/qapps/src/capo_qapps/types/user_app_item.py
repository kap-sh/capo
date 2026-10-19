"""Generated from Smithy shape ``com.amazonaws.qapps#UserAppItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.app_arn
    import capo_qapps.types.description
    import capo_qapps.types.q_apps_timestamp
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class UserAppItem(TypedDict, closed=True):
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App.</p>"""
    app_arn: "capo_qapps.types.app_arn.AppArn"
    """<p>The Amazon Resource Name (ARN) of the Q App.</p>"""
    title: "capo_qapps.types.title.Title"
    """<p>The title of the Q App.</p>"""
    description: NotRequired["capo_qapps.types.description.Description"]
    """<p>The description of the Q App.</p>"""
    created_at: "capo_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the user's association with the Q App was created.</p>"""
    can_edit: NotRequired["bool"]
    """<p>A flag indicating whether the user can edit the Q App.</p>"""
    status: NotRequired["str"]
    """<p>The status of the user's association with the Q App.</p>"""
    is_verified: "bool"
    """<p>Indicates whether the Q App has been verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAppItem) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appArn"] = value["app_arn"]
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_qapps.types.q_apps_timestamp

    out["createdAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
        value["created_at"]
    )
    if "can_edit" in value:
        out["canEdit"] = value["can_edit"]
    if "status" in value:
        out["status"] = value["status"]
    out["isVerified"] = value.get("is_verified", False)
    return out


def deserialize_json(data: dict) -> UserAppItem:
    out: UserAppItem = {}  # type: ignore[typeddict-item]
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
    if data.get("createdAt") is not None:
        import capo_qapps.types.q_apps_timestamp

        out["created_at"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("canEdit") is not None:
        out["can_edit"] = data["canEdit"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("isVerified") is not None:
        out["is_verified"] = data["isVerified"]
    else:
        out["is_verified"] = False
    return out
