"""Generated from Smithy shape ``com.amazonaws.codebuild#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.security_group_ids
    import capo_codebuild.types.subnets


class VpcConfig(TypedDict, closed=True):
    vpc_id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the Amazon VPC.</p>"""
    subnets: NotRequired["capo_codebuild.types.subnets.Subnets"]
    """<p>A list of one or more subnet IDs in your Amazon VPC.</p>"""
    security_group_ids: NotRequired[
        "capo_codebuild.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of one or more security groups IDs in your Amazon VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfig) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnets" in value:
        import capo_codebuild.types.subnets

        out["subnets"] = capo_codebuild.types.subnets.serialize_aws_json_1_1(
            value["subnets"]
        )
    if "security_group_ids" in value:
        import capo_codebuild.types.security_group_ids

        out["securityGroupIds"] = (
            capo_codebuild.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("subnets") is not None:
        import capo_codebuild.types.subnets

        out["subnets"] = capo_codebuild.types.subnets.deserialize_aws_json_1_1(
            data["subnets"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_codebuild.types.security_group_ids

        out["security_group_ids"] = (
            capo_codebuild.types.security_group_ids.deserialize_aws_json_1_1(
                data["securityGroupIds"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VpcConfig) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnets" in value:
        import capo_codebuild.types.subnets

        out["subnets"] = capo_codebuild.types.subnets.serialize_cbor(value["subnets"])
    if "security_group_ids" in value:
        import capo_codebuild.types.security_group_ids

        out["securityGroupIds"] = (
            capo_codebuild.types.security_group_ids.serialize_cbor(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("subnets") is not None:
        import capo_codebuild.types.subnets

        out["subnets"] = capo_codebuild.types.subnets.deserialize_cbor(data["subnets"])
    if data.get("securityGroupIds") is not None:
        import capo_codebuild.types.security_group_ids

        out["security_group_ids"] = (
            capo_codebuild.types.security_group_ids.deserialize_cbor(
                data["securityGroupIds"]
            )
        )
    return out
