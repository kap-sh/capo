"""Generated from Smithy shape ``com.amazonaws.savingsplans#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_savingsplans.errors import DeserializationError

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_arn
    import capo_savingsplans.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_savingsplans.types.savings_plan_arn.SavingsPlanArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "capo_savingsplans.types.tag_map.TagMap"
    """<p>One or more tags. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_savingsplans.types.tag_map

    out["tags"] = capo_savingsplans.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("tags") is not None:
        import capo_savingsplans.types.tag_map

        out["tags"] = capo_savingsplans.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
