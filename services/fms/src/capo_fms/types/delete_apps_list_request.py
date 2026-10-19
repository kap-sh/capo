"""Generated from Smithy shape ``com.amazonaws.fms#DeleteAppsListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fms.types.list_id


class DeleteAppsListRequest(TypedDict, closed=True):
    list_id: "capo_fms.types.list_id.ListId"
    """<p>The ID of the applications list that you want to delete. You can retrieve this ID from <code>PutAppsList</code>, <code>ListAppsLists</code>, and <code>GetAppsList</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAppsListRequest) -> dict:
    out: dict = {}
    out["ListId"] = value["list_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAppsListRequest:
    out: DeleteAppsListRequest = {}  # type: ignore[typeddict-item]
    if data.get("ListId") is not None:
        out["list_id"] = data["ListId"]
    else:
        out["list_id"] = ""
    return out
