"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplyEnvironmentManagedActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.string


class ApplyEnvironmentManagedActionRequest(TypedDict, closed=True):
    environment_name: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The name of the target environment.</p>"""
    environment_id: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The environment ID of the target environment.</p>"""
    action_id: "capo_elastic_beanstalk.types.string.String"
    """<p>The action ID of the scheduled managed action to execute.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplyEnvironmentManagedActionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    if "environment_id" in value:
        pairs.append((f"{key_prefix}EnvironmentId", str(value["environment_id"])))
    pairs.append((f"{key_prefix}ActionId", str(value["action_id"])))


def deserialize_query(el: Element) -> ApplyEnvironmentManagedActionRequest:
    out: ApplyEnvironmentManagedActionRequest = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_action_id = el.find("ActionId")
    if child_action_id is not None:
        out["action_id"] = str(child_action_id.text or "")
    else:
        out["action_id"] = ""
    return out
