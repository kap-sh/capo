"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerDependency``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.container_condition
    import capo_ecs.types.string


class ContainerDependency(TypedDict, closed=True):
    container_name: "capo_ecs.types.string.String"
    """<p>The name of a container.</p>"""
    condition: "capo_ecs.types.container_condition.ContainerCondition"
    """<p>The dependency condition of the container. The following are the available conditions and their behavior:</p> <ul> <li> <p> <code>START</code> - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start.</p> </li> <li> <p> <code>COMPLETE</code> - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. This condition can't be set on an essential container.</p> </li> <li> <p> <code>SUCCESS</code> - This condition is the same as <code>COMPLETE</code>, but it also requires that the container exits with a <code>zero</code> status. This condition can't be set on an essential container.</p> </li> <li> <p> <code>HEALTHY</code> - This condition validates that the dependent container passes its Docker health check before permitting other containers to start. This requires that the dependent container has health checks configured. This condition is confirmed only at task startup.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDependency) -> dict:
    out: dict = {}
    out["containerName"] = value["container_name"]
    import capo_ecs.types.container_condition

    out["condition"] = capo_ecs.types.container_condition.serialize_aws_json_1_1(
        value["condition"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerDependency:
    out: ContainerDependency = {}  # type: ignore[typeddict-item]
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    else:
        out["container_name"] = ""
    if data.get("condition") is not None:
        import capo_ecs.types.container_condition

        out["condition"] = capo_ecs.types.container_condition.deserialize_aws_json_1_1(
            data["condition"]
        )
    else:
        import typing

        out["condition"] = typing.cast(
            "capo_ecs.types.container_condition.ContainerCondition", ""
        )
    return out
