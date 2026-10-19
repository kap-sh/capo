"""Generated from Smithy shape ``com.amazonaws.mgn#AssociateApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.application_i_ds
    import capo_mgn.types.wave_id


class AssociateApplicationsRequest(TypedDict, closed=True):
    wave_id: "capo_mgn.types.wave_id.WaveID"
    """<p>Wave ID.</p>"""
    application_i_ds: "capo_mgn.types.application_i_ds.ApplicationIDs"
    """<p>Application IDs list.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateApplicationsRequest) -> dict:
    out: dict = {}
    out["waveID"] = value["wave_id"]
    import capo_mgn.types.application_i_ds

    out["applicationIDs"] = capo_mgn.types.application_i_ds.serialize_json(
        value["application_i_ds"]
    )
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> AssociateApplicationsRequest:
    out: AssociateApplicationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("waveID") is not None:
        out["wave_id"] = data["waveID"]
    else:
        out["wave_id"] = ""
    if data.get("applicationIDs") is not None:
        import capo_mgn.types.application_i_ds

        out["application_i_ds"] = capo_mgn.types.application_i_ds.deserialize_json(
            data["applicationIDs"]
        )
    else:
        out["application_i_ds"] = []
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
