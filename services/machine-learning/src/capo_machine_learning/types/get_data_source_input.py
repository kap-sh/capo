"""Generated from Smithy shape ``com.amazonaws.machinelearning#GetDataSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.verbose


class GetDataSourceInput(TypedDict, closed=True):
    data_source_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>DataSource</code> at creation.</p>"""
    verbose: NotRequired["capo_machine_learning.types.verbose.Verbose"]
    """<p>Specifies whether the <code>GetDataSource</code> operation should return <code>DataSourceSchema</code>.</p> <p>If true, <code>DataSourceSchema</code> is returned.</p> <p>If false, <code>DataSourceSchema</code> is not returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataSourceInput) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    if "verbose" in value:
        out["Verbose"] = value["verbose"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataSourceInput:
    out: GetDataSourceInput = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("Verbose") is not None:
        out["verbose"] = data["Verbose"]
    return out
