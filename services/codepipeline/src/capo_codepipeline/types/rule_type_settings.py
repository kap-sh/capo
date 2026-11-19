"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleTypeSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.url
    import capo_codepipeline.types.url_template


class RuleTypeSettings(TypedDict, closed=True):
    third_party_configuration_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.</p>"""
    entity_url_template: NotRequired["capo_codepipeline.types.url_template.UrlTemplate"]
    """<p>The URL returned to the CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for a CodeDeploy deployment group. This link is provided as part of the action display in the pipeline.</p>"""
    execution_url_template: NotRequired[
        "capo_codepipeline.types.url_template.UrlTemplate"
    ]
    """<p>The URL returned to the CodePipeline console that contains a link to the top-level landing page for the external system, such as the console page for CodeDeploy. This link is shown on the pipeline view page in the CodePipeline console and provides a link to the execution entity of the external action.</p>"""
    revision_url_template: NotRequired[
        "capo_codepipeline.types.url_template.UrlTemplate"
    ]
    """<p>The URL returned to the CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleTypeSettings) -> dict:
    out: dict = {}
    if "third_party_configuration_url" in value:
        out["thirdPartyConfigurationUrl"] = value["third_party_configuration_url"]
    if "entity_url_template" in value:
        out["entityUrlTemplate"] = value["entity_url_template"]
    if "execution_url_template" in value:
        out["executionUrlTemplate"] = value["execution_url_template"]
    if "revision_url_template" in value:
        out["revisionUrlTemplate"] = value["revision_url_template"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleTypeSettings:
    out: RuleTypeSettings = {}  # type: ignore[typeddict-item]
    if data.get("thirdPartyConfigurationUrl") is not None:
        out["third_party_configuration_url"] = data["thirdPartyConfigurationUrl"]
    if data.get("entityUrlTemplate") is not None:
        out["entity_url_template"] = data["entityUrlTemplate"]
    if data.get("executionUrlTemplate") is not None:
        out["execution_url_template"] = data["executionUrlTemplate"]
    if data.get("revisionUrlTemplate") is not None:
        out["revision_url_template"] = data["revisionUrlTemplate"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleTypeSettings) -> dict:
    out: dict = {}
    if "third_party_configuration_url" in value:
        out["thirdPartyConfigurationUrl"] = value["third_party_configuration_url"]
    if "entity_url_template" in value:
        out["entityUrlTemplate"] = value["entity_url_template"]
    if "execution_url_template" in value:
        out["executionUrlTemplate"] = value["execution_url_template"]
    if "revision_url_template" in value:
        out["revisionUrlTemplate"] = value["revision_url_template"]
    return out


def deserialize_cbor(data: dict) -> RuleTypeSettings:
    out: RuleTypeSettings = {}  # type: ignore[typeddict-item]
    if data.get("thirdPartyConfigurationUrl") is not None:
        out["third_party_configuration_url"] = data["thirdPartyConfigurationUrl"]
    if data.get("entityUrlTemplate") is not None:
        out["entity_url_template"] = data["entityUrlTemplate"]
    if data.get("executionUrlTemplate") is not None:
        out["execution_url_template"] = data["executionUrlTemplate"]
    if data.get("revisionUrlTemplate") is not None:
        out["revision_url_template"] = data["revisionUrlTemplate"]
    return out
