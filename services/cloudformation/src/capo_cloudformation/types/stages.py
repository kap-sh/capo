"""Generated from Smithy shape ``com.amazonaws.cloudformation#Stages``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.role_provisioning
    import capo_cloudformation.types.stack_instances_deployment


class Stages(TypedDict, closed=True):
    role_provisioning: NotRequired[
        "capo_cloudformation.types.role_provisioning.RoleProvisioning"
    ]
    """<p>The progress detail for the role provisioning stage. For operations that do not provision roles, this stage is present with a <code>Status</code> of <code>NOT_APPLICABLE</code>.</p>"""
    stack_instances_deployment: NotRequired[
        "capo_cloudformation.types.stack_instances_deployment.StackInstancesDeployment"
    ]
    """<p>The progress detail for the stack instances deployment stage. This stage reports the deployment of stack instances to the target accounts and Amazon Web Services Regions, after any role provisioning has finished.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Stages, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "role_provisioning" in value:
        import capo_cloudformation.types.role_provisioning

        capo_cloudformation.types.role_provisioning.serialize_query(
            value["role_provisioning"], pairs, f"{key_prefix}RoleProvisioning"
        )
    if "stack_instances_deployment" in value:
        import capo_cloudformation.types.stack_instances_deployment

        capo_cloudformation.types.stack_instances_deployment.serialize_query(
            value["stack_instances_deployment"],
            pairs,
            f"{key_prefix}StackInstancesDeployment",
        )


def deserialize_query(el: Element) -> Stages:
    out: Stages = {}  # type: ignore[typeddict-item]
    child_role_provisioning = el.find("RoleProvisioning")
    if child_role_provisioning is not None:
        import capo_cloudformation.types.role_provisioning

        out["role_provisioning"] = (
            capo_cloudformation.types.role_provisioning.deserialize_query(
                child_role_provisioning
            )
        )
    child_stack_instances_deployment = el.find("StackInstancesDeployment")
    if child_stack_instances_deployment is not None:
        import capo_cloudformation.types.stack_instances_deployment

        out["stack_instances_deployment"] = (
            capo_cloudformation.types.stack_instances_deployment.deserialize_query(
                child_stack_instances_deployment
            )
        )
    return out
