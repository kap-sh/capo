"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StopContinuousExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configurations_export_id


class StopContinuousExportRequest(TypedDict, closed=True):
    export_id: "capo_application_discovery_service.types.configurations_export_id.ConfigurationsExportId"
    """<p>The unique ID assigned to this export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopContinuousExportRequest) -> dict:
    out: dict = {}
    out["exportId"] = value["export_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopContinuousExportRequest:
    out: StopContinuousExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("exportId") is not None:
        out["export_id"] = data["exportId"]
    else:
        out["export_id"] = ""
    return out
