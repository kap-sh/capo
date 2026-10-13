"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.account_detail

AccountDetails: TypeAlias = list["capo_guardduty.types.account_detail.AccountDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountDetails) -> list:
    import capo_guardduty.types.account_detail

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.account_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountDetails:
    import capo_guardduty.types.account_detail

    out: AccountDetails = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.account_detail.deserialize_json(item))
    return out


def redact_sensitive(value: AccountDetails) -> list[Any]:
    import capo_guardduty.types.account_detail

    return [
        capo_guardduty.types.account_detail.redact_sensitive(item) for item in value
    ]
