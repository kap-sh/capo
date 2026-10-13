"""Generated from Smithy shape ``com.amazonaws.appstream#UserStackAssociationErrorList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.user_stack_association_error

UserStackAssociationErrorList: TypeAlias = list[
    "capo_appstream.types.user_stack_association_error.UserStackAssociationError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStackAssociationErrorList) -> list:
    import capo_appstream.types.user_stack_association_error

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.user_stack_association_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserStackAssociationErrorList:
    import capo_appstream.types.user_stack_association_error

    out: UserStackAssociationErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.user_stack_association_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: UserStackAssociationErrorList) -> list[Any]:
    import capo_appstream.types.user_stack_association_error

    return [
        capo_appstream.types.user_stack_association_error.redact_sensitive(item)
        for item in value
    ]
