"""Generated from Smithy shape ``com.amazonaws.backup#ProtectedResourceConditions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.key_value_list


class ProtectedResourceConditions(TypedDict, closed=True):
    string_equals: NotRequired["capo_backup.types.key_value_list.KeyValueList"]
    """<p>Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called "exact matching."</p>"""
    string_not_equals: NotRequired["capo_backup.types.key_value_list.KeyValueList"]
    """<p>Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called "negated matching."</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedResourceConditions) -> dict:
    out: dict = {}
    if "string_equals" in value:
        import capo_backup.types.key_value_list

        out["StringEquals"] = capo_backup.types.key_value_list.serialize_json(
            value["string_equals"]
        )
    if "string_not_equals" in value:
        import capo_backup.types.key_value_list

        out["StringNotEquals"] = capo_backup.types.key_value_list.serialize_json(
            value["string_not_equals"]
        )
    return out


def deserialize_json(data: dict) -> ProtectedResourceConditions:
    out: ProtectedResourceConditions = {}  # type: ignore[typeddict-item]
    if data.get("StringEquals") is not None:
        import capo_backup.types.key_value_list

        out["string_equals"] = capo_backup.types.key_value_list.deserialize_json(
            data["StringEquals"]
        )
    if data.get("StringNotEquals") is not None:
        import capo_backup.types.key_value_list

        out["string_not_equals"] = capo_backup.types.key_value_list.deserialize_json(
            data["StringNotEquals"]
        )
    return out
