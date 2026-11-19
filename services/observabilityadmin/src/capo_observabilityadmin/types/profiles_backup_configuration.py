"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ProfilesBackupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.region


class ProfilesBackupConfiguration(TypedDict, closed=True):
    region: "capo_observabilityadmin.types.region.Region"
    """<p>The backup Region for profiles, within the primary destination account, to which the service centralizes profiles data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfilesBackupConfiguration) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> ProfilesBackupConfiguration:
    out: ProfilesBackupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    return out
