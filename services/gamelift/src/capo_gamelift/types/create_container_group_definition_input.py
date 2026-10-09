"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateContainerGroupDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition_name
    import capo_gamelift.types.container_group_type
    import capo_gamelift.types.container_operating_system
    import capo_gamelift.types.container_total_memory_limit
    import capo_gamelift.types.container_total_vcpu_limit
    import capo_gamelift.types.game_server_container_definition_input
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.support_container_definition_input_list
    import capo_gamelift.types.tag_list


class CreateContainerGroupDefinitionInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.container_group_definition_name.ContainerGroupDefinitionName"
    ]
    """<p>A descriptive identifier for the container group definition. The name value must be unique in an Amazon Web Services Region.</p>"""
    container_group_type: NotRequired[
        "capo_gamelift.types.container_group_type.ContainerGroupType"
    ]
    """<p>The type of container group being defined. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.</p> <p>Default value: <code>GAME_SERVER</code> </p>"""
    total_memory_limit_mebibytes: NotRequired[
        "capo_gamelift.types.container_total_memory_limit.ContainerTotalMemoryLimit"
    ]
    """<p>The maximum amount of memory (in MiB) to allocate to the container group. All containers in the group share this memory. If you specify memory limits for an individual container, the total value must be greater than any individual container's memory limit.</p> <p>Default value: 1024</p>"""
    total_vcpu_limit: NotRequired[
        "capo_gamelift.types.container_total_vcpu_limit.ContainerTotalVcpuLimit"
    ]
    """<p>The maximum amount of vCPU units to allocate to the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share these resources. If you set vCPU reservations for individual containers, the total value must be equal to or greater than the sum of the <code>Vcpu</code> values for all containers in the group.</p> <p>This property is required for a per-instance container group.</p> <p>For a game server container group, Amazon GameLift Servers requires either a total vCPU limit or a <code>Vcpu</code> value for the game server container. If you set a total vCPU limit for a game server container group, Amazon GameLift Servers uses this value to calculate how many game server container groups fit on an instance. If you don't set a total vCPU limit, the group's containers can use up to the instance's available vCPU, and Amazon GameLift Servers uses the sum of the containers' <code>Vcpu</code> values to calculate how many game server container groups fit on an instance.</p>"""
    game_server_container_definition: NotRequired[
        "capo_gamelift.types.game_server_container_definition_input.GameServerContainerDefinitionInput"
    ]
    """<p>The definition for the game server container in this group. Define a game server container only when the container group type is <code>GAME_SERVER</code>. Game server containers specify a container image with your game server build. You can pass in your container definitions as a JSON file.</p>"""
    support_container_definitions: NotRequired[
        "capo_gamelift.types.support_container_definition_input_list.SupportContainerDefinitionInputList"
    ]
    """<p>One or more definition for support containers in this group. You can define a support container in any type of container group. You can pass in your container definitions as a JSON file.</p>"""
    operating_system: NotRequired[
        "capo_gamelift.types.container_operating_system.ContainerOperatingSystem"
    ]
    """<p>The platform that all containers in the group use. Containers in a group must run on the same operating system.</p> <p>Default value: <code>AMAZON_LINUX_2023</code> </p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>"""
    version_description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A description for the initial version of this container group definition. </p>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of labels to assign to the container group definition resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerGroupDefinitionInput) -> dict:
    out: dict = {}
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
        import capo_gamelift.types.game_server_container_definition_input

        out["GameServerContainerDefinition"] = (
            capo_gamelift.types.game_server_container_definition_input.serialize_aws_json_1_1(
                value["game_server_container_definition"]
            )
        )
    if "support_container_definitions" in value:
        import capo_gamelift.types.support_container_definition_input_list

        out["SupportContainerDefinitions"] = (
            capo_gamelift.types.support_container_definition_input_list.serialize_aws_json_1_1(
                value["support_container_definitions"]
            )
        )
    if "operating_system" in value:
        import capo_gamelift.types.container_operating_system

        out["OperatingSystem"] = (
            capo_gamelift.types.container_operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerGroupDefinitionInput:
    out: CreateContainerGroupDefinitionInput = {}  # type: ignore[typeddict-item]
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
        import capo_gamelift.types.game_server_container_definition_input

        out["game_server_container_definition"] = (
            capo_gamelift.types.game_server_container_definition_input.deserialize_aws_json_1_1(
                data["GameServerContainerDefinition"]
            )
        )
    if data.get("SupportContainerDefinitions") is not None:
        import capo_gamelift.types.support_container_definition_input_list

        out["support_container_definitions"] = (
            capo_gamelift.types.support_container_definition_input_list.deserialize_aws_json_1_1(
                data["SupportContainerDefinitions"]
            )
        )
    if data.get("OperatingSystem") is not None:
        import capo_gamelift.types.container_operating_system

        out["operating_system"] = (
            capo_gamelift.types.container_operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
