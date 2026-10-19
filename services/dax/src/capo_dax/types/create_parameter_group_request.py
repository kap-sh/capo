"""Generated from Smithy shape ``com.amazonaws.dax#CreateParameterGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string


class CreateParameterGroupRequest(TypedDict, closed=True):
    parameter_group_name: "capo_dax.types.string.String"
    """<p>The name of the parameter group to apply to all of the clusters in this replication group.</p>"""
    description: NotRequired["capo_dax.types.string.String"]
    """<p>A description of the parameter group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateParameterGroupRequest:
    out: CreateParameterGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        out["parameter_group_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
