"""Generated from Smithy shape ``com.amazonaws.machinelearning#UpdateDataSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name


class UpdateDataSourceInput(TypedDict, closed=True):
    data_source_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>DataSource</code> during creation.</p>"""
    data_source_name: "capo_machine_learning.types.entity_name.EntityName"
    """<p>A new user-supplied name or description of the <code>DataSource</code> that will replace the current description. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataSourceInput) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    out["DataSourceName"] = value["data_source_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataSourceInput:
    out: UpdateDataSourceInput = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("DataSourceName") is not None:
        out["data_source_name"] = data["DataSourceName"]
    else:
        out["data_source_name"] = ""
    return out
