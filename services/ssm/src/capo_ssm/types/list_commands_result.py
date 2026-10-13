"""Generated from Smithy shape ``com.amazonaws.ssm#ListCommandsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.command_list
    import capo_ssm.types.next_token


class ListCommandsResult(TypedDict, closed=True):
    commands: NotRequired["capo_ssm.types.command_list.CommandList"]
    """<p>(Optional) The list of commands requested by the user. </p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandsResult) -> dict:
    out: dict = {}
    if "commands" in value:
        import capo_ssm.types.command_list

        out["Commands"] = capo_ssm.types.command_list.serialize_aws_json_1_1(
            value["commands"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommandsResult:
    out: ListCommandsResult = {}  # type: ignore[typeddict-item]
    if data.get("Commands") is not None:
        import capo_ssm.types.command_list

        out["commands"] = capo_ssm.types.command_list.deserialize_aws_json_1_1(
            data["Commands"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListCommandsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "commands" in value:
        import capo_ssm.types.command_list

        out["commands"] = capo_ssm.types.command_list.redact_sensitive(
            value["commands"]
        )
    return out
