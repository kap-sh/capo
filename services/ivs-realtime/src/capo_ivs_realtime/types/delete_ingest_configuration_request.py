"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DeleteIngestConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.boolean
    import capo_ivs_realtime.types.ingest_configuration_arn


class DeleteIngestConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>ARN of the IngestConfiguration.</p>"""
    force: NotRequired["capo_ivs_realtime.types.boolean.Boolean"]
    """<p>Optional field to force deletion of the IngestConfiguration. If this is set to <code>true</code> when a participant is actively publishing, the participant is disconnected from the stage, followed by deletion of the IngestConfiguration. Default: <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIngestConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_json(data: dict) -> DeleteIngestConfigurationRequest:
    out: DeleteIngestConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("force") is not None:
        out["force"] = data["force"]
    return out
