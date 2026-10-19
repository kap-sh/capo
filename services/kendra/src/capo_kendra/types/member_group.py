"""Generated from Smithy shape ``com.amazonaws.kendra#MemberGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.group_id


class MemberGroup(TypedDict, closed=True):
    group_id: "capo_kendra.types.group_id.GroupId"
    """<p>The identifier of the sub group you want to map to a group.</p>"""
    data_source_id: NotRequired["capo_kendra.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source for the sub group you want to map to a group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberGroup) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MemberGroup:
    out: MemberGroup = {}  # type: ignore[typeddict-item]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        out["group_id"] = ""
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    return out
