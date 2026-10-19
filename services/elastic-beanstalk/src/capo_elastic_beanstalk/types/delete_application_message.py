"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeleteApplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.terminate_env_force


class DeleteApplicationMessage(TypedDict, closed=True):
    application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application to delete.</p>"""
    terminate_env_by_force: NotRequired[
        "capo_elastic_beanstalk.types.terminate_env_force.TerminateEnvForce"
    ]
    """<p>When set to true, running environments will be terminated before deleting the application.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteApplicationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    if "terminate_env_by_force" in value:
        pairs.append(
            (
                f"{key_prefix}TerminateEnvByForce",
                "true" if value["terminate_env_by_force"] else "false",
            )
        )


def deserialize_query(el: Element) -> DeleteApplicationMessage:
    out: DeleteApplicationMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        out["application_name"] = ""
    child_terminate_env_by_force = el.find("TerminateEnvByForce")
    if child_terminate_env_by_force is not None:
        out["terminate_env_by_force"] = (
            child_terminate_env_by_force.text or ""
        ).lower() == "true"
    return out
