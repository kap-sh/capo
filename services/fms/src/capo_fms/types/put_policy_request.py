"""Generated from Smithy shape ``com.amazonaws.fms#PutPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.policy
    import capo_fms.types.tag_list


class PutPolicyRequest(TypedDict, closed=True):
    policy: "capo_fms.types.policy.Policy"
    """<p>The details of the Firewall Manager policy to be created.</p>"""
    tag_list: NotRequired["capo_fms.types.tag_list.TagList"]
    """<p>The tags to add to the Amazon Web Services resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPolicyRequest) -> dict:
    out: dict = {}
    import capo_fms.types.policy

    out["Policy"] = capo_fms.types.policy.serialize_aws_json_1_1(value["policy"])
    if "tag_list" in value:
        import capo_fms.types.tag_list

        out["TagList"] = capo_fms.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPolicyRequest:
    out: PutPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        import capo_fms.types.policy

        out["policy"] = capo_fms.types.policy.deserialize_aws_json_1_1(data["Policy"])
    else:
        raise DeserializationError("PutPolicyRequest.policy required")
    if data.get("TagList") is not None:
        import capo_fms.types.tag_list

        out["tag_list"] = capo_fms.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutPolicyRequest) -> dict:
    out: dict = {}
    import capo_fms.types.policy

    out["Policy"] = capo_fms.types.policy.serialize_cbor(value["policy"])
    if "tag_list" in value:
        import capo_fms.types.tag_list

        out["TagList"] = capo_fms.types.tag_list.serialize_cbor(value["tag_list"])
    return out


def deserialize_cbor(data: dict) -> PutPolicyRequest:
    out: PutPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        import capo_fms.types.policy

        out["policy"] = capo_fms.types.policy.deserialize_cbor(data["Policy"])
    else:
        raise DeserializationError("PutPolicyRequest.policy required")
    if data.get("TagList") is not None:
        import capo_fms.types.tag_list

        out["tag_list"] = capo_fms.types.tag_list.deserialize_cbor(data["TagList"])
    return out
