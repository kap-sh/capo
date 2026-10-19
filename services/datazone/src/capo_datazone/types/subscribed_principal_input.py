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


class _SubscribedPrincipalInput_project(TypedDict, closed=True):
    project: "capo_datazone.types.subscribed_project_input.SubscribedProjectInput"


class _SubscribedPrincipalInput_user(TypedDict, closed=True):
    user: "capo_datazone.types.subscribed_user_input.SubscribedUserInput"


class _SubscribedPrincipalInput_group(TypedDict, closed=True):
    group: "capo_datazone.types.subscribed_group_input.SubscribedGroupInput"


class _SubscribedPrincipalInput_iam(TypedDict, closed=True):
    iam: (
        "capo_datazone.types.subscribed_iam_principal_input.SubscribedIamPrincipalInput"
    )


SubscribedPrincipalInput: TypeAlias = (
    _SubscribedPrincipalInput_project
    | _SubscribedPrincipalInput_user
    | _SubscribedPrincipalInput_group
    | _SubscribedPrincipalInput_iam
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedPrincipalInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SubscribedPrincipalInput: cannot serialize unknown variant {value.name!r}"
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
            return UnknownUnionMember(name)
        raise DeserializationError(
            "SubscribedPrincipalInput: no recognized variant key"
        )
