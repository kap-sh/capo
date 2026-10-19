"""Generated from Smithy shape ``com.amazonaws.memorydb#ResetParameterGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_memorydb.types.boolean
    import capo_memorydb.types.parameter_name_list
    import capo_memorydb.types.string


class ResetParameterGroupRequest(TypedDict, closed=True):
    parameter_group_name: "capo_memorydb.types.string.String"
    """<p>The name of the parameter group to reset.</p>"""
    all_parameters: NotRequired["capo_memorydb.types.boolean.Boolean"]
    """<p>If true, all parameters in the parameter group are reset to their default values. If false, only the parameters listed by ParameterNames are reset to their default values.</p>"""
    parameter_names: NotRequired[
        "capo_memorydb.types.parameter_name_list.ParameterNameList"
    ]
    """<p>An array of parameter names to reset to their default values. If AllParameters is true, do not use ParameterNames. If AllParameters is false, you must specify the name of at least one parameter to reset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    if "all_parameters" in value:
        out["AllParameters"] = value["all_parameters"]
    if "parameter_names" in value:
        import capo_memorydb.types.parameter_name_list

        out["ParameterNames"] = (
            capo_memorydb.types.parameter_name_list.serialize_aws_json_1_1(
                value["parameter_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetParameterGroupRequest:
    out: ResetParameterGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        raise DeserializationError(
            "ResetParameterGroupRequest.parameter_group_name required"
        )
    if data.get("AllParameters") is not None:
        out["all_parameters"] = data["AllParameters"]
    if data.get("ParameterNames") is not None:
        import capo_memorydb.types.parameter_name_list

        out["parameter_names"] = (
            capo_memorydb.types.parameter_name_list.deserialize_aws_json_1_1(
                data["ParameterNames"]
            )
        )
    return out
