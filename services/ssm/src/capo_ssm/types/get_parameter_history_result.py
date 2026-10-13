"""Generated from Smithy shape ``com.amazonaws.ssm#GetParameterHistoryResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.parameter_history_list


class GetParameterHistoryResult(TypedDict, closed=True):
    parameters: NotRequired[
        "capo_ssm.types.parameter_history_list.ParameterHistoryList"
    ]
    """<p>A list of parameters returned by the request.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParameterHistoryResult) -> dict:
    out: dict = {}
    if "parameters" in value:
        import capo_ssm.types.parameter_history_list

        out["Parameters"] = (
            capo_ssm.types.parameter_history_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParameterHistoryResult:
    out: GetParameterHistoryResult = {}  # type: ignore[typeddict-item]
    if data.get("Parameters") is not None:
        import capo_ssm.types.parameter_history_list

        out["parameters"] = (
            capo_ssm.types.parameter_history_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: GetParameterHistoryResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        import capo_ssm.types.parameter_history_list

        out["parameters"] = capo_ssm.types.parameter_history_list.redact_sensitive(
            value["parameters"]
        )
    return out
