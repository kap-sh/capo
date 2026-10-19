"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#UpdateApplicationVersionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.version_label


class UpdateApplicationVersionMessage(TypedDict, closed=True):
    application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application associated with this version.</p> <p> If no application is found with this name, <code>UpdateApplication</code> returns an <code>InvalidParameterValue</code> error.</p>"""
    version_label: "capo_elastic_beanstalk.types.version_label.VersionLabel"
    """<p>The name of the version to update.</p> <p>If no application version is found with this label, <code>UpdateApplication</code> returns an <code>InvalidParameterValue</code> error. </p>"""
    description: NotRequired["capo_elastic_beanstalk.types.description.Description"]
    """<p>A new description for this version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateApplicationVersionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    pairs.append((f"{key_prefix}VersionLabel", str(value["version_label"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_query(el: Element) -> UpdateApplicationVersionMessage:
    out: UpdateApplicationVersionMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        out["application_name"] = ""
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    else:
        out["version_label"] = ""
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
