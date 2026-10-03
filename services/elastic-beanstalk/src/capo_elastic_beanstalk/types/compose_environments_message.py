"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ComposeEnvironmentsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.group_name
    import capo_elastic_beanstalk.types.version_labels


class ComposeEnvironmentsMessage(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The name of the application to which the specified source bundles belong.</p>"""
    group_name: NotRequired["capo_elastic_beanstalk.types.group_name.GroupName"]
    """<p>The name of the group to which the target environments belong. Specify a group name only if the environment name defined in each target environment's manifest ends with a + (plus) character. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html">Environment Manifest (env.yaml)</a> for details.</p>"""
    version_labels: NotRequired[
        "capo_elastic_beanstalk.types.version_labels.VersionLabels"
    ]
    """<p>A list of version labels, specifying one or more application source bundles that belong to the target application. Each source bundle must include an environment manifest that specifies the name of the environment and the name of the solution stack to use, and optionally can specify environment links to create.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ComposeEnvironmentsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_name" in value:
        pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "version_labels" in value:
        import capo_elastic_beanstalk.types.version_labels

        capo_elastic_beanstalk.types.version_labels.serialize_query(
            value["version_labels"], pairs, f"{key_prefix}VersionLabels"
        )


def deserialize_query(el: Element) -> ComposeEnvironmentsMessage:
    out: ComposeEnvironmentsMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_version_labels = el.find("VersionLabels")
    if child_version_labels is not None:
        import capo_elastic_beanstalk.types.version_labels

        out["version_labels"] = (
            capo_elastic_beanstalk.types.version_labels.deserialize_query(
                child_version_labels
            )
        )
    return out
