"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DisassociateEnvironmentOperationsRoleMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_name


class DisassociateEnvironmentOperationsRoleMessage(TypedDict, closed=True):
    environment_name: "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    """<p>The name of the environment from which to disassociate the operations role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DisassociateEnvironmentOperationsRoleMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))


def deserialize_query(el: Element) -> DisassociateEnvironmentOperationsRoleMessage:
    out: DisassociateEnvironmentOperationsRoleMessage = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    else:
        out["environment_name"] = ""
    return out
