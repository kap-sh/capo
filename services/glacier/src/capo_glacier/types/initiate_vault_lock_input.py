"""Generated from Smithy shape ``com.amazonaws.glacier#InitiateVaultLockInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.string
    import capo_glacier.types.vault_lock_policy


class InitiateVaultLockInput(TypedDict, closed=True):
    account_id: "capo_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "capo_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    policy: NotRequired["capo_glacier.types.vault_lock_policy.VaultLockPolicy"]
    r"""<p>The vault lock policy as a JSON string, which uses "\" as an escape character.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateVaultLockInput) -> dict:
    out: dict = {}
    if "policy" in value:
        import capo_glacier.types.vault_lock_policy

        out["policy"] = capo_glacier.types.vault_lock_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> InitiateVaultLockInput:
    out: InitiateVaultLockInput = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        import capo_glacier.types.vault_lock_policy

        out["policy"] = capo_glacier.types.vault_lock_policy.deserialize_json(
            data["policy"]
        )
    return out
