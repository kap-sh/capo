"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#MetricsBackupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.region


class MetricsBackupConfiguration(TypedDict, closed=True):
    region: "capo_observabilityadmin.types.region.Region"
    """<p>Metrics specific backup destination region within the primary destination account to which metrics data should be centralized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsBackupConfiguration) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> MetricsBackupConfiguration:
    out: MetricsBackupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    return out
