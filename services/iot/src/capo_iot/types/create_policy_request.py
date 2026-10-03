"""Generated from Smithy shape ``com.amazonaws.iot#CreatePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.policy_document
    import capo_iot.types.policy_name
    import capo_iot.types.tag_list


class CreatePolicyRequest(TypedDict, closed=True):
    policy_name: "capo_iot.types.policy_name.PolicyName"
    """<p>The policy name.</p>"""
    policy_document: "capo_iot.types.policy_document.PolicyDocument"
    """<p>The JSON document that describes the policy. <b>policyDocument</b> must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the policy.</p> <note> <p>For URI Request parameters use format: ...key1=value1&key2=value2...</p> <p>For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."</p> <p>For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyRequest) -> dict:
    out: dict = {}
    out["policyDocument"] = value["policy_document"]
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePolicyRequest:
    out: CreatePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        raise DeserializationError("CreatePolicyRequest.policy_document required")
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    return out
