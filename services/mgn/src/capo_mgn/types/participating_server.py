"""Generated from Smithy shape ``com.amazonaws.mgn#ParticipatingServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.ec2_instance_id
    import capo_mgn.types.launch_status
    import capo_mgn.types.post_launch_actions_status
    import capo_mgn.types.source_server_id


class ParticipatingServer(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>Participating server Source Server ID.</p>"""
    launch_status: NotRequired["capo_mgn.types.launch_status.LaunchStatus"]
    """<p>Participating server launch status.</p>"""
    launched_ec2_instance_id: NotRequired[
        "capo_mgn.types.ec2_instance_id.EC2InstanceID"
    ]
    """<p>Participating server's launched ec2 instance ID.</p>"""
    post_launch_actions_status: NotRequired[
        "capo_mgn.types.post_launch_actions_status.PostLaunchActionsStatus"
    ]
    """<p>Participating server's Post Launch Actions Status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingServer) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "launch_status" in value:
        out["launchStatus"] = value["launch_status"]
    if "launched_ec2_instance_id" in value:
        out["launchedEc2InstanceID"] = value["launched_ec2_instance_id"]
    if "post_launch_actions_status" in value:
        import capo_mgn.types.post_launch_actions_status

        out["postLaunchActionsStatus"] = (
            capo_mgn.types.post_launch_actions_status.serialize_json(
                value["post_launch_actions_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParticipatingServer:
    out: ParticipatingServer = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("launchStatus") is not None:
        out["launch_status"] = data["launchStatus"]
    if data.get("launchedEc2InstanceID") is not None:
        out["launched_ec2_instance_id"] = data["launchedEc2InstanceID"]
    if data.get("postLaunchActionsStatus") is not None:
        import capo_mgn.types.post_launch_actions_status

        out["post_launch_actions_status"] = (
            capo_mgn.types.post_launch_actions_status.deserialize_json(
                data["postLaunchActionsStatus"]
            )
        )
    return out
