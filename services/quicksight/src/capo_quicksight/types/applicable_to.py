"""Generated from Smithy shape ``com.amazonaws.quicksight#ApplicableTo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.applicable_to_type
    import capo_quicksight.types.group_arn_list


class ApplicableTo(TypedDict, closed=True):
    type: "capo_quicksight.types.applicable_to_type.ApplicableToType"
    """<p>The type of scoping that determines which principals the approval policy applies to. Valid values are defined as follows:</p> <ul> <li> <p> <code>GROUP</code>: The policy applies only to principals in the groups specified by <code>GroupArns</code>. When you use <code>GROUP</code>, you must also provide a value for <code>GroupArns</code>.</p> </li> </ul>"""
    group_arns: NotRequired["capo_quicksight.types.group_arn_list.GroupArnList"]
    """<p>The list of group ARNs that the policy applies to. Required when type is GROUP.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicableTo) -> dict:
    out: dict = {}
    import capo_quicksight.types.applicable_to_type

    out["Type"] = capo_quicksight.types.applicable_to_type.serialize_json(value["type"])
    if "group_arns" in value:
        import capo_quicksight.types.group_arn_list

        out["GroupArns"] = capo_quicksight.types.group_arn_list.serialize_json(
            value["group_arns"]
        )
    return out


def deserialize_json(data: dict) -> ApplicableTo:
    out: ApplicableTo = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_quicksight.types.applicable_to_type

        out["type"] = capo_quicksight.types.applicable_to_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_quicksight.types.applicable_to_type.ApplicableToType", ""
        )
    if data.get("GroupArns") is not None:
        import capo_quicksight.types.group_arn_list

        out["group_arns"] = capo_quicksight.types.group_arn_list.deserialize_json(
            data["GroupArns"]
        )
    return out
