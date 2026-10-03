"""Generated from Smithy shape ``com.amazonaws.qconnect#RenderingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uri


class RenderingConfiguration(TypedDict, closed=True):
    template_uri: NotRequired["capo_qconnect.types.uri.Uri"]
    """<p>A URI template containing exactly one variable in <code>${variableName} </code>format. This can only be set for <code>EXTERNAL</code> knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following:</p> <ul> <li> <p>Salesforce: <code>Id</code>, <code>ArticleNumber</code>, <code>VersionNumber</code>, <code>Title</code>, <code>PublishStatus</code>, or <code>IsDeleted</code> </p> </li> <li> <p>ServiceNow: <code>number</code>, <code>short_description</code>, <code>sys_mod_count</code>, <code>workflow_state</code>, or <code>active</code> </p> </li> <li> <p>Zendesk: <code>id</code>, <code>title</code>, <code>updated_at</code>, or <code>draft</code> </p> </li> </ul> <p>The variable is replaced with the actual value for a piece of content when calling <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetContent.html">GetContent</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenderingConfiguration) -> dict:
    out: dict = {}
    if "template_uri" in value:
        out["templateUri"] = value["template_uri"]
    return out


def deserialize_json(data: dict) -> RenderingConfiguration:
    out: RenderingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("templateUri") is not None:
        out["template_uri"] = data["templateUri"]
    return out
