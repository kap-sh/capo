"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeUrls``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.url
    import capo_codepipeline.types.url_template


class ActionTypeUrls(TypedDict, closed=True):
    configuration_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>The URL returned to the CodePipeline console that contains a link to the page where customers can configure the external action.</p>"""
    entity_url_template: NotRequired["capo_codepipeline.types.url_template.UrlTemplate"]
    """<p>The URL returned to the CodePipeline console that provides a deep link to the resources of the external system, such as a status page. This link is provided as part of the action display in the pipeline.</p>"""
    execution_url_template: NotRequired[
        "capo_codepipeline.types.url_template.UrlTemplate"
    ]
    """<p>The link to an execution page for the action type in progress. For example, for a CodeDeploy action, this link is shown on the pipeline view page in the CodePipeline console, and it links to a CodeDeploy status page.</p>"""
    revision_url_template: NotRequired[
        "capo_codepipeline.types.url_template.UrlTemplate"
    ]
    """<p>The URL returned to the CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeUrls) -> dict:
    out: dict = {}
    if "configuration_url" in value:
        out["configurationUrl"] = value["configuration_url"]
    if "entity_url_template" in value:
        out["entityUrlTemplate"] = value["entity_url_template"]
    if "execution_url_template" in value:
        out["executionUrlTemplate"] = value["execution_url_template"]
    if "revision_url_template" in value:
        out["revisionUrlTemplate"] = value["revision_url_template"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypeUrls:
    out: ActionTypeUrls = {}  # type: ignore[typeddict-item]
    if data.get("configurationUrl") is not None:
        out["configuration_url"] = data["configurationUrl"]
    if data.get("entityUrlTemplate") is not None:
        out["entity_url_template"] = data["entityUrlTemplate"]
    if data.get("executionUrlTemplate") is not None:
        out["execution_url_template"] = data["executionUrlTemplate"]
    if data.get("revisionUrlTemplate") is not None:
        out["revision_url_template"] = data["revisionUrlTemplate"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionTypeUrls) -> dict:
    out: dict = {}
    if "configuration_url" in value:
        out["configurationUrl"] = value["configuration_url"]
    if "entity_url_template" in value:
        out["entityUrlTemplate"] = value["entity_url_template"]
    if "execution_url_template" in value:
        out["executionUrlTemplate"] = value["execution_url_template"]
    if "revision_url_template" in value:
        out["revisionUrlTemplate"] = value["revision_url_template"]
    return out


def deserialize_cbor(data: dict) -> ActionTypeUrls:
    out: ActionTypeUrls = {}  # type: ignore[typeddict-item]
    if data.get("configurationUrl") is not None:
        out["configuration_url"] = data["configurationUrl"]
    if data.get("entityUrlTemplate") is not None:
        out["entity_url_template"] = data["entityUrlTemplate"]
    if data.get("executionUrlTemplate") is not None:
        out["execution_url_template"] = data["executionUrlTemplate"]
    if data.get("revisionUrlTemplate") is not None:
        out["revision_url_template"] = data["revisionUrlTemplate"]
    return out
