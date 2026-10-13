"""Generated from Smithy shape ``com.amazonaws.appstream#UserStackAssociationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.user_stack_association

UserStackAssociationList: TypeAlias = list[
    "capo_appstream.types.user_stack_association.UserStackAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStackAssociationList) -> list:
    import capo_appstream.types.user_stack_association

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.user_stack_association.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserStackAssociationList:
    import capo_appstream.types.user_stack_association

    out: UserStackAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.user_stack_association.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: UserStackAssociationList) -> list[Any]:
    import capo_appstream.types.user_stack_association

    return [
        capo_appstream.types.user_stack_association.redact_sensitive(item)
        for item in value
    ]
