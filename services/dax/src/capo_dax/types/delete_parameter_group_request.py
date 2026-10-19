"""Generated from Smithy shape ``com.amazonaws.dax#DeleteParameterGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string


class DeleteParameterGroupRequest(TypedDict, closed=True):
    parameter_group_name: "capo_dax.types.string.String"
    """<p>The name of the parameter group to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteParameterGroupRequest:
    out: DeleteParameterGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        out["parameter_group_name"] = ""
    return out
