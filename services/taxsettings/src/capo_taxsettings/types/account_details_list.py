"""Generated from Smithy shape ``com.amazonaws.taxsettings#AccountDetailsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_taxsettings.types.account_details

AccountDetailsList: TypeAlias = list[
    "capo_taxsettings.types.account_details.AccountDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountDetailsList) -> list:
    import capo_taxsettings.types.account_details

    out: list = []
    for item in value:
        out.append(capo_taxsettings.types.account_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountDetailsList:
    import capo_taxsettings.types.account_details

    out: AccountDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_taxsettings.types.account_details.deserialize_json(item))
    return out


def redact_sensitive(value: AccountDetailsList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
