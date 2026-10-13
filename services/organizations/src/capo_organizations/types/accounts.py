"""Generated from Smithy shape ``com.amazonaws.organizations#Accounts``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.account

Accounts: TypeAlias = list["capo_organizations.types.account.Account"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Accounts) -> list:
    import capo_organizations.types.account

    out: list = []
    for item in value:
        out.append(capo_organizations.types.account.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Accounts:
    import capo_organizations.types.account

    out: Accounts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_organizations.types.account.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Accounts) -> list[Any]:
    import capo_organizations.types.account

    return [capo_organizations.types.account.redact_sensitive(item) for item in value]
