"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetIngestConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration_arn


class GetIngestConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>ARN of the ingest for which the information is to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIngestConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetIngestConfigurationRequest:
    out: GetIngestConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
