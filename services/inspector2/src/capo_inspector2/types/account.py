"""Generated from Smithy shape ``com.amazonaws.inspector2#Account``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.resource_status
    import capo_inspector2.types.status


class Account(TypedDict, closed=True):
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account.</p>"""
    status: "capo_inspector2.types.status.Status"
    """<p>The status of Amazon Inspector for the account.</p>"""
    resource_status: "capo_inspector2.types.resource_status.ResourceStatus"
    """<p>Details of the status of Amazon Inspector scans by resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Account) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["status"] = value["status"]
    import capo_inspector2.types.resource_status

    out["resourceStatus"] = capo_inspector2.types.resource_status.serialize_json(
        value["resource_status"]
    )
    return out


def deserialize_json(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("resourceStatus") is not None:
        import capo_inspector2.types.resource_status

        out["resource_status"] = capo_inspector2.types.resource_status.deserialize_json(
            data["resourceStatus"]
        )
    else:
        raise DeserializationError("Account.resource_status required")
    return out
