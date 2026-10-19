"""Generated from Smithy shape ``com.amazonaws.inspector2#AccountState``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.resource_state
    import capo_inspector2.types.state


class AccountState(TypedDict, closed=True):
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    state: "capo_inspector2.types.state.State"
    """<p>An object detailing the status of Amazon Inspector for the account.</p>"""
    resource_state: "capo_inspector2.types.resource_state.ResourceState"
    """<p>An object detailing which resources Amazon Inspector is enabled to scan for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountState) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_inspector2.types.state

    out["state"] = capo_inspector2.types.state.serialize_json(value["state"])
    import capo_inspector2.types.resource_state

    out["resourceState"] = capo_inspector2.types.resource_state.serialize_json(
        value["resource_state"]
    )
    return out


def deserialize_json(data: dict) -> AccountState:
    out: AccountState = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("state") is not None:
        import capo_inspector2.types.state

        out["state"] = capo_inspector2.types.state.deserialize_json(data["state"])
    else:
        raise DeserializationError("AccountState.state required")
    if data.get("resourceState") is not None:
        import capo_inspector2.types.resource_state

        out["resource_state"] = capo_inspector2.types.resource_state.deserialize_json(
            data["resourceState"]
        )
    else:
        raise DeserializationError("AccountState.resource_state required")
    return out
