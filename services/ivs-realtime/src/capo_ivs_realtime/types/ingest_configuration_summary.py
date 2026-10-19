"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#IngestConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration_arn
    import capo_ivs_realtime.types.ingest_configuration_name
    import capo_ivs_realtime.types.ingest_configuration_stage_arn
    import capo_ivs_realtime.types.ingest_configuration_state
    import capo_ivs_realtime.types.ingest_protocol
    import capo_ivs_realtime.types.participant_id
    import capo_ivs_realtime.types.redundant_ingest
    import capo_ivs_realtime.types.user_id


class IngestConfigurationSummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration_name.IngestConfigurationName"
    ]
    """<p>Ingest name.</p>"""
    arn: "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>Ingest configuration ARN.</p>"""
    ingest_protocol: "capo_ivs_realtime.types.ingest_protocol.IngestProtocol"
    """<p>Type of ingest protocol that the user employs for broadcasting.</p>"""
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


# --- restJson1 ser/de ---
def serialize_json(value: IngestConfigurationSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    import capo_ivs_realtime.types.ingest_protocol

    out["ingestProtocol"] = capo_ivs_realtime.types.ingest_protocol.serialize_json(
        value["ingest_protocol"]
    )
    out["stageArn"] = value["stage_arn"]
    out["participantId"] = value["participant_id"]
    out["state"] = value["state"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    out["redundantIngest"] = value.get("redundant_ingest", False)
    return out


def deserialize_json(data: dict) -> IngestConfigurationSummary:
    out: IngestConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("ingestProtocol") is not None:
        import capo_ivs_realtime.types.ingest_protocol

        out["ingest_protocol"] = (
            capo_ivs_realtime.types.ingest_protocol.deserialize_json(
                data["ingestProtocol"]
            )
        )
    else:
        import typing

        out["ingest_protocol"] = typing.cast(
            "capo_ivs_realtime.types.ingest_protocol.IngestProtocol", ""
        )
    if data.get("stageArn") is not None:
        out["stage_arn"] = data["stageArn"]
    else:
        out["stage_arn"] = ""
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    else:
        out["participant_id"] = ""
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("redundantIngest") is not None:
        out["redundant_ingest"] = data["redundantIngest"]
    else:
        out["redundant_ingest"] = False
    return out
