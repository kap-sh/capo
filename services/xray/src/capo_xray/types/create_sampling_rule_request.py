"""Generated from Smithy shape ``com.amazonaws.xray#CreateSamplingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_xray.errors import DeserializationError

if TYPE_CHECKING:
    import capo_xray.types.sampling_rule
    import capo_xray.types.tag_list


class CreateSamplingRuleRequest(TypedDict, closed=True):
    sampling_rule: "capo_xray.types.sampling_rule.SamplingRule"
    """<p>The rule definition.</p>"""
    tags: NotRequired["capo_xray.types.tag_list.TagList"]
    """<p>A map that contains one or more tag keys and tag values to attach to an X-Ray sampling rule. For more information about ways to use tags, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>Maximum number of user-applied tags per resource: 50</p> </li> <li> <p>Maximum tag key length: 128 Unicode characters</p> </li> <li> <p>Maximum tag value length: 256 Unicode characters</p> </li> <li> <p>Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: _ . : / = + - and @</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for keys; it's reserved for Amazon Web Services use.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSamplingRuleRequest) -> dict:
    out: dict = {}
    import capo_xray.types.sampling_rule

    out["SamplingRule"] = capo_xray.types.sampling_rule.serialize_json(
        value["sampling_rule"]
    )
    if "tags" in value:
        import capo_xray.types.tag_list

        out["Tags"] = capo_xray.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSamplingRuleRequest:
    out: CreateSamplingRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("SamplingRule") is not None:
        import capo_xray.types.sampling_rule

        out["sampling_rule"] = capo_xray.types.sampling_rule.deserialize_json(
            data["SamplingRule"]
        )
    else:
        raise DeserializationError("CreateSamplingRuleRequest.sampling_rule required")
    if data.get("Tags") is not None:
        import capo_xray.types.tag_list

        out["tags"] = capo_xray.types.tag_list.deserialize_json(data["Tags"])
    return out
