"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.action_failure_policy
    import capo_mailmanager.types.name_or_arn


class ArchiveAction(TypedDict, closed=True):
    action_failure_policy: NotRequired[
        "capo_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified archive has been deleted.</p>"""
    target_archive: "capo_mailmanager.types.name_or_arn.NameOrArn"
    """<p>The identifier of the archive to send the email to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import capo_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            capo_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["TargetArchive"] = value["target_archive"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ArchiveAction:
    out: ArchiveAction = {}  # type: ignore[typeddict-item]
    if data.get("ActionFailurePolicy") is not None:
        import capo_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            capo_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if data.get("TargetArchive") is not None:
        out["target_archive"] = data["TargetArchive"]
    else:
        out["target_archive"] = ""
    return out
