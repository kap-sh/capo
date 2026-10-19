"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateParameterGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.parameter_name_value_list
    import capo_memorydb.types.string


class UpdateParameterGroupRequest(TypedDict, closed=True):
    parameter_group_name: "capo_memorydb.types.string.String"
    """<p>The name of the parameter group to update.</p>"""
    parameter_name_values: (
        "capo_memorydb.types.parameter_name_value_list.ParameterNameValueList"
    )
    """<p>An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be updated per request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    import capo_memorydb.types.parameter_name_value_list

    out["ParameterNameValues"] = (
        capo_memorydb.types.parameter_name_value_list.serialize_aws_json_1_1(
            value["parameter_name_values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateParameterGroupRequest:
    out: UpdateParameterGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        out["parameter_group_name"] = ""
    if data.get("ParameterNameValues") is not None:
        import capo_memorydb.types.parameter_name_value_list

        out["parameter_name_values"] = (
            capo_memorydb.types.parameter_name_value_list.deserialize_aws_json_1_1(
                data["ParameterNameValues"]
            )
        )
    else:
        out["parameter_name_values"] = []
    return out
