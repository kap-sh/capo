"""Generated from Smithy shape ``com.amazonaws.organizations#ResponsibilityTransfers``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.responsibility_transfer

ResponsibilityTransfers: TypeAlias = list[
    "capo_organizations.types.responsibility_transfer.ResponsibilityTransfer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponsibilityTransfers) -> list:
    import capo_organizations.types.responsibility_transfer

    out: list = []
    for item in value:
        out.append(
            capo_organizations.types.responsibility_transfer.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResponsibilityTransfers:
    import capo_organizations.types.responsibility_transfer

    out: ResponsibilityTransfers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_organizations.types.responsibility_transfer.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: ResponsibilityTransfers) -> list[Any]:
    import capo_organizations.types.responsibility_transfer

    return [
        capo_organizations.types.responsibility_transfer.redact_sensitive(item)
        for item in value
    ]
