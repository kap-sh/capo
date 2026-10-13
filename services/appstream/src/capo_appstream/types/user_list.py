"""Generated from Smithy shape ``com.amazonaws.appstream#UserList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.user

UserList: TypeAlias = list["capo_appstream.types.user.User"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserList) -> list:
    import capo_appstream.types.user

    out: list = []
    for item in value:
        out.append(capo_appstream.types.user.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UserList:
    import capo_appstream.types.user

    out: UserList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.user.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: UserList) -> list[Any]:
    import capo_appstream.types.user

    return [capo_appstream.types.user.redact_sensitive(item) for item in value]
