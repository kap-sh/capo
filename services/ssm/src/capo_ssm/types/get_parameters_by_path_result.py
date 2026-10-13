"""Generated from Smithy shape ``com.amazonaws.ssm#GetParametersByPathResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.parameter_list


class GetParametersByPathResult(TypedDict, closed=True):
    parameters: NotRequired["capo_ssm.types.parameter_list.ParameterList"]
    """<p>A list of parameters found in the specified hierarchy.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParametersByPathResult) -> dict:
    out: dict = {}
    if "parameters" in value:
        import capo_ssm.types.parameter_list

        out["Parameters"] = capo_ssm.types.parameter_list.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParametersByPathResult:
    out: GetParametersByPathResult = {}  # type: ignore[typeddict-item]
    if data.get("Parameters") is not None:
        import capo_ssm.types.parameter_list

        out["parameters"] = capo_ssm.types.parameter_list.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: GetParametersByPathResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        import capo_ssm.types.parameter_list

        out["parameters"] = capo_ssm.types.parameter_list.redact_sensitive(
            value["parameters"]
        )
    return out
