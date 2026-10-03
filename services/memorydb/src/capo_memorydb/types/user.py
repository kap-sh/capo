"""Generated from Smithy shape ``com.amazonaws.memorydb#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.acl_name_list
    import capo_memorydb.types.authentication
    import capo_memorydb.types.string


class User(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the user</p>"""
    status: NotRequired["capo_memorydb.types.string.String"]
    """<p>Indicates the user status. Can be "active", "modifying" or "deleting".</p>"""
    access_string: NotRequired["capo_memorydb.types.string.String"]
    """<p>Access permissions string used for this user.</p>"""
    acl_names: NotRequired["capo_memorydb.types.acl_name_list.ACLNameList"]
    """<p>The names of the Access Control Lists to which the user belongs</p>"""
    minimum_engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The minimum engine version supported for the user</p>"""
    authentication: NotRequired["capo_memorydb.types.authentication.Authentication"]
    """<p>Denotes whether the user requires a password to authenticate.</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the user. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: User) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "access_string" in value:
        out["AccessString"] = value["access_string"]
    if "acl_names" in value:
        import capo_memorydb.types.acl_name_list

        out["ACLNames"] = capo_memorydb.types.acl_name_list.serialize_aws_json_1_1(
            value["acl_names"]
        )
    if "minimum_engine_version" in value:
        out["MinimumEngineVersion"] = value["minimum_engine_version"]
    if "authentication" in value:
        import capo_memorydb.types.authentication

        out["Authentication"] = (
            capo_memorydb.types.authentication.serialize_aws_json_1_1(
                value["authentication"]
            )
        )
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("AccessString") is not None:
        out["access_string"] = data["AccessString"]
    if data.get("ACLNames") is not None:
        import capo_memorydb.types.acl_name_list

        out["acl_names"] = capo_memorydb.types.acl_name_list.deserialize_aws_json_1_1(
            data["ACLNames"]
        )
    if data.get("MinimumEngineVersion") is not None:
        out["minimum_engine_version"] = data["MinimumEngineVersion"]
    if data.get("Authentication") is not None:
        import capo_memorydb.types.authentication

        out["authentication"] = (
            capo_memorydb.types.authentication.deserialize_aws_json_1_1(
                data["Authentication"]
            )
        )
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    return out
