"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateReplicationSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.client_token
    import capo_ssm_incidents.types.update_action_list


class UpdateReplicationSetInput(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the replication set you're updating.</p>"""
    actions: "capo_ssm_incidents.types.update_action_list.UpdateActionList"
    """<p>An action to add or delete a Region.</p>"""
    client_token: NotRequired["capo_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that the operation is called only once with the specified details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReplicationSetInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_ssm_incidents.types.update_action_list

    out["actions"] = capo_ssm_incidents.types.update_action_list.serialize_json(
        value["actions"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateReplicationSetInput:
    out: UpdateReplicationSetInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("actions") is not None:
        import capo_ssm_incidents.types.update_action_list

        out["actions"] = capo_ssm_incidents.types.update_action_list.deserialize_json(
            data["actions"]
        )
    else:
        out["actions"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
