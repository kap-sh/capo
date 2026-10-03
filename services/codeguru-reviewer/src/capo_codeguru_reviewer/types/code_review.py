"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#CodeReview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.analysis_types
    import capo_codeguru_reviewer.types.arn
    import capo_codeguru_reviewer.types.association_arn
    import capo_codeguru_reviewer.types.config_file_state
    import capo_codeguru_reviewer.types.job_state
    import capo_codeguru_reviewer.types.metrics
    import capo_codeguru_reviewer.types.name
    import capo_codeguru_reviewer.types.owner
    import capo_codeguru_reviewer.types.provider_type
    import capo_codeguru_reviewer.types.pull_request_id
    import capo_codeguru_reviewer.types.source_code_type
    import capo_codeguru_reviewer.types.state_reason
    import capo_codeguru_reviewer.types.time_stamp
    import capo_codeguru_reviewer.types.type


class CodeReview(TypedDict, closed=True):
    name: NotRequired["capo_codeguru_reviewer.types.name.Name"]
    """<p>The name of the code review.</p>"""
    code_review_arn: NotRequired["capo_codeguru_reviewer.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>"""
    repository_name: NotRequired["capo_codeguru_reviewer.types.name.Name"]
    """<p>The name of the repository.</p>"""
    owner: NotRequired["capo_codeguru_reviewer.types.owner.Owner"]
    """<p>The owner of the repository. For an Amazon Web Services CodeCommit repository, this is the Amazon Web Services account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or Amazon Web Services account ID.</p>"""
    provider_type: NotRequired[
        "capo_codeguru_reviewer.types.provider_type.ProviderType"
    ]
    """<p>The type of repository that contains the reviewed code (for example, GitHub or Bitbucket).</p>"""
    state: NotRequired["capo_codeguru_reviewer.types.job_state.JobState"]
    """<p>The valid code review states are:</p> <ul> <li> <p> <code>Completed</code>: The code review is complete.</p> </li> <li> <p> <code>Pending</code>: The code review started and has not completed or failed.</p> </li> <li> <p> <code>Failed</code>: The code review failed.</p> </li> <li> <p> <code>Deleting</code>: The code review is being deleted.</p> </li> </ul>"""
    state_reason: NotRequired["capo_codeguru_reviewer.types.state_reason.StateReason"]
    """<p>The reason for the state of the code review.</p>"""
    created_time_stamp: NotRequired["capo_codeguru_reviewer.types.time_stamp.TimeStamp"]
    """<p>The time, in milliseconds since the epoch, when the code review was created.</p>"""
    last_updated_time_stamp: NotRequired[
        "capo_codeguru_reviewer.types.time_stamp.TimeStamp"
    ]
    """<p>The time, in milliseconds since the epoch, when the code review was last updated.</p>"""
    type: NotRequired["capo_codeguru_reviewer.types.type.Type"]
    """<p>The type of code review.</p>"""
    pull_request_id: NotRequired[
        "capo_codeguru_reviewer.types.pull_request_id.PullRequestId"
    ]
    """<p>The pull request ID for the code review.</p>"""
    source_code_type: NotRequired[
        "capo_codeguru_reviewer.types.source_code_type.SourceCodeType"
    ]
    """<p>The type of the source code for the code review.</p>"""
    association_arn: NotRequired[
        "capo_codeguru_reviewer.types.association_arn.AssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> that contains the reviewed source code. You can retrieve associated repository ARNs by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p>"""
    metrics: NotRequired["capo_codeguru_reviewer.types.metrics.Metrics"]
    """<p>The statistics from the code review.</p>"""
    analysis_types: NotRequired[
        "capo_codeguru_reviewer.types.analysis_types.AnalysisTypes"
    ]
    """<p>The types of analysis performed during a repository analysis or a pull request review. You can specify either <code>Security</code>, <code>CodeQuality</code>, or both.</p>"""
    config_file_state: NotRequired[
        "capo_codeguru_reviewer.types.config_file_state.ConfigFileState"
    ]
    """<p>The state of the <code>aws-codeguru-reviewer.yml</code> configuration file that allows the configuration of the CodeGuru Reviewer analysis. The file either exists, doesn't exist, or exists with errors at the root directory of your repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeReview) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "code_review_arn" in value:
        out["CodeReviewArn"] = value["code_review_arn"]
    if "repository_name" in value:
        out["RepositoryName"] = value["repository_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "provider_type" in value:
        import capo_codeguru_reviewer.types.provider_type

        out["ProviderType"] = capo_codeguru_reviewer.types.provider_type.serialize_json(
            value["provider_type"]
        )
    if "state" in value:
        import capo_codeguru_reviewer.types.job_state

        out["State"] = capo_codeguru_reviewer.types.job_state.serialize_json(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "created_time_stamp" in value:
        import capo_codeguru_reviewer.types.time_stamp

        out["CreatedTimeStamp"] = (
            capo_codeguru_reviewer.types.time_stamp.serialize_json(
                value["created_time_stamp"]
            )
        )
    if "last_updated_time_stamp" in value:
        import capo_codeguru_reviewer.types.time_stamp

        out["LastUpdatedTimeStamp"] = (
            capo_codeguru_reviewer.types.time_stamp.serialize_json(
                value["last_updated_time_stamp"]
            )
        )
    if "type" in value:
        import capo_codeguru_reviewer.types.type

        out["Type"] = capo_codeguru_reviewer.types.type.serialize_json(value["type"])
    if "pull_request_id" in value:
        out["PullRequestId"] = value["pull_request_id"]
    if "source_code_type" in value:
        import capo_codeguru_reviewer.types.source_code_type

        out["SourceCodeType"] = (
            capo_codeguru_reviewer.types.source_code_type.serialize_json(
                value["source_code_type"]
            )
        )
    if "association_arn" in value:
        out["AssociationArn"] = value["association_arn"]
    if "metrics" in value:
        import capo_codeguru_reviewer.types.metrics

        out["Metrics"] = capo_codeguru_reviewer.types.metrics.serialize_json(
            value["metrics"]
        )
    if "analysis_types" in value:
        import capo_codeguru_reviewer.types.analysis_types

        out["AnalysisTypes"] = (
            capo_codeguru_reviewer.types.analysis_types.serialize_json(
                value["analysis_types"]
            )
        )
    if "config_file_state" in value:
        import capo_codeguru_reviewer.types.config_file_state

        out["ConfigFileState"] = (
            capo_codeguru_reviewer.types.config_file_state.serialize_json(
                value["config_file_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeReview:
    out: CodeReview = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CodeReviewArn") is not None:
        out["code_review_arn"] = data["CodeReviewArn"]
    if data.get("RepositoryName") is not None:
        out["repository_name"] = data["RepositoryName"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("ProviderType") is not None:
        import capo_codeguru_reviewer.types.provider_type

        out["provider_type"] = (
            capo_codeguru_reviewer.types.provider_type.deserialize_json(
                data["ProviderType"]
            )
        )
    if data.get("State") is not None:
        import capo_codeguru_reviewer.types.job_state

        out["state"] = capo_codeguru_reviewer.types.job_state.deserialize_json(
            data["State"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("CreatedTimeStamp") is not None:
        import capo_codeguru_reviewer.types.time_stamp

        out["created_time_stamp"] = (
            capo_codeguru_reviewer.types.time_stamp.deserialize_json(
                data["CreatedTimeStamp"]
            )
        )
    if data.get("LastUpdatedTimeStamp") is not None:
        import capo_codeguru_reviewer.types.time_stamp

        out["last_updated_time_stamp"] = (
            capo_codeguru_reviewer.types.time_stamp.deserialize_json(
                data["LastUpdatedTimeStamp"]
            )
        )
    if data.get("Type") is not None:
        import capo_codeguru_reviewer.types.type

        out["type"] = capo_codeguru_reviewer.types.type.deserialize_json(data["Type"])
    if data.get("PullRequestId") is not None:
        out["pull_request_id"] = data["PullRequestId"]
    if data.get("SourceCodeType") is not None:
        import capo_codeguru_reviewer.types.source_code_type

        out["source_code_type"] = (
            capo_codeguru_reviewer.types.source_code_type.deserialize_json(
                data["SourceCodeType"]
            )
        )
    if data.get("AssociationArn") is not None:
        out["association_arn"] = data["AssociationArn"]
    if data.get("Metrics") is not None:
        import capo_codeguru_reviewer.types.metrics

        out["metrics"] = capo_codeguru_reviewer.types.metrics.deserialize_json(
            data["Metrics"]
        )
    if data.get("AnalysisTypes") is not None:
        import capo_codeguru_reviewer.types.analysis_types

        out["analysis_types"] = (
            capo_codeguru_reviewer.types.analysis_types.deserialize_json(
                data["AnalysisTypes"]
            )
        )
    if data.get("ConfigFileState") is not None:
        import capo_codeguru_reviewer.types.config_file_state

        out["config_file_state"] = (
            capo_codeguru_reviewer.types.config_file_state.deserialize_json(
                data["ConfigFileState"]
            )
        )
    return out
