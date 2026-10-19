"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeleteEnvironmentConfigurationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.environment_name


class DeleteEnvironmentConfigurationMessage(TypedDict, closed=True):
    application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application the environment is associated with.</p>"""
    environment_name: "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    """<p>The name of the environment to delete the draft configuration from.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteEnvironmentConfigurationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))


def deserialize_query(el: Element) -> DeleteEnvironmentConfigurationMessage:
    out: DeleteEnvironmentConfigurationMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        out["application_name"] = ""
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    else:
        out["environment_name"] = ""
    return out
