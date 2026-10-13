"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateContainerGroupDefinitionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition


class CreateContainerGroupDefinitionOutput(TypedDict, closed=True):
    container_group_definition: NotRequired[
        "capo_gamelift.types.container_group_definition.ContainerGroupDefinition"
    ]
    """<p>The properties of the new container group definition resource. You can use this resource to create a container fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerGroupDefinitionOutput) -> dict:
    out: dict = {}
    if "container_group_definition" in value:
        import capo_gamelift.types.container_group_definition

        out["ContainerGroupDefinition"] = (
            capo_gamelift.types.container_group_definition.serialize_aws_json_1_1(
                value["container_group_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerGroupDefinitionOutput:
    out: CreateContainerGroupDefinitionOutput = {}  # type: ignore[typeddict-item]
    if data.get("ContainerGroupDefinition") is not None:
        import capo_gamelift.types.container_group_definition

        out["container_group_definition"] = (
            capo_gamelift.types.container_group_definition.deserialize_aws_json_1_1(
                data["ContainerGroupDefinition"]
            )
        )
    return out


def redact_sensitive(value: CreateContainerGroupDefinitionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "container_group_definition" in value:
        import capo_gamelift.types.container_group_definition

        out["container_group_definition"] = (
            capo_gamelift.types.container_group_definition.redact_sensitive(
                value["container_group_definition"]
            )
        )
    return out
