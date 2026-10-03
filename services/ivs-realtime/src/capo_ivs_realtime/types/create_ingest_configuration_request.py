"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CreateIngestConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration_name
    import capo_ivs_realtime.types.ingest_configuration_stage_arn
    import capo_ivs_realtime.types.ingest_protocol
    import capo_ivs_realtime.types.insecure_ingest
    import capo_ivs_realtime.types.participant_attributes
    import capo_ivs_realtime.types.redundant_ingest
    import capo_ivs_realtime.types.tags
    import capo_ivs_realtime.types.user_id


class CreateIngestConfigurationRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration_name.IngestConfigurationName"
    ]
    """<p>Optional name that can be specified for the IngestConfiguration being created.</p>"""
    stage_arn: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration_stage_arn.IngestConfigurationStageArn"
    ]
    """<p>ARN of the stage with which the IngestConfiguration is associated.</p>"""
    user_id: NotRequired["capo_ivs_realtime.types.user_id.UserId"]
    """<p>Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    attributes: NotRequired[
        "capo_ivs_realtime.types.participant_attributes.ParticipantAttributes"
    ]
    """<p>Application-provided attributes to store in the IngestConfiguration and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    ingest_protocol: "capo_ivs_realtime.types.ingest_protocol.IngestProtocol"
    """<p>Type of ingest protocol that the user employs to broadcast. If this is set to <code>RTMP</code>, <code>insecureIngest</code> must be set to <code>true</code>.</p>"""
    insecure_ingest: "capo_ivs_realtime.types.insecure_ingest.InsecureIngest"
    """<p>Whether the stage allows insecure RTMP ingest. This must be set to <code>true</code>, if <code>ingestProtocol</code> is set to <code>RTMP</code>. Default: <code>false</code>. </p>"""
    redundant_ingest: "capo_ivs_realtime.types.redundant_ingest.RedundantIngest"
    """<p>Indicates whether redundant ingest is enabled for the ingest configuration. Default: <code>false</code>. </p>"""
    tags: NotRequired["capo_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIngestConfigurationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "stage_arn" in value:
        out["stageArn"] = value["stage_arn"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "attributes" in value:
        import capo_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_attributes.serialize_json(
                value["attributes"]
            )
        )
    import capo_ivs_realtime.types.ingest_protocol

    out["ingestProtocol"] = capo_ivs_realtime.types.ingest_protocol.serialize_json(
        value["ingest_protocol"]
    )
    out["insecureIngest"] = value.get("insecure_ingest", False)
    out["redundantIngest"] = value.get("redundant_ingest", False)
    if "tags" in value:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIngestConfigurationRequest:
    out: CreateIngestConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("stageArn") is not None:
        out["stage_arn"] = data["stageArn"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("attributes") is not None:
        import capo_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if data.get("ingestProtocol") is not None:
        import capo_ivs_realtime.types.ingest_protocol

        out["ingest_protocol"] = (
            capo_ivs_realtime.types.ingest_protocol.deserialize_json(
                data["ingestProtocol"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIngestConfigurationRequest.ingest_protocol required"
        )
    if data.get("insecureIngest") is not None:
        out["insecure_ingest"] = data["insecureIngest"]
    else:
        out["insecure_ingest"] = False
    if data.get("redundantIngest") is not None:
        out["redundant_ingest"] = data["redundantIngest"]
    else:
        out["redundant_ingest"] = False
    if data.get("tags") is not None:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
