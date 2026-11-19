"""Generated from Smithy shape ``com.amazonaws.snowball#JobResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.ec2_ami_resource_list
    import capo_snowball.types.lambda_resource_list
    import capo_snowball.types.s3_resource_list


class JobResource(TypedDict, closed=True):
    s3_resources: NotRequired["capo_snowball.types.s3_resource_list.S3ResourceList"]
    """<p>An array of <code>S3Resource</code> objects.</p>"""
    lambda_resources: NotRequired[
        "capo_snowball.types.lambda_resource_list.LambdaResourceList"
    ]
    """<p>The Python-language Lambda functions for this job.</p>"""
    ec2_ami_resources: NotRequired[
        "capo_snowball.types.ec2_ami_resource_list.Ec2AmiResourceList"
    ]
    """<p>The Amazon Machine Images (AMIs) associated with this job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobResource) -> dict:
    out: dict = {}
    if "s3_resources" in value:
        import capo_snowball.types.s3_resource_list

        out["S3Resources"] = (
            capo_snowball.types.s3_resource_list.serialize_aws_json_1_1(
                value["s3_resources"]
            )
        )
    if "lambda_resources" in value:
        import capo_snowball.types.lambda_resource_list

        out["LambdaResources"] = (
            capo_snowball.types.lambda_resource_list.serialize_aws_json_1_1(
                value["lambda_resources"]
            )
        )
    if "ec2_ami_resources" in value:
        import capo_snowball.types.ec2_ami_resource_list

        out["Ec2AmiResources"] = (
            capo_snowball.types.ec2_ami_resource_list.serialize_aws_json_1_1(
                value["ec2_ami_resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobResource:
    out: JobResource = {}  # type: ignore[typeddict-item]
    if data.get("S3Resources") is not None:
        import capo_snowball.types.s3_resource_list

        out["s3_resources"] = (
            capo_snowball.types.s3_resource_list.deserialize_aws_json_1_1(
                data["S3Resources"]
            )
        )
    if data.get("LambdaResources") is not None:
        import capo_snowball.types.lambda_resource_list

        out["lambda_resources"] = (
            capo_snowball.types.lambda_resource_list.deserialize_aws_json_1_1(
                data["LambdaResources"]
            )
        )
    if data.get("Ec2AmiResources") is not None:
        import capo_snowball.types.ec2_ami_resource_list

        out["ec2_ami_resources"] = (
            capo_snowball.types.ec2_ami_resource_list.deserialize_aws_json_1_1(
                data["Ec2AmiResources"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JobResource) -> dict:
    out: dict = {}
    if "s3_resources" in value:
        import capo_snowball.types.s3_resource_list

        out["S3Resources"] = capo_snowball.types.s3_resource_list.serialize_cbor(
            value["s3_resources"]
        )
    if "lambda_resources" in value:
        import capo_snowball.types.lambda_resource_list

        out["LambdaResources"] = (
            capo_snowball.types.lambda_resource_list.serialize_cbor(
                value["lambda_resources"]
            )
        )
    if "ec2_ami_resources" in value:
        import capo_snowball.types.ec2_ami_resource_list

        out["Ec2AmiResources"] = (
            capo_snowball.types.ec2_ami_resource_list.serialize_cbor(
                value["ec2_ami_resources"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> JobResource:
    out: JobResource = {}  # type: ignore[typeddict-item]
    if data.get("S3Resources") is not None:
        import capo_snowball.types.s3_resource_list

        out["s3_resources"] = capo_snowball.types.s3_resource_list.deserialize_cbor(
            data["S3Resources"]
        )
    if data.get("LambdaResources") is not None:
        import capo_snowball.types.lambda_resource_list

        out["lambda_resources"] = (
            capo_snowball.types.lambda_resource_list.deserialize_cbor(
                data["LambdaResources"]
            )
        )
    if data.get("Ec2AmiResources") is not None:
        import capo_snowball.types.ec2_ami_resource_list

        out["ec2_ami_resources"] = (
            capo_snowball.types.ec2_ami_resource_list.deserialize_cbor(
                data["Ec2AmiResources"]
            )
        )
    return out
