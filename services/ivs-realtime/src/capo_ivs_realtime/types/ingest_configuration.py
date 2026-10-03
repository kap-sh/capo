"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#IngestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration_arn
    import capo_ivs_realtime.types.ingest_configuration_name
    import capo_ivs_realtime.types.ingest_configuration_stage_arn
    import capo_ivs_realtime.types.ingest_configuration_state
    import capo_ivs_realtime.types.ingest_protocol
    import capo_ivs_realtime.types.participant_attributes
    import capo_ivs_realtime.types.participant_id
    import capo_ivs_realtime.types.redundant_ingest
    import capo_ivs_realtime.types.redundant_ingest_credentials
    import capo_ivs_realtime.types.stream_key
    import capo_ivs_realtime.types.tags
    import capo_ivs_realtime.types.user_id


class IngestConfiguration(TypedDict, closed=True):
    name: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration_name.IngestConfigurationName"
    ]
    """<p>Ingest name</p>"""
    arn: "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>Ingest configuration ARN.</p>"""
    ingest_protocol: "capo_ivs_realtime.types.ingest_protocol.IngestProtocol"
    """<p>Type of ingest protocol that the user employs for broadcasting.</p>"""
    stream_key: "capo_ivs_realtime.types.stream_key.StreamKey"
    """<p>Ingest-key value for the RTMP(S) protocol.</p>"""
    stage_arn: "capo_ivs_realtime.types.ingest_configuration_stage_arn.IngestConfigurationStageArn"
    """<p>ARN of the stage with which the IngestConfiguration is associated.</p>"""
    participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId"
    """<p>ID of the participant within the stage.</p>"""
    state: "capo_ivs_realtime.types.ingest_configuration_state.IngestConfigurationState"
    """<p>State of the ingest configuration. It is <code>ACTIVE</code> if a publisher currently is publishing to the stage associated with the ingest configuration.</p>"""
    user_id: NotRequired["capo_ivs_realtime.types.user_id.UserId"]
    """<p>Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    redundant_ingest: "capo_ivs_realtime.types.redundant_ingest.RedundantIngest"
    """<p>Indicates whether redundant ingest is enabled for the ingest configuration.</p>"""
    redundant_ingest_credentials: NotRequired[
        "capo_ivs_realtime.types.redundant_ingest_credentials.RedundantIngestCredentials"
    ]
    """<p>A list of redundant ingest credentials, present only when <code>redundantIngest</code> is set to <code>true</code>. See <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html#redundant-ingest">Redundant Ingest</a> in <i>IVS RTMP Publishing</i> for details.</p>"""
    attributes: NotRequired[
        "capo_ivs_realtime.types.participant_attributes.ParticipantAttributes"
    ]
    """<p>Application-provided attributes to to store in the IngestConfiguration and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    tags: NotRequired["capo_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    import capo_ivs_realtime.types.ingest_protocol

    out["ingestProtocol"] = capo_ivs_realtime.types.ingest_protocol.serialize_json(
        value["ingest_protocol"]
    )
    out["streamKey"] = value["stream_key"]
    out["stageArn"] = value["stage_arn"]
    out["participantId"] = value["participant_id"]
    out["state"] = value["state"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    out["redundantIngest"] = value.get("redundant_ingest", False)
    if "redundant_ingest_credentials" in value:
        import capo_ivs_realtime.types.redundant_ingest_credentials

        out["redundantIngestCredentials"] = (
            capo_ivs_realtime.types.redundant_ingest_credentials.serialize_json(
                value["redundant_ingest_credentials"]
            )
        )
    if "attributes" in value:
        import capo_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "tags" in value:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> IngestConfiguration:
    out: IngestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IngestConfiguration.arn required")
    if data.get("ingestProtocol") is not None:
        import capo_ivs_realtime.types.ingest_protocol

        out["ingest_protocol"] = (
            capo_ivs_realtime.types.ingest_protocol.deserialize_json(
                data["ingestProtocol"]
            )
        )
    else:
        raise DeserializationError("IngestConfiguration.ingest_protocol required")
    if data.get("streamKey") is not None:
        out["stream_key"] = data["streamKey"]
    else:
        raise DeserializationError("IngestConfiguration.stream_key required")
    if data.get("stageArn") is not None:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("IngestConfiguration.stage_arn required")
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError("IngestConfiguration.participant_id required")
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        raise DeserializationError("IngestConfiguration.state required")
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("redundantIngest") is not None:
        out["redundant_ingest"] = data["redundantIngest"]
    else:
        out["redundant_ingest"] = False
    if data.get("redundantIngestCredentials") is not None:
        import capo_ivs_realtime.types.redundant_ingest_credentials

        out["redundant_ingest_credentials"] = (
            capo_ivs_realtime.types.redundant_ingest_credentials.deserialize_json(
                data["redundantIngestCredentials"]
            )
        )
    if data.get("attributes") is not None:
        import capo_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if data.get("tags") is not None:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
