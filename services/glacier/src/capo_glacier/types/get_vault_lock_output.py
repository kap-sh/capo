"""Generated from Smithy shape ``com.amazonaws.glacier#GetVaultLockOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.string


class GetVaultLockOutput(TypedDict, closed=True):
    policy: NotRequired["capo_glacier.types.string.string"]
    r"""<p>The vault lock policy as a JSON string, which uses "\" as an escape character.</p>"""
    state: NotRequired["capo_glacier.types.string.string"]
    """<p>The state of the vault lock. <code>InProgress</code> or <code>Locked</code>.</p>"""
    expiration_date: NotRequired["capo_glacier.types.string.string"]
    """<p>The UTC date and time at which the lock ID expires. This value can be <code>null</code> if the vault lock is in a <code>Locked</code> state.</p>"""
    creation_date: NotRequired["capo_glacier.types.string.string"]
    """<p>The UTC date and time at which the vault lock was put into the <code>InProgress</code> state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVaultLockOutput) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "state" in value:
        out["State"] = value["state"]
    if "expiration_date" in value:
        out["ExpirationDate"] = value["expiration_date"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    return out


def deserialize_json(data: dict) -> GetVaultLockOutput:
    out: GetVaultLockOutput = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("ExpirationDate") is not None:
        out["expiration_date"] = data["ExpirationDate"]
    if data.get("CreationDate") is not None:
        out["creation_date"] = data["CreationDate"]
    return out
