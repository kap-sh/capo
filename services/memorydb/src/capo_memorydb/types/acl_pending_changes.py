"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLPendingChanges``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.user_name_list


class ACLPendingChanges(TypedDict, closed=True):
    user_names_to_remove: NotRequired["capo_memorydb.types.user_name_list.UserNameList"]
    """<p>A list of user names being removed from the ACL</p>"""
    user_names_to_add: NotRequired["capo_memorydb.types.user_name_list.UserNameList"]
    """<p>A list of users being added to the ACL</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLPendingChanges) -> dict:
    out: dict = {}
    if "user_names_to_remove" in value:
        import capo_memorydb.types.user_name_list

        out["UserNamesToRemove"] = (
            capo_memorydb.types.user_name_list.serialize_aws_json_1_1(
                value["user_names_to_remove"]
            )
        )
    if "user_names_to_add" in value:
        import capo_memorydb.types.user_name_list

        out["UserNamesToAdd"] = (
            capo_memorydb.types.user_name_list.serialize_aws_json_1_1(
                value["user_names_to_add"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ACLPendingChanges:
    out: ACLPendingChanges = {}  # type: ignore[typeddict-item]
    if data.get("UserNamesToRemove") is not None:
        import capo_memorydb.types.user_name_list

        out["user_names_to_remove"] = (
            capo_memorydb.types.user_name_list.deserialize_aws_json_1_1(
                data["UserNamesToRemove"]
            )
        )
    if data.get("UserNamesToAdd") is not None:
        import capo_memorydb.types.user_name_list

        out["user_names_to_add"] = (
            capo_memorydb.types.user_name_list.deserialize_aws_json_1_1(
                data["UserNamesToAdd"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ACLPendingChanges) -> dict:
    out: dict = {}
    if "user_names_to_remove" in value:
        import capo_memorydb.types.user_name_list

        out["UserNamesToRemove"] = capo_memorydb.types.user_name_list.serialize_cbor(
            value["user_names_to_remove"]
        )
    if "user_names_to_add" in value:
        import capo_memorydb.types.user_name_list

        out["UserNamesToAdd"] = capo_memorydb.types.user_name_list.serialize_cbor(
            value["user_names_to_add"]
        )
    return out


def deserialize_cbor(data: dict) -> ACLPendingChanges:
    out: ACLPendingChanges = {}  # type: ignore[typeddict-item]
    if data.get("UserNamesToRemove") is not None:
        import capo_memorydb.types.user_name_list

        out["user_names_to_remove"] = (
            capo_memorydb.types.user_name_list.deserialize_cbor(
                data["UserNamesToRemove"]
            )
        )
    if data.get("UserNamesToAdd") is not None:
        import capo_memorydb.types.user_name_list

        out["user_names_to_add"] = capo_memorydb.types.user_name_list.deserialize_cbor(
            data["UserNamesToAdd"]
        )
    return out
