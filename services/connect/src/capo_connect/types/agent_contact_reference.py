"""Generated from Smithy shape ``com.amazonaws.connect#AgentContactReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.channel
    import capo_connect.types.contact_id
    import capo_connect.types.contact_initiation_method
    import capo_connect.types.contact_state
    import capo_connect.types.queue_reference
    import capo_connect.types.timestamp


class AgentContactReference(TypedDict, closed=True):
    contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    channel: NotRequired["capo_connect.types.channel.Channel"]
    """<p>The channel of the contact.</p>"""
    initiation_method: NotRequired[
        "capo_connect.types.contact_initiation_method.ContactInitiationMethod"
    ]
    """<p>How the contact was initiated.</p>"""
    agent_contact_state: NotRequired["capo_connect.types.contact_state.ContactState"]
    """<p>The <a href="https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html">state of the contact</a>.</p> <note> <p>When <code>AgentContactState</code> is set to <code>CONNECTED_ONHOLD</code>, <code>StateStartTimestamp</code> is not changed. Instead, <code>StateStartTimestamp</code> reflects the time the contact was <code>CONNECTED</code> to the agent.</p> </note>"""
    state_start_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The epoch timestamp when the contact state started.</p>"""
    connected_to_agent_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The time at which the contact was connected to an agent.</p>"""
    queue: NotRequired["capo_connect.types.queue_reference.QueueReference"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentContactReference) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "channel" in value:
        import capo_connect.types.channel

        out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    if "initiation_method" in value:
        import capo_connect.types.contact_initiation_method

        out["InitiationMethod"] = (
            capo_connect.types.contact_initiation_method.serialize_json(
                value["initiation_method"]
            )
        )
    if "agent_contact_state" in value:
        import capo_connect.types.contact_state

        out["AgentContactState"] = capo_connect.types.contact_state.serialize_json(
            value["agent_contact_state"]
        )
    if "state_start_timestamp" in value:
        import capo_connect.types.timestamp

        out["StateStartTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["state_start_timestamp"]
        )
    if "connected_to_agent_timestamp" in value:
        import capo_connect.types.timestamp

        out["ConnectedToAgentTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["connected_to_agent_timestamp"]
        )
    if "queue" in value:
        import capo_connect.types.queue_reference

        out["Queue"] = capo_connect.types.queue_reference.serialize_json(value["queue"])
    return out


def deserialize_json(data: dict) -> AgentContactReference:
    out: AgentContactReference = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    if data.get("InitiationMethod") is not None:
        import capo_connect.types.contact_initiation_method

        out["initiation_method"] = (
            capo_connect.types.contact_initiation_method.deserialize_json(
                data["InitiationMethod"]
            )
        )
    if data.get("AgentContactState") is not None:
        import capo_connect.types.contact_state

        out["agent_contact_state"] = capo_connect.types.contact_state.deserialize_json(
            data["AgentContactState"]
        )
    if data.get("StateStartTimestamp") is not None:
        import capo_connect.types.timestamp

        out["state_start_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["StateStartTimestamp"]
        )
    if data.get("ConnectedToAgentTimestamp") is not None:
        import capo_connect.types.timestamp

        out["connected_to_agent_timestamp"] = (
            capo_connect.types.timestamp.deserialize_json(
                data["ConnectedToAgentTimestamp"]
            )
        )
    if data.get("Queue") is not None:
        import capo_connect.types.queue_reference

        out["queue"] = capo_connect.types.queue_reference.deserialize_json(
            data["Queue"]
        )
    return out
