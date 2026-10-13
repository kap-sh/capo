"""Generated from Smithy shape ``com.amazonaws.organizations#DelegatedAdministrators``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.delegated_administrator

DelegatedAdministrators: TypeAlias = list[
    "capo_organizations.types.delegated_administrator.DelegatedAdministrator"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DelegatedAdministrators) -> list:
    import capo_organizations.types.delegated_administrator

    out: list = []
    for item in value:
        out.append(
            capo_organizations.types.delegated_administrator.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DelegatedAdministrators:
    import capo_organizations.types.delegated_administrator

    out: DelegatedAdministrators = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_organizations.types.delegated_administrator.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: DelegatedAdministrators) -> list[Any]:
    import capo_organizations.types.delegated_administrator

    return [
        capo_organizations.types.delegated_administrator.redact_sensitive(item)
        for item in value
    ]
