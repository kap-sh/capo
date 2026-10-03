"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition_arn
    import capo_gamelift.types.container_group_definition_name
    import capo_gamelift.types.container_group_definition_status
    import capo_gamelift.types.container_group_type
    import capo_gamelift.types.container_operating_system
    import capo_gamelift.types.container_total_memory_limit
    import capo_gamelift.types.container_total_vcpu_limit
    import capo_gamelift.types.game_server_container_definition
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.support_container_definition_list
    import capo_gamelift.types.timestamp


class ContainerGroupDefinition(TypedDict, closed=True):
    container_group_definition_arn: NotRequired[
        "capo_gamelift.types.container_group_definition_arn.ContainerGroupDefinitionArn"
    ]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to an Amazon GameLift Servers <code>ContainerGroupDefinition</code> resource. It uniquely identifies the resource across all Amazon Web Services Regions. Format is <code>arn:aws:gamelift:[region]::containergroupdefinition/[container group definition name]:[version]</code>.</p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    operating_system: NotRequired[
        "capo_gamelift.types.container_operating_system.ContainerOperatingSystem"
    ]
    """<p>The platform that all containers in the container group definition run on.</p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>"""
    name: NotRequired[
        "capo_gamelift.types.container_group_definition_name.ContainerGroupDefinitionName"
    ]
    """<p>A descriptive identifier for the container group definition. The name value is unique in an Amazon Web Services Region.</p>"""
    container_group_type: NotRequired[
        "capo_gamelift.types.container_group_type.ContainerGroupType"
    ]
    """<p>The type of container group. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.</p>"""
    total_memory_limit_mebibytes: NotRequired[
        "capo_gamelift.types.container_total_memory_limit.ContainerTotalMemoryLimit"
    ]
    """<p>The amount of memory (in MiB) on a fleet instance to allocate for the container group. All containers in the group share these resources. </p> <p>You can set a limit for each container definition in the group. If individual containers have limits, this total value must be greater than any individual container's memory limit.</p>"""
    total_vcpu_limit: NotRequired[
        "capo_gamelift.types.container_total_vcpu_limit.ContainerTotalVcpuLimit"
    ]
    """<p>The amount of vCPU units on a fleet instance to allocate for the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share these resources. You can set a limit for each container definition in the group. If individual containers have limits, this total value must be equal to or greater than the sum of the limits for each container in the group.</p>"""
    game_server_container_definition: NotRequired[
        "capo_gamelift.types.game_server_container_definition.GameServerContainerDefinition"
    ]
    """<p>The definition for the game server container in this group. This property is used only when the container group type is <code>GAME_SERVER</code>. This container definition specifies a container image with the game server build. </p>"""
    support_container_definitions: NotRequired[
        "capo_gamelift.types.support_container_definition_list.SupportContainerDefinitionList"
    ]
    """<p>The set of definitions for support containers in this group. A container group definition might have zero support container definitions. Support container can be used in any type of container group.</p>"""
    version_number: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>Indicates the version of a particular container group definition. This number is incremented automatically when you update a container group definition. You can view, update, or delete individual versions or the entire container group definition.</p>"""
    version_description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>An optional description that was provided for a container group definition update. Each version can have a unique description.</p>"""
    status: NotRequired[
        "capo_gamelift.types.container_group_definition_status.ContainerGroupDefinitionStatus"
    ]
    """<p>Current status of the container group definition resource. Values include:</p> <ul> <li> <p> <code>COPYING</code> -- Amazon GameLift Servers is in the process of making copies of all container images that are defined in the group. While in this state, the resource can't be used to create a container fleet.</p> </li> <li> <p> <code>READY</code> -- Amazon GameLift Servers has copied the registry images for all containers that are defined in the group. You can use a container group definition in this status to create a container fleet. </p> </li> <li> <p> <code>FAILED</code> -- Amazon GameLift Servers failed to create a valid container group definition resource. For more details on the cause of the failure, see <code>StatusReason</code>. A container group definition resource in failed status will be deleted within a few minutes.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Additional information about a container group definition that's in <code>FAILED</code> status. Possible reasons include:</p> <ul> <li> <p>An internal issue prevented Amazon GameLift Servers from creating the container group definition resource. Delete the failed resource and call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html">CreateContainerGroupDefinition</a>again. </p> </li> <li> <p>An access-denied message means that you don't have permissions to access the container image on ECR. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-iam-policy-examples.html.html"> IAM permission examples</a> for help setting up required IAM permissions for Amazon GameLift Servers.</p> </li> <li> <p>The <code>ImageUri</code> value for at least one of the containers in the container group definition was invalid or not found in the current Amazon Web Services account.</p> </li> <li> <p>At least one of the container images referenced in the container group definition exceeds the allowed size. For size limits, see <a href="https://docs.aws.amazon.com/general/latest/gr/gamelift.html"> Amazon GameLift Servers endpoints and quotas</a>.</p> </li> <li> <p>At least one of the container images referenced in the container group definition uses a different operating system than the one defined for the container group.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerGroupDefinition) -> dict:
    out: dict = {}
    if "container_group_definition_arn" in value:
        out["ContainerGroupDefinitionArn"] = value["container_group_definition_arn"]
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "operating_system" in value:
        import capo_gamelift.types.container_operating_system

        out["OperatingSystem"] = (
            capo_gamelift.types.container_operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "container_group_type" in value:
        import capo_gamelift.types.container_group_type

        out["ContainerGroupType"] = (
            capo_gamelift.types.container_group_type.serialize_aws_json_1_1(
                value["container_group_type"]
            )
        )
    if "total_memory_limit_mebibytes" in value:
        out["TotalMemoryLimitMebibytes"] = value["total_memory_limit_mebibytes"]
    if "total_vcpu_limit" in value:
        out["TotalVcpuLimit"] = (
            "NaN"
            if value["total_vcpu_limit"] != value["total_vcpu_limit"]
            else "Infinity"
            if value["total_vcpu_limit"] == float("inf")
            else "-Infinity"
            if value["total_vcpu_limit"] == float("-inf")
            else value["total_vcpu_limit"]
        )
    if "game_server_container_definition" in value:
        import capo_gamelift.types.game_server_container_definition

        out["GameServerContainerDefinition"] = (
            capo_gamelift.types.game_server_container_definition.serialize_aws_json_1_1(
                value["game_server_container_definition"]
            )
        )
    if "support_container_definitions" in value:
        import capo_gamelift.types.support_container_definition_list

        out["SupportContainerDefinitions"] = (
            capo_gamelift.types.support_container_definition_list.serialize_aws_json_1_1(
                value["support_container_definitions"]
            )
        )
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "status" in value:
        import capo_gamelift.types.container_group_definition_status

        out["Status"] = (
            capo_gamelift.types.container_group_definition_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerGroupDefinition:
    out: ContainerGroupDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ContainerGroupDefinitionArn") is not None:
        out["container_group_definition_arn"] = data["ContainerGroupDefinitionArn"]
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("OperatingSystem") is not None:
        import capo_gamelift.types.container_operating_system

        out["operating_system"] = (
            capo_gamelift.types.container_operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ContainerGroupType") is not None:
        import capo_gamelift.types.container_group_type

        out["container_group_type"] = (
            capo_gamelift.types.container_group_type.deserialize_aws_json_1_1(
                data["ContainerGroupType"]
            )
        )
    if data.get("TotalMemoryLimitMebibytes") is not None:
        out["total_memory_limit_mebibytes"] = data["TotalMemoryLimitMebibytes"]
    if data.get("TotalVcpuLimit") is not None:
        out["total_vcpu_limit"] = float(data["TotalVcpuLimit"])
    if data.get("GameServerContainerDefinition") is not None:
        import capo_gamelift.types.game_server_container_definition

        out["game_server_container_definition"] = (
            capo_gamelift.types.game_server_container_definition.deserialize_aws_json_1_1(
                data["GameServerContainerDefinition"]
            )
        )
    if data.get("SupportContainerDefinitions") is not None:
        import capo_gamelift.types.support_container_definition_list

        out["support_container_definitions"] = (
            capo_gamelift.types.support_container_definition_list.deserialize_aws_json_1_1(
                data["SupportContainerDefinitions"]
            )
        )
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("Status") is not None:
        import capo_gamelift.types.container_group_definition_status

        out["status"] = (
            capo_gamelift.types.container_group_definition_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    return out
