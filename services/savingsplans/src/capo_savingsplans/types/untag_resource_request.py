"""Generated from Smithy shape ``com.amazonaws.savingsplans#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_arn
    import capo_savingsplans.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_savingsplans.types.savings_plan_arn.SavingsPlanArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "capo_savingsplans.types.tag_key_list.TagKeyList"
    """<p>The tag keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_savingsplans.types.tag_key_list

    out["tagKeys"] = capo_savingsplans.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_savingsplans.types.tag_key_list

        out["tag_keys"] = capo_savingsplans.types.tag_key_list.deserialize_json(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
