"""Generated from Smithy shape ``com.amazonaws.kendra#DescribePrincipalMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.group_id
    import capo_kendra.types.index_id


class DescribePrincipalMappingRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index required to check the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups.</p>"""
    data_source_id: NotRequired["capo_kendra.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source to check the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups.</p>"""
    group_id: "capo_kendra.types.group_id.GroupId"
    """<p>The identifier of the group required to check the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePrincipalMappingRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    out["GroupId"] = value["group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePrincipalMappingRequest:
    out: DescribePrincipalMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        out["group_id"] = ""
    return out
