"""Generated from Smithy shape ``com.amazonaws.mpa#MfaMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.mfa_sync_status
    import capo_mpa.types.mfa_type


class MfaMethod(TypedDict, closed=True):
    type: "capo_mpa.types.mfa_type.MfaType"
    """<p>The type of MFA configuration used by the approver</p>"""
    sync_status: "capo_mpa.types.mfa_sync_status.MfaSyncStatus"
    """<p>Indicates if the approver's MFA device is in-sync with the Identity Source</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MfaMethod) -> dict:
    out: dict = {}
    import capo_mpa.types.mfa_type

    out["Type"] = capo_mpa.types.mfa_type.serialize_json(value["type"])
    import capo_mpa.types.mfa_sync_status

    out["SyncStatus"] = capo_mpa.types.mfa_sync_status.serialize_json(
        value["sync_status"]
    )
    return out


def deserialize_json(data: dict) -> MfaMethod:
    out: MfaMethod = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_mpa.types.mfa_type

        out["type"] = capo_mpa.types.mfa_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_mpa.types.mfa_type.MfaType", "")
    if data.get("SyncStatus") is not None:
        import capo_mpa.types.mfa_sync_status

        out["sync_status"] = capo_mpa.types.mfa_sync_status.deserialize_json(
            data["SyncStatus"]
        )
    else:
        import typing

        out["sync_status"] = typing.cast(
            "capo_mpa.types.mfa_sync_status.MfaSyncStatus", ""
        )
    return out
