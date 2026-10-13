"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedPrincipal``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.subscribed_group
    import capo_datazone.types.subscribed_iam_principal
    import capo_datazone.types.subscribed_project
    import capo_datazone.types.subscribed_user


class _SubscribedPrincipal_project(TypedDict, closed=True):
    project: "capo_datazone.types.subscribed_project.SubscribedProject"


class _SubscribedPrincipal_user(TypedDict, closed=True):
    user: "capo_datazone.types.subscribed_user.SubscribedUser"


class _SubscribedPrincipal_group(TypedDict, closed=True):
    group: "capo_datazone.types.subscribed_group.SubscribedGroup"


class _SubscribedPrincipal_iam(TypedDict, closed=True):
    iam: "capo_datazone.types.subscribed_iam_principal.SubscribedIamPrincipal"


SubscribedPrincipal: TypeAlias = (
    _SubscribedPrincipal_project
    | _SubscribedPrincipal_user
    | _SubscribedPrincipal_group
    | _SubscribedPrincipal_iam
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedPrincipal) -> dict:
    if "project" in value:
        import capo_datazone.types.subscribed_project

        return {
            "project": capo_datazone.types.subscribed_project.serialize_json(
                value["project"]
            )
        }
    elif "user" in value:
        import capo_datazone.types.subscribed_user

        return {
            "user": capo_datazone.types.subscribed_user.serialize_json(value["user"])
        }
    elif "group" in value:
        import capo_datazone.types.subscribed_group

        return {
            "group": capo_datazone.types.subscribed_group.serialize_json(value["group"])
        }
    elif "iam" in value:
        import capo_datazone.types.subscribed_iam_principal

        return {
            "iam": capo_datazone.types.subscribed_iam_principal.serialize_json(
                value["iam"]
            )
        }
    else:
        raise SerializationError("SubscribedPrincipal: no variant present")


def deserialize_json(data: dict) -> SubscribedPrincipal:
    if data.get("project") is not None:
        import capo_datazone.types.subscribed_project

        return {
            "project": capo_datazone.types.subscribed_project.deserialize_json(
                data["project"]
            )
        }
    elif data.get("user") is not None:
        import capo_datazone.types.subscribed_user

        return {
            "user": capo_datazone.types.subscribed_user.deserialize_json(data["user"])
        }
    elif data.get("group") is not None:
        import capo_datazone.types.subscribed_group

        return {
            "group": capo_datazone.types.subscribed_group.deserialize_json(
                data["group"]
            )
        }
    elif data.get("iam") is not None:
        import capo_datazone.types.subscribed_iam_principal

        return {
            "iam": capo_datazone.types.subscribed_iam_principal.deserialize_json(
                data["iam"]
            )
        }
    else:
        raise DeserializationError("SubscribedPrincipal: no recognized variant key")


def redact_sensitive(value: SubscribedPrincipal) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "project" in value:
        import capo_datazone.types.subscribed_project

        out["project"] = capo_datazone.types.subscribed_project.redact_sensitive(
            value["project"]
        )
    if "user" in value:
        import capo_datazone.types.subscribed_user

        out["user"] = capo_datazone.types.subscribed_user.redact_sensitive(
            value["user"]
        )
    if "group" in value:
        import capo_datazone.types.subscribed_group

        out["group"] = capo_datazone.types.subscribed_group.redact_sensitive(
            value["group"]
        )
    return out
