"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.action_revision
    import capo_codepipeline.types.url


class ActionState(TypedDict, closed=True):
    action_name: NotRequired["capo_codepipeline.types.action_name.ActionName"]
    """<p>The name of the action.</p>"""
    current_revision: NotRequired[
        "capo_codepipeline.types.action_revision.ActionRevision"
    ]
    """<p>Represents information about the version (or revision) of an action.</p>"""
    latest_execution: NotRequired[
        "capo_codepipeline.types.action_execution.ActionExecution"
    ]
    """<p>Represents information about the run of an action.</p>"""
    entity_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>A URL link for more information about the state of the action, such as a deployment group details page.</p>"""
    revision_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>A URL link for more information about the revision, such as a commit details page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionState) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "current_revision" in value:
        import capo_codepipeline.types.action_revision

        out["currentRevision"] = (
            capo_codepipeline.types.action_revision.serialize_aws_json_1_1(
                value["current_revision"]
            )
        )
    if "latest_execution" in value:
        import capo_codepipeline.types.action_execution

        out["latestExecution"] = (
            capo_codepipeline.types.action_execution.serialize_aws_json_1_1(
                value["latest_execution"]
            )
        )
    if "entity_url" in value:
        out["entityUrl"] = value["entity_url"]
    if "revision_url" in value:
        out["revisionUrl"] = value["revision_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionState:
    out: ActionState = {}  # type: ignore[typeddict-item]
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    if data.get("currentRevision") is not None:
        import capo_codepipeline.types.action_revision

        out["current_revision"] = (
            capo_codepipeline.types.action_revision.deserialize_aws_json_1_1(
                data["currentRevision"]
            )
        )
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.action_execution

        out["latest_execution"] = (
            capo_codepipeline.types.action_execution.deserialize_aws_json_1_1(
                data["latestExecution"]
            )
        )
    if data.get("entityUrl") is not None:
        out["entity_url"] = data["entityUrl"]
    if data.get("revisionUrl") is not None:
        out["revision_url"] = data["revisionUrl"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionState) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "current_revision" in value:
        import capo_codepipeline.types.action_revision

        out["currentRevision"] = capo_codepipeline.types.action_revision.serialize_cbor(
            value["current_revision"]
        )
    if "latest_execution" in value:
        import capo_codepipeline.types.action_execution

        out["latestExecution"] = (
            capo_codepipeline.types.action_execution.serialize_cbor(
                value["latest_execution"]
            )
        )
    if "entity_url" in value:
        out["entityUrl"] = value["entity_url"]
    if "revision_url" in value:
        out["revisionUrl"] = value["revision_url"]
    return out


def deserialize_cbor(data: dict) -> ActionState:
    out: ActionState = {}  # type: ignore[typeddict-item]
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    if data.get("currentRevision") is not None:
        import capo_codepipeline.types.action_revision

        out["current_revision"] = (
            capo_codepipeline.types.action_revision.deserialize_cbor(
                data["currentRevision"]
            )
        )
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.action_execution

        out["latest_execution"] = (
            capo_codepipeline.types.action_execution.deserialize_cbor(
                data["latestExecution"]
            )
        )
    if data.get("entityUrl") is not None:
        out["entity_url"] = data["entityUrl"]
    if data.get("revisionUrl") is not None:
        out["revision_url"] = data["revisionUrl"]
    return out
