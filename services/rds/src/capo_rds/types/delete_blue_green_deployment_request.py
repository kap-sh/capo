"""Generated from Smithy shape ``com.amazonaws.rds#DeleteBlueGreenDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.blue_green_deployment_identifier
    import capo_rds.types.boolean_optional


class DeleteBlueGreenDeploymentRequest(TypedDict, closed=True):
    blue_green_deployment_identifier: NotRequired[
        "capo_rds.types.blue_green_deployment_identifier.BlueGreenDeploymentIdentifier"
    ]
    """<p>The unique identifier of the blue/green deployment to delete. This parameter isn't case-sensitive.</p> <p>Constraints: </p> <ul> <li> <p>Must match an existing blue/green deployment identifier.</p> </li> </ul>"""
    delete_target: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to delete the resources in the green environment. You can't specify this option if the blue/green deployment <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_BlueGreenDeployment.html">status</a> is <code>SWITCHOVER_COMPLETED</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteBlueGreenDeploymentRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "blue_green_deployment_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}BlueGreenDeploymentIdentifier",
                str(value["blue_green_deployment_identifier"]),
            )
        )
    if "delete_target" in value:
        pairs.append(
            (f"{key_prefix}DeleteTarget", "true" if value["delete_target"] else "false")
        )


def deserialize_query(el: Element) -> DeleteBlueGreenDeploymentRequest:
    out: DeleteBlueGreenDeploymentRequest = {}  # type: ignore[typeddict-item]
    child_blue_green_deployment_identifier = el.find("BlueGreenDeploymentIdentifier")
    if child_blue_green_deployment_identifier is not None:
        out["blue_green_deployment_identifier"] = str(
            child_blue_green_deployment_identifier.text or ""
        )
    child_delete_target = el.find("DeleteTarget")
    if child_delete_target is not None:
        out["delete_target"] = (child_delete_target.text or "").lower() == "true"
    return out
