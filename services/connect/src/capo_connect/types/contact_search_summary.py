"""Generated from Smithy shape ``com.amazonaws.connect#ContactSearchSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.channel
    import capo_connect.types.contact_id
    import capo_connect.types.contact_initiation_method
    import capo_connect.types.contact_search_summary_agent_info
    import capo_connect.types.contact_search_summary_ai_agent_info_list
    import capo_connect.types.contact_search_summary_queue_info
    import capo_connect.types.contact_search_summary_segment_attributes
    import capo_connect.types.contact_tag_map
    import capo_connect.types.global_resiliency_metadata
    import capo_connect.types.name
    import capo_connect.types.routing_criteria
    import capo_connect.types.timestamp


class ContactSearchSummary(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the contact.</p>"""
    id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact summary.</p>"""
    initial_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>If this contact is related to other contacts, this is the ID of the initial contact.</p>"""
    previous_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>If this contact is not the first contact, this is the ID of the previous contact.</p>"""
    initiation_method: NotRequired[
        "capo_connect.types.contact_initiation_method.ContactInitiationMethod"
    ]
    """<p>Indicates how the contact was initiated.</p>"""
    channel: NotRequired["capo_connect.types.channel.Channel"]
    """<p>How the contact reached your contact center.</p>"""
    queue_info: NotRequired[
        "capo_connect.types.contact_search_summary_queue_info.ContactSearchSummaryQueueInfo"
    ]
    """<p>If this contact was queued, this contains information about the queue.</p>"""
    agent_info: NotRequired[
        "capo_connect.types.contact_search_summary_agent_info.ContactSearchSummaryAgentInfo"
    ]
    """<p>Information about the agent who accepted the contact.</p>"""
    initiation_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The date and time this contact was initiated, in UTC time. For <code>INBOUND</code>, this is when the contact arrived. For <code>OUTBOUND</code>, this is when the agent began dialing. For <code>CALLBACK</code>, this is when the callback contact was created. For <code>TRANSFER</code> and <code>QUEUE_TRANSFER</code>, this is when the transfer was initiated. For API, this is when the request arrived. For <code>EXTERNAL_OUTBOUND</code>, this is when the agent started dialing the external participant. For <code>MONITOR</code>, this is when the supervisor started listening to a contact.</p>"""
    disconnect_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the customer endpoint disconnected from Connect Customer.</p>"""
    scheduled_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp, in Unix epoch time format, at which to start running the inbound flow.</p>"""
    segment_attributes: NotRequired[
        "capo_connect.types.contact_search_summary_segment_attributes.ContactSearchSummarySegmentAttributes"
    ]
    """<p>Set of segment attributes for a contact.</p>"""
    name: NotRequired["capo_connect.types.name.Name"]
    """<p>Indicates name of the contact.</p>"""
    routing_criteria: NotRequired["capo_connect.types.routing_criteria.RoutingCriteria"]
    tags: NotRequired["capo_connect.types.contact_tag_map.ContactTagMap"]
    """<p>Tags associated with the contact. This contains both Amazon Web Services generated and user-defined tags.</p>"""
    global_resiliency_metadata: NotRequired[
        "capo_connect.types.global_resiliency_metadata.GlobalResiliencyMetadata"
    ]
    """<p>Additional routing information for contacts created in ACGR instances.</p>"""
    ai_agent_info: NotRequired[
        "capo_connect.types.contact_search_summary_ai_agent_info_list.ContactSearchSummaryAiAgentInfoList"
    ]
    """<p>Information about the AI agents involved in the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactSearchSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "initial_contact_id" in value:
        out["InitialContactId"] = value["initial_contact_id"]
    if "previous_contact_id" in value:
        out["PreviousContactId"] = value["previous_contact_id"]
    if "initiation_method" in value:
        import capo_connect.types.contact_initiation_method

        out["InitiationMethod"] = (
            capo_connect.types.contact_initiation_method.serialize_json(
                value["initiation_method"]
            )
        )
    if "channel" in value:
        import capo_connect.types.channel

        out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    if "queue_info" in value:
        import capo_connect.types.contact_search_summary_queue_info

        out["QueueInfo"] = (
            capo_connect.types.contact_search_summary_queue_info.serialize_json(
                value["queue_info"]
            )
        )
    if "agent_info" in value:
        import capo_connect.types.contact_search_summary_agent_info

        out["AgentInfo"] = (
            capo_connect.types.contact_search_summary_agent_info.serialize_json(
                value["agent_info"]
            )
        )
    if "initiation_timestamp" in value:
        import capo_connect.types.timestamp

        out["InitiationTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["initiation_timestamp"]
        )
    if "disconnect_timestamp" in value:
        import capo_connect.types.timestamp

        out["DisconnectTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["disconnect_timestamp"]
        )
    if "scheduled_timestamp" in value:
        import capo_connect.types.timestamp

        out["ScheduledTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["scheduled_timestamp"]
        )
    if "segment_attributes" in value:
        import capo_connect.types.contact_search_summary_segment_attributes

        out["SegmentAttributes"] = (
            capo_connect.types.contact_search_summary_segment_attributes.serialize_json(
                value["segment_attributes"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "routing_criteria" in value:
        import capo_connect.types.routing_criteria

        out["RoutingCriteria"] = capo_connect.types.routing_criteria.serialize_json(
            value["routing_criteria"]
        )
    if "tags" in value:
        import capo_connect.types.contact_tag_map

        out["Tags"] = capo_connect.types.contact_tag_map.serialize_json(value["tags"])
    if "global_resiliency_metadata" in value:
        import capo_connect.types.global_resiliency_metadata

        out["GlobalResiliencyMetadata"] = (
            capo_connect.types.global_resiliency_metadata.serialize_json(
                value["global_resiliency_metadata"]
            )
        )
    if "ai_agent_info" in value:
        import capo_connect.types.contact_search_summary_ai_agent_info_list

        out["AiAgentInfo"] = (
            capo_connect.types.contact_search_summary_ai_agent_info_list.serialize_json(
                value["ai_agent_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactSearchSummary:
    out: ContactSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("InitialContactId") is not None:
        out["initial_contact_id"] = data["InitialContactId"]
    if data.get("PreviousContactId") is not None:
        out["previous_contact_id"] = data["PreviousContactId"]
    if data.get("InitiationMethod") is not None:
        import capo_connect.types.contact_initiation_method

        out["initiation_method"] = (
            capo_connect.types.contact_initiation_method.deserialize_json(
                data["InitiationMethod"]
            )
        )
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    if data.get("QueueInfo") is not None:
        import capo_connect.types.contact_search_summary_queue_info

        out["queue_info"] = (
            capo_connect.types.contact_search_summary_queue_info.deserialize_json(
                data["QueueInfo"]
            )
        )
    if data.get("AgentInfo") is not None:
        import capo_connect.types.contact_search_summary_agent_info

        out["agent_info"] = (
            capo_connect.types.contact_search_summary_agent_info.deserialize_json(
                data["AgentInfo"]
            )
        )
    if data.get("InitiationTimestamp") is not None:
        import capo_connect.types.timestamp

        out["initiation_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["InitiationTimestamp"]
        )
    if data.get("DisconnectTimestamp") is not None:
        import capo_connect.types.timestamp

        out["disconnect_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["DisconnectTimestamp"]
        )
    if data.get("ScheduledTimestamp") is not None:
        import capo_connect.types.timestamp

        out["scheduled_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["ScheduledTimestamp"]
        )
    if data.get("SegmentAttributes") is not None:
        import capo_connect.types.contact_search_summary_segment_attributes

        out["segment_attributes"] = (
            capo_connect.types.contact_search_summary_segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RoutingCriteria") is not None:
        import capo_connect.types.routing_criteria

        out["routing_criteria"] = capo_connect.types.routing_criteria.deserialize_json(
            data["RoutingCriteria"]
        )
    if data.get("Tags") is not None:
        import capo_connect.types.contact_tag_map

        out["tags"] = capo_connect.types.contact_tag_map.deserialize_json(data["Tags"])
    if data.get("GlobalResiliencyMetadata") is not None:
        import capo_connect.types.global_resiliency_metadata

        out["global_resiliency_metadata"] = (
            capo_connect.types.global_resiliency_metadata.deserialize_json(
                data["GlobalResiliencyMetadata"]
            )
        )
    if data.get("AiAgentInfo") is not None:
        import capo_connect.types.contact_search_summary_ai_agent_info_list

        out["ai_agent_info"] = (
            capo_connect.types.contact_search_summary_ai_agent_info_list.deserialize_json(
                data["AiAgentInfo"]
            )
        )
    return out


def redact_sensitive(value: ContactSearchSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "segment_attributes" in value:
        out["segment_attributes"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
