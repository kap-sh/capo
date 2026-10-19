"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#AssociateEnvironmentOperationsRoleMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.operations_role


class AssociateEnvironmentOperationsRoleMessage(TypedDict, closed=True):
    environment_name: "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    """<p>The name of the environment to which to set the operations role.</p>"""
    operations_role: "capo_elastic_beanstalk.types.operations_role.OperationsRole"
    """<p>The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AssociateEnvironmentOperationsRoleMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    pairs.append((f"{key_prefix}OperationsRole", str(value["operations_role"])))


def deserialize_query(el: Element) -> AssociateEnvironmentOperationsRoleMessage:
    out: AssociateEnvironmentOperationsRoleMessage = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    else:
        out["environment_name"] = ""
    child_operations_role = el.find("OperationsRole")
    if child_operations_role is not None:
        out["operations_role"] = str(child_operations_role.text or "")
    else:
        out["operations_role"] = ""
    return out
