"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.rule_execution
    import capo_codepipeline.types.rule_name
    import capo_codepipeline.types.rule_revision
    import capo_codepipeline.types.url


class RuleState(TypedDict, closed=True):
    rule_name: NotRequired["capo_codepipeline.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    current_revision: NotRequired["capo_codepipeline.types.rule_revision.RuleRevision"]
    """<p>The ID of the current revision of the artifact successfully worked on by the job.</p>"""
    latest_execution: NotRequired[
        "capo_codepipeline.types.rule_execution.RuleExecution"
    ]
    """<p>Represents information about the latest run of an rule.</p>"""
    entity_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>A URL link for more information about the state of the action, such as a details page.</p>"""
    revision_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>A URL link for more information about the revision, such as a commit details page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleState) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["ruleName"] = value["rule_name"]
    if "current_revision" in value:
        import capo_codepipeline.types.rule_revision

        out["currentRevision"] = (
            capo_codepipeline.types.rule_revision.serialize_aws_json_1_1(
                value["current_revision"]
            )
        )
    if "latest_execution" in value:
        import capo_codepipeline.types.rule_execution

        out["latestExecution"] = (
            capo_codepipeline.types.rule_execution.serialize_aws_json_1_1(
                value["latest_execution"]
            )
        )
    if "entity_url" in value:
        out["entityUrl"] = value["entity_url"]
    if "revision_url" in value:
        out["revisionUrl"] = value["revision_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleState:
    out: RuleState = {}  # type: ignore[typeddict-item]
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
    if data.get("currentRevision") is not None:
        import capo_codepipeline.types.rule_revision

        out["current_revision"] = (
            capo_codepipeline.types.rule_revision.deserialize_aws_json_1_1(
                data["currentRevision"]
            )
        )
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.rule_execution

        out["latest_execution"] = (
            capo_codepipeline.types.rule_execution.deserialize_aws_json_1_1(
                data["latestExecution"]
            )
        )
    if data.get("entityUrl") is not None:
        out["entity_url"] = data["entityUrl"]
    if data.get("revisionUrl") is not None:
        out["revision_url"] = data["revisionUrl"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleState) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["ruleName"] = value["rule_name"]
    if "current_revision" in value:
        import capo_codepipeline.types.rule_revision

        out["currentRevision"] = capo_codepipeline.types.rule_revision.serialize_cbor(
            value["current_revision"]
        )
    if "latest_execution" in value:
        import capo_codepipeline.types.rule_execution

        out["latestExecution"] = capo_codepipeline.types.rule_execution.serialize_cbor(
            value["latest_execution"]
        )
    if "entity_url" in value:
        out["entityUrl"] = value["entity_url"]
    if "revision_url" in value:
        out["revisionUrl"] = value["revision_url"]
    return out


def deserialize_cbor(data: dict) -> RuleState:
    out: RuleState = {}  # type: ignore[typeddict-item]
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
    if data.get("currentRevision") is not None:
        import capo_codepipeline.types.rule_revision

        out["current_revision"] = (
            capo_codepipeline.types.rule_revision.deserialize_cbor(
                data["currentRevision"]
            )
        )
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.rule_execution

        out["latest_execution"] = (
            capo_codepipeline.types.rule_execution.deserialize_cbor(
                data["latestExecution"]
            )
        )
    if data.get("entityUrl") is not None:
        out["entity_url"] = data["entityUrl"]
    if data.get("revisionUrl") is not None:
        out["revision_url"] = data["revisionUrl"]
    return out
