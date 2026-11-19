"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.tag_key
    import capo_config_service.types.tag_value


class ConformancePackScope(TypedDict, closed=True):
    tag_key: "capo_config_service.types.tag_key.TagKey"
    """<p>The tag key that applies to only those Amazon Web Services resources that you want to trigger an evaluation for the rules in the conformance pack. Defines the <a>Scope$TagKey</a> of all Config rules in the conformance pack. </p>"""
    tag_value: NotRequired["capo_config_service.types.tag_value.TagValue"]
    """<p>The tag value that applies to only those Amazon Web Services resources that you want to trigger an evaluation for the rules in the conformance pack. If you do not specify a value for <code>TagValue</code>, resources that have the tag key <code>TagKey</code> trigger an evaluation, regardless of the tag value. Defines the <a>Scope$TagValue</a> of all Config rules in the conformance pack. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackScope) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    if "tag_value" in value:
        out["TagValue"] = value["tag_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackScope:
    out: ConformancePackScope = {}  # type: ignore[typeddict-item]
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    else:
        out["tag_key"] = ""
    if data.get("TagValue") is not None:
        out["tag_value"] = data["TagValue"]
    return out
