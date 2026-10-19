"""Generated from Smithy shape ``com.amazonaws.ssm#LabelParameterVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.parameter_label_list
    import capo_ssm.types.ps_parameter_name
    import capo_ssm.types.ps_parameter_version


class LabelParameterVersionRequest(TypedDict, closed=True):
    name: "capo_ssm.types.ps_parameter_name.PSParameterName"
    """<p>The parameter name on which you want to attach one or more labels.</p> <note> <p>You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.</p> </note>"""
    parameter_version: NotRequired[
        "capo_ssm.types.ps_parameter_version.PSParameterVersion"
    ]
    """<p>The specific version of the parameter on which you want to attach one or more labels. If no version is specified, the system attaches the label to the latest version.</p>"""
    labels: "capo_ssm.types.parameter_label_list.ParameterLabelList"
    """<p>One or more labels to attach to the specified parameter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelParameterVersionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "parameter_version" in value:
        out["ParameterVersion"] = value["parameter_version"]
    import capo_ssm.types.parameter_label_list

    out["Labels"] = capo_ssm.types.parameter_label_list.serialize_aws_json_1_1(
        value["labels"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelParameterVersionRequest:
    out: LabelParameterVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ParameterVersion") is not None:
        out["parameter_version"] = data["ParameterVersion"]
    if data.get("Labels") is not None:
        import capo_ssm.types.parameter_label_list

        out["labels"] = capo_ssm.types.parameter_label_list.deserialize_aws_json_1_1(
            data["Labels"]
        )
    else:
        out["labels"] = []
    return out
