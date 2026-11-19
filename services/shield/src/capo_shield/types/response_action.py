"""Generated from Smithy shape ``com.amazonaws.shield#ResponseAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.block_action
    import capo_shield.types.count_action


class ResponseAction(TypedDict, closed=True):
    block: NotRequired["capo_shield.types.block_action.BlockAction"]
    """<p>Specifies that Shield Advanced should configure its WAF rules with the WAF <code>Block</code> action. </p> <p>You must specify exactly one action, either <code>Block</code> or <code>Count</code>.</p>"""
    count: NotRequired["capo_shield.types.count_action.CountAction"]
    """<p>Specifies that Shield Advanced should configure its WAF rules with the WAF <code>Count</code> action. </p> <p>You must specify exactly one action, either <code>Block</code> or <code>Count</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseAction) -> dict:
    out: dict = {}
    if "block" in value:
        import capo_shield.types.block_action

        out["Block"] = capo_shield.types.block_action.serialize_aws_json_1_1(
            value["block"]
        )
    if "count" in value:
        import capo_shield.types.count_action

        out["Count"] = capo_shield.types.count_action.serialize_aws_json_1_1(
            value["count"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseAction:
    out: ResponseAction = {}  # type: ignore[typeddict-item]
    if data.get("Block") is not None:
        import capo_shield.types.block_action

        out["block"] = capo_shield.types.block_action.deserialize_aws_json_1_1(
            data["Block"]
        )
    if data.get("Count") is not None:
        import capo_shield.types.count_action

        out["count"] = capo_shield.types.count_action.deserialize_aws_json_1_1(
            data["Count"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResponseAction) -> dict:
    out: dict = {}
    if "block" in value:
        import capo_shield.types.block_action

        out["Block"] = capo_shield.types.block_action.serialize_cbor(value["block"])
    if "count" in value:
        import capo_shield.types.count_action

        out["Count"] = capo_shield.types.count_action.serialize_cbor(value["count"])
    return out


def deserialize_cbor(data: dict) -> ResponseAction:
    out: ResponseAction = {}  # type: ignore[typeddict-item]
    if data.get("Block") is not None:
        import capo_shield.types.block_action

        out["block"] = capo_shield.types.block_action.deserialize_cbor(data["Block"])
    if data.get("Count") is not None:
        import capo_shield.types.count_action

        out["count"] = capo_shield.types.count_action.deserialize_cbor(data["Count"])
    return out
