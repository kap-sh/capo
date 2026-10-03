"""Generated from Smithy shape ``com.amazonaws.connect#UpdateParticipantRoleConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.update_participant_role_config_channel_info


class UpdateParticipantRoleConfigRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    channel_configuration: "capo_connect.types.update_participant_role_config_channel_info.UpdateParticipantRoleConfigChannelInfo"
    """<p>The Connect Customer channel you want to configure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateParticipantRoleConfigRequest) -> dict:
    out: dict = {}
    import capo_connect.types.update_participant_role_config_channel_info

    out["ChannelConfiguration"] = (
        capo_connect.types.update_participant_role_config_channel_info.serialize_json(
            value["channel_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateParticipantRoleConfigRequest:
    out: UpdateParticipantRoleConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ChannelConfiguration") is not None:
        import capo_connect.types.update_participant_role_config_channel_info

        out["channel_configuration"] = (
            capo_connect.types.update_participant_role_config_channel_info.deserialize_json(
                data["ChannelConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateParticipantRoleConfigRequest.channel_configuration required"
        )
    return out
