"""Generated from Smithy shape ``com.amazonaws.health#DescribeTagKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.resource_tag_key_list


class DescribeTagKeysResponse(TypedDict, closed=True):
    keys: NotRequired["capo_health.types.resource_tag_key_list.ResourceTagKeyList"]
    """<p>The list of configured resource tag keys and their status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagKeysResponse) -> dict:
    out: dict = {}
    if "keys" in value:
        import capo_health.types.resource_tag_key_list

        out["keys"] = capo_health.types.resource_tag_key_list.serialize_aws_json_1_1(
            value["keys"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagKeysResponse:
    out: DescribeTagKeysResponse = {}  # type: ignore[typeddict-item]
    if data.get("keys") is not None:
        import capo_health.types.resource_tag_key_list

        out["keys"] = capo_health.types.resource_tag_key_list.deserialize_aws_json_1_1(
            data["keys"]
        )
    return out
