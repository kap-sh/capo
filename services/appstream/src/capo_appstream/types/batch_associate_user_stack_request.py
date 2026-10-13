"""Generated from Smithy shape ``com.amazonaws.appstream#BatchAssociateUserStackRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.user_stack_association_list


class BatchAssociateUserStackRequest(TypedDict, closed=True):
    user_stack_associations: NotRequired[
        "capo_appstream.types.user_stack_association_list.UserStackAssociationList"
    ]
    """<p>The list of UserStackAssociation objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAssociateUserStackRequest) -> dict:
    out: dict = {}
    if "user_stack_associations" in value:
        import capo_appstream.types.user_stack_association_list

        out["UserStackAssociations"] = (
            capo_appstream.types.user_stack_association_list.serialize_aws_json_1_1(
                value["user_stack_associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchAssociateUserStackRequest:
    out: BatchAssociateUserStackRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserStackAssociations") is not None:
        import capo_appstream.types.user_stack_association_list

        out["user_stack_associations"] = (
            capo_appstream.types.user_stack_association_list.deserialize_aws_json_1_1(
                data["UserStackAssociations"]
            )
        )
    return out


def redact_sensitive(value: BatchAssociateUserStackRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_stack_associations" in value:
        import capo_appstream.types.user_stack_association_list

        out["user_stack_associations"] = (
            capo_appstream.types.user_stack_association_list.redact_sensitive(
                value["user_stack_associations"]
            )
        )
    return out
