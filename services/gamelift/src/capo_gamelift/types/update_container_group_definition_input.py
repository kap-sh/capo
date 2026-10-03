"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateContainerGroupDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition_name_or_arn
    import capo_gamelift.types.container_operating_system
    import capo_gamelift.types.container_total_memory_limit
    import capo_gamelift.types.container_total_vcpu_limit
    import capo_gamelift.types.game_server_container_definition_input
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.support_container_definition_input_list


class UpdateContainerGroupDefinitionInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>A descriptive identifier for the container group definition. The name value must be unique in an Amazon Web Services Region.</p>"""
    game_server_container_definition: NotRequired[
        "capo_gamelift.types.game_server_container_definition_input.GameServerContainerDefinitionInput"
    ]
    """<p>An updated definition for the game server container in this group. Define a game server container only when the container group type is <code>GAME_SERVER</code>. You can pass in your container definitions as a JSON file.</p>"""
    support_container_definitions: NotRequired[
        "capo_gamelift.types.support_container_definition_input_list.SupportContainerDefinitionInputList"
    ]
    """<p>One or more definitions for support containers in this group. You can define a support container in any type of container group. You can pass in your container definitions as a JSON file.</p>"""
    total_memory_limit_mebibytes: NotRequired[
        "capo_gamelift.types.container_total_memory_limit.ContainerTotalMemoryLimit"
    ]
    """<p>The maximum amount of memory (in MiB) to allocate to the container group. All containers in the group share this memory. If you specify memory limits for an individual container, the total value must be greater than any individual container's memory limit.</p>"""
    total_vcpu_limit: NotRequired[
        "capo_gamelift.types.container_total_vcpu_limit.ContainerTotalVcpuLimit"
    ]
    """<p>The maximum amount of vCPU units to allocate to the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share this memory. If you specify vCPU limits for individual containers, the total value must be equal to or greater than the sum of the CPU limits for all containers in the group.</p>"""
    version_description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A description for this update to the container group definition. </p>"""
    source_version_number: NotRequired[
        "capo_gamelift.types.positive_integer.PositiveInteger"
    ]
    """<p>The container group definition version to update. The new version starts with values from the source version, and then updates values included in this request. </p>"""
    operating_system: NotRequired[
        "capo_gamelift.types.container_operating_system.ContainerOperatingSystem"
    ]
    """<p>The platform that all containers in the group use. Containers in a group must run on the same operating system.</p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContainerGroupDefinitionInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
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
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "source_version_number" in value:
        out["SourceVersionNumber"] = value["source_version_number"]
    if "operating_system" in value:
        import capo_gamelift.types.container_operating_system

        out["OperatingSystem"] = (
            capo_gamelift.types.container_operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContainerGroupDefinitionInput:
    out: UpdateContainerGroupDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("TotalMemoryLimitMebibytes") is not None:
        out["total_memory_limit_mebibytes"] = data["TotalMemoryLimitMebibytes"]
    if data.get("TotalVcpuLimit") is not None:
        out["total_vcpu_limit"] = float(data["TotalVcpuLimit"])
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("SourceVersionNumber") is not None:
        out["source_version_number"] = data["SourceVersionNumber"]
    if data.get("OperatingSystem") is not None:
        import capo_gamelift.types.container_operating_system

        out["operating_system"] = (
            capo_gamelift.types.container_operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    return out
