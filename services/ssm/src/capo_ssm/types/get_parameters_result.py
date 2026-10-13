"""Generated from Smithy shape ``com.amazonaws.ssm#GetParametersResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.parameter_list
    import capo_ssm.types.parameter_name_list


class GetParametersResult(TypedDict, closed=True):
    parameters: NotRequired["capo_ssm.types.parameter_list.ParameterList"]
    """<p>A list of details for a parameter.</p>"""
    invalid_parameters: NotRequired[
        "capo_ssm.types.parameter_name_list.ParameterNameList"
    ]
    """<p>A list of parameters that aren't formatted correctly or don't run during an execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParametersResult) -> dict:
    out: dict = {}
    if "parameters" in value:
        import capo_ssm.types.parameter_list

        out["Parameters"] = capo_ssm.types.parameter_list.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "invalid_parameters" in value:
        import capo_ssm.types.parameter_name_list

        out["InvalidParameters"] = (
            capo_ssm.types.parameter_name_list.serialize_aws_json_1_1(
                value["invalid_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParametersResult:
    out: GetParametersResult = {}  # type: ignore[typeddict-item]
    if data.get("Parameters") is not None:
        import capo_ssm.types.parameter_list

        out["parameters"] = capo_ssm.types.parameter_list.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if data.get("InvalidParameters") is not None:
        import capo_ssm.types.parameter_name_list

        out["invalid_parameters"] = (
            capo_ssm.types.parameter_name_list.deserialize_aws_json_1_1(
                data["InvalidParameters"]
            )
        )
    return out


def redact_sensitive(value: GetParametersResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        import capo_ssm.types.parameter_list

        out["parameters"] = capo_ssm.types.parameter_list.redact_sensitive(
            value["parameters"]
        )
    return out
