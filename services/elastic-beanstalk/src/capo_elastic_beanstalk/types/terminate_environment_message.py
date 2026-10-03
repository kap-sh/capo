"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#TerminateEnvironmentMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_id
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.force_terminate
    import capo_elastic_beanstalk.types.terminate_environment_resources


class TerminateEnvironmentMessage(TypedDict, closed=True):
    environment_id: NotRequired[
        "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment to terminate.</p> <p> Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>"""
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment to terminate.</p> <p> Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>"""
    terminate_resources: NotRequired[
        "capo_elastic_beanstalk.types.terminate_environment_resources.TerminateEnvironmentResources"
    ]
    """<p>Indicates whether the associated Amazon Web Services resources should shut down when the environment is terminated:</p> <ul> <li> <p> <code>true</code>: The specified environment as well as the associated Amazon Web Services resources, such as Auto Scaling group and LoadBalancer, are terminated.</p> </li> <li> <p> <code>false</code>: Elastic Beanstalk resource management is removed from the environment, but the Amazon Web Services resources continue to operate.</p> </li> </ul> <p> For more information, see the <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/ug/"> Elastic Beanstalk User Guide. </a> </p> <p> Default: <code>true</code> </p> <p> Valid Values: <code>true</code> | <code>false</code> </p>"""
    force_terminate: NotRequired[
        "capo_elastic_beanstalk.types.force_terminate.ForceTerminate"
    ]
    """<p>Terminates the target environment even if another environment in the same group is dependent on it.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TerminateEnvironmentMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "environment_id" in value:
        pairs.append((f"{key_prefix}EnvironmentId", str(value["environment_id"])))
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    if "terminate_resources" in value:
        pairs.append(
            (
                f"{key_prefix}TerminateResources",
                "true" if value["terminate_resources"] else "false",
            )
        )
    if "force_terminate" in value:
        pairs.append(
            (
                f"{key_prefix}ForceTerminate",
                "true" if value["force_terminate"] else "false",
            )
        )


def deserialize_query(el: Element) -> TerminateEnvironmentMessage:
    out: TerminateEnvironmentMessage = {}  # type: ignore[typeddict-item]
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_terminate_resources = el.find("TerminateResources")
    if child_terminate_resources is not None:
        out["terminate_resources"] = (
            child_terminate_resources.text or ""
        ).lower() == "true"
    child_force_terminate = el.find("ForceTerminate")
    if child_force_terminate is not None:
        out["force_terminate"] = (child_force_terminate.text or "").lower() == "true"
    return out
