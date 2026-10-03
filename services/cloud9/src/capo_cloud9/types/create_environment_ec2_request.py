"""Generated from Smithy shape ``com.amazonaws.cloud9#CreateEnvironmentEC2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloud9.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloud9.types.automatic_stop_time_minutes
    import capo_cloud9.types.client_request_token
    import capo_cloud9.types.connection_type
    import capo_cloud9.types.environment_description
    import capo_cloud9.types.environment_name
    import capo_cloud9.types.image_id
    import capo_cloud9.types.instance_type
    import capo_cloud9.types.nullable_boolean
    import capo_cloud9.types.subnet_id
    import capo_cloud9.types.tag_list
    import capo_cloud9.types.user_arn


class CreateEnvironmentEC2Request(TypedDict, closed=True):
    name: "capo_cloud9.types.environment_name.EnvironmentName"
    """<p>The name of the environment to create.</p> <p>This name is visible to other IAM users in the same Amazon Web Services account.</p>"""
    description: NotRequired[
        "capo_cloud9.types.environment_description.EnvironmentDescription"
    ]
    """<p>The description of the environment to create.</p>"""
    client_request_token: NotRequired[
        "capo_cloud9.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, case-sensitive string that helps Cloud9 to ensure this operation completes no more than one time.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Client Tokens</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    instance_type: "capo_cloud9.types.instance_type.InstanceType"
    """<p>The type of instance to connect to the environment (for example, <code>t2.micro</code>).</p>"""
    subnet_id: NotRequired["capo_cloud9.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in Amazon VPC that Cloud9 will use to communicate with the Amazon EC2 instance.</p>"""
    image_id: "capo_cloud9.types.image_id.ImageId"
    """<p>The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. To choose an AMI for the instance, you must specify a valid AMI alias or a valid Amazon EC2 Systems Manager (SSM) path.</p> <p></p> <p>We recommend using Amazon Linux 2023 as the AMI to create your environment as it is fully supported.</p> <p>From December 16, 2024, Ubuntu 18.04 will be removed from the list of available <code>imageIds</code> for Cloud9. This change is necessary as Ubuntu 18.04 has ended standard support on May 31, 2023. This change will only affect direct API consumers, and not Cloud9 console users.</p> <p>Since Ubuntu 18.04 has ended standard support as of May 31, 2023, we recommend you choose Ubuntu 22.04.</p> <p> <b>AMI aliases </b> </p> <ul> <li> <p>Amazon Linux 2023 (recommended): <code>amazonlinux-2023-x86_64</code> </p> </li> <li> <p>Ubuntu 22.04: <code>ubuntu-22.04-x86_64</code> </p> </li> </ul> <p> <b>SSM paths</b> </p> <ul> <li> <p>Amazon Linux 2023 (recommended): <code>resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2023-x86_64</code> </p> </li> <li> <p>Ubuntu 22.04: <code>resolve:ssm:/aws/service/cloud9/amis/ubuntu-22.04-x86_64</code> </p> </li> </ul>"""
    automatic_stop_time_minutes: NotRequired[
        "capo_cloud9.types.automatic_stop_time_minutes.AutomaticStopTimeMinutes"
    ]
    """<p>The number of minutes until the running instance is shut down after the environment has last been used.</p>"""
    owner_arn: NotRequired["capo_cloud9.types.user_arn.UserArn"]
    """<p>The Amazon Resource Name (ARN) of the environment owner. This ARN can be the ARN of any IAM principal. If this value is not specified, the ARN defaults to this environment's creator.</p>"""
    tags: NotRequired["capo_cloud9.types.tag_list.TagList"]
    """<p>An array of key-value pairs that will be associated with the new Cloud9 development environment.</p>"""
    connection_type: NotRequired["capo_cloud9.types.connection_type.ConnectionType"]
    """<p>The connection type used for connecting to an Amazon EC2 environment. Valid values are <code>CONNECT_SSH</code> (default) and <code>CONNECT_SSM</code> (connected through Amazon EC2 Systems Manager).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html">Accessing no-ingress EC2 instances with Amazon EC2 Systems Manager</a> in the <i>Cloud9 User Guide</i>.</p>"""
    dry_run: NotRequired["capo_cloud9.types.nullable_boolean.NullableBoolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEnvironmentEC2Request) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["instanceType"] = value["instance_type"]
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    out["imageId"] = value["image_id"]
    if "automatic_stop_time_minutes" in value:
        out["automaticStopTimeMinutes"] = value["automatic_stop_time_minutes"]
    if "owner_arn" in value:
        out["ownerArn"] = value["owner_arn"]
    if "tags" in value:
        import capo_cloud9.types.tag_list

        out["tags"] = capo_cloud9.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "connection_type" in value:
        import capo_cloud9.types.connection_type

        out["connectionType"] = (
            capo_cloud9.types.connection_type.serialize_aws_json_1_1(
                value["connection_type"]
            )
        )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEnvironmentEC2Request:
    out: CreateEnvironmentEC2Request = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentEC2Request.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError("CreateEnvironmentEC2Request.instance_type required")
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    if data.get("imageId") is not None:
        out["image_id"] = data["imageId"]
    else:
        raise DeserializationError("CreateEnvironmentEC2Request.image_id required")
    if data.get("automaticStopTimeMinutes") is not None:
        out["automatic_stop_time_minutes"] = data["automaticStopTimeMinutes"]
    if data.get("ownerArn") is not None:
        out["owner_arn"] = data["ownerArn"]
    if data.get("tags") is not None:
        import capo_cloud9.types.tag_list

        out["tags"] = capo_cloud9.types.tag_list.deserialize_aws_json_1_1(data["tags"])
    if data.get("connectionType") is not None:
        import capo_cloud9.types.connection_type

        out["connection_type"] = (
            capo_cloud9.types.connection_type.deserialize_aws_json_1_1(
                data["connectionType"]
            )
        )
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
