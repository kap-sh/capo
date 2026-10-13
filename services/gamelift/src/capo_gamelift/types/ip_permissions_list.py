"""Generated from Smithy shape ``com.amazonaws.gamelift#IpPermissionsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.ip_permission

IpPermissionsList: TypeAlias = list["capo_gamelift.types.ip_permission.IpPermission"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpPermissionsList) -> list:
    import capo_gamelift.types.ip_permission

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.ip_permission.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IpPermissionsList:
    import capo_gamelift.types.ip_permission

    out: IpPermissionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.ip_permission.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: IpPermissionsList) -> list[Any]:
    import capo_gamelift.types.ip_permission

    return [capo_gamelift.types.ip_permission.redact_sensitive(item) for item in value]
