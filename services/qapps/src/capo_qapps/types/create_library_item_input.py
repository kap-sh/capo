"""Generated from Smithy shape ``com.amazonaws.qapps#CreateLibraryItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.app_version
    import capo_qapps.types.category_id_list
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class CreateLibraryItemInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Amazon Q App to publish to the library.</p>"""
    app_version: "capo_qapps.types.app_version.AppVersion"
    """<p>The version of the Amazon Q App to publish to the library.</p>"""
    categories: "capo_qapps.types.category_id_list.CategoryIdList"
    """<p>The categories to associate with the library item for easier discovery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLibraryItemInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appVersion"] = value["app_version"]
    import capo_qapps.types.category_id_list

    out["categories"] = capo_qapps.types.category_id_list.serialize_json(
        value["categories"]
    )
    return out


def deserialize_json(data: dict) -> CreateLibraryItemInput:
    out: CreateLibraryItemInput = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        out["app_version"] = 0
    if data.get("categories") is not None:
        import capo_qapps.types.category_id_list

        out["categories"] = capo_qapps.types.category_id_list.deserialize_json(
            data["categories"]
        )
    else:
        out["categories"] = []
    return out
