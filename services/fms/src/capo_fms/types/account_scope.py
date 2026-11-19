"""Generated from Smithy shape ``com.amazonaws.fms#AccountScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.account_id_list
    import capo_fms.types.boolean


class AccountScope(TypedDict, closed=True):
    accounts: NotRequired["capo_fms.types.account_id_list.AccountIdList"]
    """<p>The list of accounts within the organization that the specified Firewall Manager administrator either can or cannot apply policies to, based on the value of <code>ExcludeSpecifiedAccounts</code>. If <code>ExcludeSpecifiedAccounts</code> is set to <code>true</code>, then the Firewall Manager administrator can apply policies to all members of the organization except for the accounts in this list. If <code>ExcludeSpecifiedAccounts</code> is set to <code>false</code>, then the Firewall Manager administrator can only apply policies to the accounts in this list.</p>"""
    all_accounts_enabled: "capo_fms.types.boolean.Boolean"
    """<p>A boolean value that indicates if the administrator can apply policies to all accounts within an organization. If true, the administrator can apply policies to all accounts within the organization. You can either enable management of all accounts through this operation, or you can specify a list of accounts to manage in <code>AccountScope$Accounts</code>. You cannot specify both.</p>"""
    exclude_specified_accounts: "capo_fms.types.boolean.Boolean"
    """<p>A boolean value that excludes the accounts in <code>AccountScope$Accounts</code> from the administrator's scope. If true, the Firewall Manager administrator can apply policies to all members of the organization except for the accounts listed in <code>AccountScope$Accounts</code>. You can either specify a list of accounts to exclude by <code>AccountScope$Accounts</code>, or you can enable management of all accounts by <code>AccountScope$AllAccountsEnabled</code>. You cannot specify both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountScope) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_fms.types.account_id_list

        out["Accounts"] = capo_fms.types.account_id_list.serialize_aws_json_1_1(
            value["accounts"]
        )
    out["AllAccountsEnabled"] = value.get("all_accounts_enabled", False)
    out["ExcludeSpecifiedAccounts"] = value.get("exclude_specified_accounts", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountScope:
    out: AccountScope = {}  # type: ignore[typeddict-item]
    if data.get("Accounts") is not None:
        import capo_fms.types.account_id_list

        out["accounts"] = capo_fms.types.account_id_list.deserialize_aws_json_1_1(
            data["Accounts"]
        )
    if data.get("AllAccountsEnabled") is not None:
        out["all_accounts_enabled"] = data["AllAccountsEnabled"]
    else:
        out["all_accounts_enabled"] = False
    if data.get("ExcludeSpecifiedAccounts") is not None:
        out["exclude_specified_accounts"] = data["ExcludeSpecifiedAccounts"]
    else:
        out["exclude_specified_accounts"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountScope) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_fms.types.account_id_list

        out["Accounts"] = capo_fms.types.account_id_list.serialize_cbor(
            value["accounts"]
        )
    out["AllAccountsEnabled"] = value.get("all_accounts_enabled", False)
    out["ExcludeSpecifiedAccounts"] = value.get("exclude_specified_accounts", False)
    return out


def deserialize_cbor(data: dict) -> AccountScope:
    out: AccountScope = {}  # type: ignore[typeddict-item]
    if data.get("Accounts") is not None:
        import capo_fms.types.account_id_list

        out["accounts"] = capo_fms.types.account_id_list.deserialize_cbor(
            data["Accounts"]
        )
    if data.get("AllAccountsEnabled") is not None:
        out["all_accounts_enabled"] = data["AllAccountsEnabled"]
    else:
        out["all_accounts_enabled"] = False
    if data.get("ExcludeSpecifiedAccounts") is not None:
        out["exclude_specified_accounts"] = data["ExcludeSpecifiedAccounts"]
    else:
        out["exclude_specified_accounts"] = False
    return out
