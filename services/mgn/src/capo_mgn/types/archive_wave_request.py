"""Generated from Smithy shape ``com.amazonaws.mgn#ArchiveWaveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.wave_id


class ArchiveWaveRequest(TypedDict, closed=True):
    wave_id: "capo_mgn.types.wave_id.WaveID"
    """<p>Wave ID.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveWaveRequest) -> dict:
    out: dict = {}
    out["waveID"] = value["wave_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ArchiveWaveRequest:
    out: ArchiveWaveRequest = {}  # type: ignore[typeddict-item]
    if data.get("waveID") is not None:
        out["wave_id"] = data["waveID"]
    else:
        out["wave_id"] = ""
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
