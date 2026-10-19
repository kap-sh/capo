"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateDataRetentionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.data_retention_action_type
    import capo_wickr.types.network_id


class UpdateDataRetentionRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the data retention bot.</p>"""
    action_type: "capo_wickr.types.data_retention_action_type.DataRetentionActionType"
    """<p>The action to perform. Valid values are 'ENABLE' (to enable the data retention service), 'DISABLE' (to disable the service), or 'PUBKEY_MSG_ACK' (to acknowledge the public key message).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataRetentionRequest) -> dict:
    out: dict = {}
    import capo_wickr.types.data_retention_action_type

    out["actionType"] = capo_wickr.types.data_retention_action_type.serialize_json(
        value["action_type"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataRetentionRequest:
    out: UpdateDataRetentionRequest = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        import capo_wickr.types.data_retention_action_type

        out["action_type"] = (
            capo_wickr.types.data_retention_action_type.deserialize_json(
                data["actionType"]
            )
        )
    else:
        import typing

        out["action_type"] = typing.cast(
            "capo_wickr.types.data_retention_action_type.DataRetentionActionType", ""
        )
    return out
