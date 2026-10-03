"""Generated from Smithy shape ``com.amazonaws.ssm#LabelParameterVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.parameter_label_list
    import capo_ssm.types.ps_parameter_version


class LabelParameterVersionResult(TypedDict, closed=True):
    invalid_labels: NotRequired[
        "capo_ssm.types.parameter_label_list.ParameterLabelList"
    ]
    """<p>The label doesn't meet the requirements. For information about parameter label requirements, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html">Working with parameter labels</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    parameter_version: "capo_ssm.types.ps_parameter_version.PSParameterVersion"
    """<p>The version of the parameter that has been labeled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelParameterVersionResult) -> dict:
    out: dict = {}
    if "invalid_labels" in value:
        import capo_ssm.types.parameter_label_list

        out["InvalidLabels"] = (
            capo_ssm.types.parameter_label_list.serialize_aws_json_1_1(
                value["invalid_labels"]
            )
        )
    out["ParameterVersion"] = value.get("parameter_version", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelParameterVersionResult:
    out: LabelParameterVersionResult = {}  # type: ignore[typeddict-item]
    if data.get("InvalidLabels") is not None:
        import capo_ssm.types.parameter_label_list

        out["invalid_labels"] = (
            capo_ssm.types.parameter_label_list.deserialize_aws_json_1_1(
                data["InvalidLabels"]
            )
        )
    if data.get("ParameterVersion") is not None:
        out["parameter_version"] = data["ParameterVersion"]
    else:
        out["parameter_version"] = 0
    return out
