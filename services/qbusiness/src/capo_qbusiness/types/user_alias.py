"""Generated from Smithy shape ``com.amazonaws.qbusiness#UserAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_source_id
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.string


class UserAlias(TypedDict, closed=True):
    index_id: NotRequired["capo_qbusiness.types.index_id.IndexId"]
    """<p>The identifier of the index that the user aliases are associated with.</p>"""
    data_source_id: NotRequired["capo_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source that the user aliases are associated with.</p>"""
    user_id: "capo_qbusiness.types.string.String"
    """<p>The identifier of the user id associated with the user aliases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAlias) -> dict:
    out: dict = {}
    if "index_id" in value:
        out["indexId"] = value["index_id"]
    if "data_source_id" in value:
        out["dataSourceId"] = value["data_source_id"]
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> UserAlias:
    out: UserAlias = {}  # type: ignore[typeddict-item]
    if data.get("indexId") is not None:
        out["index_id"] = data["indexId"]
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    return out
