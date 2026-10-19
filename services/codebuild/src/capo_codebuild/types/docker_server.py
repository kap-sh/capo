"""Generated from Smithy shape ``com.amazonaws.codebuild#DockerServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.compute_type
    import capo_codebuild.types.docker_server_status
    import capo_codebuild.types.security_group_ids


class DockerServer(TypedDict, closed=True):
    compute_type: "capo_codebuild.types.compute_type.ComputeType"
    """<p>Information about the compute resources the docker server uses. Available values include:</p> <ul> <li> <p> <code>BUILD_GENERAL1_SMALL</code>: Use up to 4 GiB memory and 2 vCPUs for your docker server.</p> </li> <li> <p> <code>BUILD_GENERAL1_MEDIUM</code>: Use up to 8 GiB memory and 4 vCPUs for your docker server.</p> </li> <li> <p> <code>BUILD_GENERAL1_LARGE</code>: Use up to 16 GiB memory and 8 vCPUs for your docker server.</p> </li> <li> <p> <code>BUILD_GENERAL1_XLARGE</code>: Use up to 64 GiB memory and 32 vCPUs for your docker server.</p> </li> <li> <p> <code>BUILD_GENERAL1_2XLARGE</code>: Use up to 128 GiB memory and 64 vCPUs for your docker server.</p> </li> </ul>"""
    security_group_ids: NotRequired[
        "capo_codebuild.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of one or more security groups IDs.</p> <note> <p>Security groups configured for Docker servers should allow ingress network traffic from the VPC configured in the project. They should allow ingress on port 9876.</p> </note>"""
    status: NotRequired["capo_codebuild.types.docker_server_status.DockerServerStatus"]
    """<p>A DockerServerStatus object to use for this docker server.</p> <note> <p>Note that <code>status</code> is only an output and cannot be passed in as an input.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DockerServer) -> dict:
    out: dict = {}
    import capo_codebuild.types.compute_type

    out["computeType"] = capo_codebuild.types.compute_type.serialize_aws_json_1_1(
        value["compute_type"]
    )
    if "security_group_ids" in value:
        import capo_codebuild.types.security_group_ids

        out["securityGroupIds"] = (
            capo_codebuild.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "status" in value:
        import capo_codebuild.types.docker_server_status

        out["status"] = (
            capo_codebuild.types.docker_server_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DockerServer:
    out: DockerServer = {}  # type: ignore[typeddict-item]
    if data.get("computeType") is not None:
        import capo_codebuild.types.compute_type

        out["compute_type"] = (
            capo_codebuild.types.compute_type.deserialize_aws_json_1_1(
                data["computeType"]
            )
        )
    else:
        import typing

        out["compute_type"] = typing.cast(
            "capo_codebuild.types.compute_type.ComputeType", ""
        )
    if data.get("securityGroupIds") is not None:
        import capo_codebuild.types.security_group_ids

        out["security_group_ids"] = (
            capo_codebuild.types.security_group_ids.deserialize_aws_json_1_1(
                data["securityGroupIds"]
            )
        )
    if data.get("status") is not None:
        import capo_codebuild.types.docker_server_status

        out["status"] = (
            capo_codebuild.types.docker_server_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
