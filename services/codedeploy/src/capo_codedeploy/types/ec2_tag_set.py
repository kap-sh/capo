"""Generated from Smithy shape ``com.amazonaws.codedeploy#EC2TagSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.ec2_tag_set_list


class EC2TagSet(TypedDict, closed=True):
    ec2_tag_set_list: NotRequired[
        "capo_codedeploy.types.ec2_tag_set_list.EC2TagSetList"
    ]
    """<p>A list that contains other lists of Amazon EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2TagSet) -> dict:
    out: dict = {}
    if "ec2_tag_set_list" in value:
        import capo_codedeploy.types.ec2_tag_set_list

        out["ec2TagSetList"] = (
            capo_codedeploy.types.ec2_tag_set_list.serialize_aws_json_1_1(
                value["ec2_tag_set_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2TagSet:
    out: EC2TagSet = {}  # type: ignore[typeddict-item]
    if data.get("ec2TagSetList") is not None:
        import capo_codedeploy.types.ec2_tag_set_list

        out["ec2_tag_set_list"] = (
            capo_codedeploy.types.ec2_tag_set_list.deserialize_aws_json_1_1(
                data["ec2TagSetList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2TagSet) -> dict:
    out: dict = {}
    if "ec2_tag_set_list" in value:
        import capo_codedeploy.types.ec2_tag_set_list

        out["ec2TagSetList"] = capo_codedeploy.types.ec2_tag_set_list.serialize_cbor(
            value["ec2_tag_set_list"]
        )
    return out


def deserialize_cbor(data: dict) -> EC2TagSet:
    out: EC2TagSet = {}  # type: ignore[typeddict-item]
    if data.get("ec2TagSetList") is not None:
        import capo_codedeploy.types.ec2_tag_set_list

        out["ec2_tag_set_list"] = (
            capo_codedeploy.types.ec2_tag_set_list.deserialize_cbor(
                data["ec2TagSetList"]
            )
        )
    return out
