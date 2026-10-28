"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedPrincipalInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.subscribed_group_input
    import capo_datazone.types.subscribed_iam_principal_input
    import capo_datazone.types.subscribed_project_input
    import capo_datazone.types.subscribed_user_input


class SubscribedPrincipalInputProjectMember(TypedDict, closed=True):
    project: "capo_datazone.types.subscribed_project_input.SubscribedProjectInput"


class SubscribedPrincipalInputUserMember(TypedDict, closed=True):
    user: "capo_datazone.types.subscribed_user_input.SubscribedUserInput"


class SubscribedPrincipalInputGroupMember(TypedDict, closed=True):
    group: "capo_datazone.types.subscribed_group_input.SubscribedGroupInput"


class SubscribedPrincipalInputIamMember(TypedDict, closed=True):
    iam: (
        "capo_datazone.types.subscribed_iam_principal_input.SubscribedIamPrincipalInput"
    )


SubscribedPrincipalInput: TypeAlias = (
    SubscribedPrincipalInputProjectMember
    | SubscribedPrincipalInputUserMember
    | SubscribedPrincipalInputGroupMember
    | SubscribedPrincipalInputIamMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedPrincipalInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SubscribedPrincipalInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "project" in value:
        import capo_datazone.types.subscribed_project_input

        return {
            "project": capo_datazone.types.subscribed_project_input.serialize_json(
                value["project"]
            )
        }
    elif "user" in value:
        import capo_datazone.types.subscribed_user_input

        return {
            "user": capo_datazone.types.subscribed_user_input.serialize_json(
                value["user"]
            )
        }
    elif "group" in value:
        import capo_datazone.types.subscribed_group_input

        return {
            "group": capo_datazone.types.subscribed_group_input.serialize_json(
                value["group"]
            )
        }
    elif "iam" in value:
        import capo_datazone.types.subscribed_iam_principal_input

        return {
            "iam": capo_datazone.types.subscribed_iam_principal_input.serialize_json(
                value["iam"]
            )
        }
    else:
        raise SerializationError("SubscribedPrincipalInput: no variant present")


def deserialize_json(data: dict) -> SubscribedPrincipalInput:
    if data.get("project") is not None:
        import capo_datazone.types.subscribed_project_input

        return {
            "project": capo_datazone.types.subscribed_project_input.deserialize_json(
                data["project"]
            )
        }
    elif data.get("user") is not None:
        import capo_datazone.types.subscribed_user_input

        return {
            "user": capo_datazone.types.subscribed_user_input.deserialize_json(
                data["user"]
            )
        }
    elif data.get("group") is not None:
        import capo_datazone.types.subscribed_group_input

        return {
            "group": capo_datazone.types.subscribed_group_input.deserialize_json(
                data["group"]
            )
        }
    elif data.get("iam") is not None:
        import capo_datazone.types.subscribed_iam_principal_input

        return {
            "iam": capo_datazone.types.subscribed_iam_principal_input.deserialize_json(
                data["iam"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "SubscribedPrincipalInput: no recognized variant key"
        )
