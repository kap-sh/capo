"""Generated from Smithy shape ``com.amazonaws.mediastore#MetricPolicyRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediastore.types.object_group
    import capo_mediastore.types.object_group_name


class MetricPolicyRule(TypedDict, closed=True):
    object_group: "capo_mediastore.types.object_group.ObjectGroup"
    """<p>A path or file name that defines which objects to include in the group. Wildcards (*) are acceptable.</p>"""
    object_group_name: "capo_mediastore.types.object_group_name.ObjectGroupName"
    """<p>A name that allows you to refer to the object group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricPolicyRule) -> dict:
    out: dict = {}
    out["ObjectGroup"] = value["object_group"]
    out["ObjectGroupName"] = value["object_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricPolicyRule:
    out: MetricPolicyRule = {}  # type: ignore[typeddict-item]
    if data.get("ObjectGroup") is not None:
        out["object_group"] = data["ObjectGroup"]
    else:
        out["object_group"] = ""
    if data.get("ObjectGroupName") is not None:
        out["object_group_name"] = data["ObjectGroupName"]
    else:
        out["object_group_name"] = ""
    return out
