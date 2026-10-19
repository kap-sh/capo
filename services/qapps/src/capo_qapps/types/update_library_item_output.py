"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateLibraryItemOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.app_version
    import capo_qapps.types.category_list
    import capo_qapps.types.q_apps_timestamp
    import capo_qapps.types.uuid


class UpdateLibraryItemOutput(TypedDict, closed=True):
    library_item_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the updated library item.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App associated with the library item.</p>"""
    app_version: "capo_qapps.types.app_version.AppVersion"
    """<p>The version of the Q App associated with the library item.</p>"""
    categories: "capo_qapps.types.category_list.CategoryList"
    """<p>The categories associated with the updated library item.</p>"""
    status: "str"
    """<p>The new status of the updated library item.</p>"""
    created_at: "capo_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the library item was originally created.</p>"""
    created_by: "str"
    """<p>The user who originally created the library item.</p>"""
    updated_at: NotRequired["capo_qapps.types.q_apps_timestamp.QAppsTimestamp"]
    """<p>The date and time the library item was last updated.</p>"""
    updated_by: NotRequired["str"]
    """<p>The user who last updated the library item.</p>"""
    rating_count: "int"
    """<p>The number of ratings the library item has received.</p>"""
    is_rated_by_user: NotRequired["bool"]
    """<p>Whether the current user has rated the library item.</p>"""
    user_count: NotRequired["int"]
    """<p>The number of users who have the associated Q App.</p>"""
    is_verified: NotRequired["bool"]
    """<p>Indicates whether the library item has been verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLibraryItemOutput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    out["appId"] = value["app_id"]
    out["appVersion"] = value["app_version"]
    import capo_qapps.types.category_list

    out["categories"] = capo_qapps.types.category_list.serialize_json(
        value["categories"]
    )
    out["status"] = value["status"]
    import capo_qapps.types.q_apps_timestamp

    out["createdAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_qapps.types.q_apps_timestamp

        out["updatedAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["ratingCount"] = value["rating_count"]
    if "is_rated_by_user" in value:
        out["isRatedByUser"] = value["is_rated_by_user"]
    if "user_count" in value:
        out["userCount"] = value["user_count"]
    if "is_verified" in value:
        out["isVerified"] = value["is_verified"]
    return out


def deserialize_json(data: dict) -> UpdateLibraryItemOutput:
    out: UpdateLibraryItemOutput = {}  # type: ignore[typeddict-item]
    if data.get("libraryItemId") is not None:
        out["library_item_id"] = data["libraryItemId"]
    else:
        out["library_item_id"] = ""
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        out["app_version"] = 0
    if data.get("categories") is not None:
        import capo_qapps.types.category_list

        out["categories"] = capo_qapps.types.category_list.deserialize_json(
            data["categories"]
        )
    else:
        out["categories"] = []
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
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
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("ratingCount") is not None:
        out["rating_count"] = data["ratingCount"]
    else:
        out["rating_count"] = 0
    if data.get("isRatedByUser") is not None:
        out["is_rated_by_user"] = data["isRatedByUser"]
    if data.get("userCount") is not None:
        out["user_count"] = data["userCount"]
    if data.get("isVerified") is not None:
        out["is_verified"] = data["isVerified"]
    return out
