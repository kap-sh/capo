"""Generated from Smithy shape ``com.amazonaws.ssm#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.resource_id
    import capo_ssm.types.resource_type_for_tagging


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_type: "capo_ssm.types.resource_type_for_tagging.ResourceTypeForTagging"
    """<p>Returns a list of tags for a specific resource type.</p>"""
    resource_id: "capo_ssm.types.resource_id.ResourceId"
    """<p>The resource ID for which you want to see a list of tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.resource_type_for_tagging

    out["ResourceType"] = (
        capo_ssm.types.resource_type_for_tagging.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        import capo_ssm.types.resource_type_for_tagging

        out["resource_type"] = (
            capo_ssm.types.resource_type_for_tagging.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_ssm.types.resource_type_for_tagging.ResourceTypeForTagging", ""
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    return out
