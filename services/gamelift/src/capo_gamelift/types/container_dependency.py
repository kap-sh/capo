"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerDependency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_dependency_condition
    import capo_gamelift.types.non_zero_and128_max_ascii_string


class ContainerDependency(TypedDict, closed=True):
    container_name: NotRequired[
        "capo_gamelift.types.non_zero_and128_max_ascii_string.NonZeroAnd128MaxAsciiString"
    ]
    """<p>A descriptive label for the container definition that this container depends on.</p>"""
    condition: NotRequired[
        "capo_gamelift.types.container_dependency_condition.ContainerDependencyCondition"
    ]
    """<p>The condition that the dependency container must reach before the dependent container can start. Valid conditions include: </p> <ul> <li> <p>START - The dependency container must have started. </p> </li> <li> <p>COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container can't be an essential container. </p> </li> <li> <p>SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container can't be an essential container. </p> </li> <li> <p>HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDependency) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "condition" in value:
        import capo_gamelift.types.container_dependency_condition

        out["Condition"] = (
            capo_gamelift.types.container_dependency_condition.serialize_aws_json_1_1(
                value["condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerDependency:
    out: ContainerDependency = {}  # type: ignore[typeddict-item]
    if data.get("ContainerName") is not None:
        out["container_name"] = data["ContainerName"]
    if data.get("Condition") is not None:
        import capo_gamelift.types.container_dependency_condition

        out["condition"] = (
            capo_gamelift.types.container_dependency_condition.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerDependency) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "condition" in value:
        import capo_gamelift.types.container_dependency_condition

        out["Condition"] = (
            capo_gamelift.types.container_dependency_condition.serialize_cbor(
                value["condition"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ContainerDependency:
    out: ContainerDependency = {}  # type: ignore[typeddict-item]
    if data.get("ContainerName") is not None:
        out["container_name"] = data["ContainerName"]
    if data.get("Condition") is not None:
        import capo_gamelift.types.container_dependency_condition

        out["condition"] = (
            capo_gamelift.types.container_dependency_condition.deserialize_cbor(
                data["Condition"]
            )
        )
    return out
