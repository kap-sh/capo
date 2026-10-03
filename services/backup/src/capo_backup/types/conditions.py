"""Generated from Smithy shape ``com.amazonaws.backup#Conditions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.condition_parameters


class Conditions(TypedDict, closed=True):
    string_equals: NotRequired[
        "capo_backup.types.condition_parameters.ConditionParameters"
    ]
    """<p>Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called "exact matching."</p>"""
    string_not_equals: NotRequired[
        "capo_backup.types.condition_parameters.ConditionParameters"
    ]
    """<p>Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called "negated matching."</p>"""
    string_like: NotRequired[
        "capo_backup.types.condition_parameters.ConditionParameters"
    ]
    """<p>Filters the values of your tagged resources for matching tag values with the use of a wildcard character (*) anywhere in the string. For example, "prod*" or "*rod*" matches the tag value "production".</p>"""
    string_not_like: NotRequired[
        "capo_backup.types.condition_parameters.ConditionParameters"
    ]
    """<p>Filters the values of your tagged resources for non-matching tag values with the use of a wildcard character (*) anywhere in the string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Conditions) -> dict:
    out: dict = {}
    if "string_equals" in value:
        import capo_backup.types.condition_parameters

        out["StringEquals"] = capo_backup.types.condition_parameters.serialize_json(
            value["string_equals"]
        )
    if "string_not_equals" in value:
        import capo_backup.types.condition_parameters

        out["StringNotEquals"] = capo_backup.types.condition_parameters.serialize_json(
            value["string_not_equals"]
        )
    if "string_like" in value:
        import capo_backup.types.condition_parameters

        out["StringLike"] = capo_backup.types.condition_parameters.serialize_json(
            value["string_like"]
        )
    if "string_not_like" in value:
        import capo_backup.types.condition_parameters

        out["StringNotLike"] = capo_backup.types.condition_parameters.serialize_json(
            value["string_not_like"]
        )
    return out


def deserialize_json(data: dict) -> Conditions:
    out: Conditions = {}  # type: ignore[typeddict-item]
    if data.get("StringEquals") is not None:
        import capo_backup.types.condition_parameters

        out["string_equals"] = capo_backup.types.condition_parameters.deserialize_json(
            data["StringEquals"]
        )
    if data.get("StringNotEquals") is not None:
        import capo_backup.types.condition_parameters

        out["string_not_equals"] = (
            capo_backup.types.condition_parameters.deserialize_json(
                data["StringNotEquals"]
            )
        )
    if data.get("StringLike") is not None:
        import capo_backup.types.condition_parameters

        out["string_like"] = capo_backup.types.condition_parameters.deserialize_json(
            data["StringLike"]
        )
    if data.get("StringNotLike") is not None:
        import capo_backup.types.condition_parameters

        out["string_not_like"] = (
            capo_backup.types.condition_parameters.deserialize_json(
                data["StringNotLike"]
            )
        )
    return out
