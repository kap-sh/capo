"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#UpdateIngestConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration_arn
    import capo_ivs_realtime.types.ingest_configuration_stage_arn
    import capo_ivs_realtime.types.redundant_ingest


class UpdateIngestConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>ARN of the IngestConfiguration, for which the related stage ARN needs to be updated.</p>"""
    stage_arn: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration_stage_arn.IngestConfigurationStageArn"
    ]
    """<p>Stage ARN that needs to be updated.</p>"""
    redundant_ingest: NotRequired[
        "capo_ivs_realtime.types.redundant_ingest.RedundantIngest"
    ]
    """<p>Indicates whether redundant ingest is enabled for the ingest configuration. Default: <code>false</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIngestConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "stage_arn" in value:
        out["stageArn"] = value["stage_arn"]
    if "redundant_ingest" in value:
        out["redundantIngest"] = value["redundant_ingest"]
    return out


def deserialize_json(data: dict) -> UpdateIngestConfigurationRequest:
    out: UpdateIngestConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("stageArn") is not None:
        out["stage_arn"] = data["stageArn"]
    if data.get("redundantIngest") is not None:
        out["redundant_ingest"] = data["redundantIngest"]
    return out
