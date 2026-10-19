"""Generated from Smithy shape ``com.amazonaws.ssm#CancelCommandRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.command_id
    import capo_ssm.types.instance_id_list


class CancelCommandRequest(TypedDict, closed=True):
    command_id: "capo_ssm.types.command_id.CommandId"
    """<p>The ID of the command you want to cancel.</p>"""
    instance_ids: NotRequired["capo_ssm.types.instance_id_list.InstanceIdList"]
    """<p>(Optional) A list of managed node IDs on which you want to cancel the command. If not provided, the command is canceled on every node on which it was requested.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelCommandRequest) -> dict:
    out: dict = {}
    out["CommandId"] = value["command_id"]
    if "instance_ids" in value:
        import capo_ssm.types.instance_id_list

        out["InstanceIds"] = capo_ssm.types.instance_id_list.serialize_aws_json_1_1(
            value["instance_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelCommandRequest:
    out: CancelCommandRequest = {}  # type: ignore[typeddict-item]
    if data.get("CommandId") is not None:
        out["command_id"] = data["CommandId"]
    else:
        out["command_id"] = ""
    if data.get("InstanceIds") is not None:
        import capo_ssm.types.instance_id_list

        out["instance_ids"] = capo_ssm.types.instance_id_list.deserialize_aws_json_1_1(
            data["InstanceIds"]
        )
    return out
