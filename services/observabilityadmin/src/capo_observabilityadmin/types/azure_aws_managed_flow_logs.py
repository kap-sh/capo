"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureAwsManagedFlowLogs``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_flow_log_retention_days


class AzureAwsManagedFlowLogs(TypedDict, closed=True):
    retention_days: "capo_observabilityadmin.types.azure_flow_log_retention_days.AzureFlowLogRetentionDays"
    """<p>The number of days that the created Storage Accounts keep Flow Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureAwsManagedFlowLogs) -> dict:
    out: dict = {}
    out["RetentionDays"] = value["retention_days"]
    return out


def deserialize_json(data: dict) -> AzureAwsManagedFlowLogs:
    out: AzureAwsManagedFlowLogs = {}  # type: ignore[typeddict-item]
    if data.get("RetentionDays") is not None:
        out["retention_days"] = data["RetentionDays"]
    else:
        out["retention_days"] = 0
    return out
