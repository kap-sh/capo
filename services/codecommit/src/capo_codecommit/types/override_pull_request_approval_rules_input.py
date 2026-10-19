"""Generated from Smithy shape ``com.amazonaws.codecommit#OverridePullRequestApprovalRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.override_status
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.revision_id


class OverridePullRequestApprovalRulesInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request for which you want to override all approval rule requirements. To get this information, use <a>GetPullRequest</a>.</p>"""
    revision_id: "capo_codecommit.types.revision_id.RevisionId"
    """<p>The system-generated ID of the most recent revision of the pull request. You cannot override approval rules for anything but the most recent revision of a pull request. To get the revision ID, use GetPullRequest.</p>"""
    override_status: "capo_codecommit.types.override_status.OverrideStatus"
    """<p>Whether you want to set aside approval rule requirements for the pull request (OVERRIDE) or revoke a previous override and apply approval rule requirements (REVOKE). REVOKE status is not stored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverridePullRequestApprovalRulesInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["revisionId"] = value["revision_id"]
    import capo_codecommit.types.override_status

    out["overrideStatus"] = (
        capo_codecommit.types.override_status.serialize_aws_json_1_1(
            value["override_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OverridePullRequestApprovalRulesInput:
    out: OverridePullRequestApprovalRulesInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    if data.get("overrideStatus") is not None:
        import capo_codecommit.types.override_status

        out["override_status"] = (
            capo_codecommit.types.override_status.deserialize_aws_json_1_1(
                data["overrideStatus"]
            )
        )
    else:
        import typing

        out["override_status"] = typing.cast(
            "capo_codecommit.types.override_status.OverrideStatus", ""
        )
    return out
