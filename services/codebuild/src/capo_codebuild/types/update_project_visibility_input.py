"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateProjectVisibilityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.project_visibility_type


class UpdateProjectVisibilityInput(TypedDict, closed=True):
    project_arn: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Resource Name (ARN) of the build project.</p>"""
    project_visibility: (
        "capo_codebuild.types.project_visibility_type.ProjectVisibilityType"
    )
    resource_access_role: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the IAM role that enables CodeBuild to access the CloudWatch Logs and Amazon S3 artifacts for the project's builds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectVisibilityInput) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    import capo_codebuild.types.project_visibility_type

    out["projectVisibility"] = (
        capo_codebuild.types.project_visibility_type.serialize_aws_json_1_1(
            value["project_visibility"]
        )
    )
    if "resource_access_role" in value:
        out["resourceAccessRole"] = value["resource_access_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectVisibilityInput:
    out: UpdateProjectVisibilityInput = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    else:
        out["project_arn"] = ""
    if data.get("projectVisibility") is not None:
        import capo_codebuild.types.project_visibility_type

        out["project_visibility"] = (
            capo_codebuild.types.project_visibility_type.deserialize_aws_json_1_1(
                data["projectVisibility"]
            )
        )
    else:
        import typing

        out["project_visibility"] = typing.cast(
            "capo_codebuild.types.project_visibility_type.ProjectVisibilityType", ""
        )
    if data.get("resourceAccessRole") is not None:
        out["resource_access_role"] = data["resourceAccessRole"]
    return out
