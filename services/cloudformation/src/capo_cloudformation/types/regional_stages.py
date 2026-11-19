"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegionalStages``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.regional_stack_instances_deployment


class RegionalStages(TypedDict, closed=True):
    regional_stack_instances_deployment: NotRequired[
        "capo_cloudformation.types.regional_stack_instances_deployment.RegionalStackInstancesDeployment"
    ]
    """<p>The progress detail for the stack instances deployment stage in this Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegionalStages, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "regional_stack_instances_deployment" in value:
        import capo_cloudformation.types.regional_stack_instances_deployment

        capo_cloudformation.types.regional_stack_instances_deployment.serialize_query(
            value["regional_stack_instances_deployment"],
            pairs,
            f"{key_prefix}RegionalStackInstancesDeployment",
        )


def deserialize_query(el: Element) -> RegionalStages:
    out: RegionalStages = {}  # type: ignore[typeddict-item]
    child_regional_stack_instances_deployment = el.find(
        "RegionalStackInstancesDeployment"
    )
    if child_regional_stack_instances_deployment is not None:
        import capo_cloudformation.types.regional_stack_instances_deployment

        out["regional_stack_instances_deployment"] = (
            capo_cloudformation.types.regional_stack_instances_deployment.deserialize_query(
                child_regional_stack_instances_deployment
            )
        )
    return out
