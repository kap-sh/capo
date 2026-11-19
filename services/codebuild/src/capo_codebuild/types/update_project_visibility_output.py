"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateProjectVisibilityOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.project_visibility_type


class UpdateProjectVisibilityOutput(TypedDict, closed=True):
    project_arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the build project.</p>"""
    public_project_alias: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>Contains the project identifier used with the public build APIs. </p>"""
    project_visibility: NotRequired[
        "capo_codebuild.types.project_visibility_type.ProjectVisibilityType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectVisibilityOutput) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["projectArn"] = value["project_arn"]
    if "public_project_alias" in value:
        out["publicProjectAlias"] = value["public_project_alias"]
    if "project_visibility" in value:
        import capo_codebuild.types.project_visibility_type

        out["projectVisibility"] = (
            capo_codebuild.types.project_visibility_type.serialize_aws_json_1_1(
                value["project_visibility"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectVisibilityOutput:
    out: UpdateProjectVisibilityOutput = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    if data.get("publicProjectAlias") is not None:
        out["public_project_alias"] = data["publicProjectAlias"]
    if data.get("projectVisibility") is not None:
        import capo_codebuild.types.project_visibility_type

        out["project_visibility"] = (
            capo_codebuild.types.project_visibility_type.deserialize_aws_json_1_1(
                data["projectVisibility"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateProjectVisibilityOutput) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["projectArn"] = value["project_arn"]
    if "public_project_alias" in value:
        out["publicProjectAlias"] = value["public_project_alias"]
    if "project_visibility" in value:
        import capo_codebuild.types.project_visibility_type

        out["projectVisibility"] = (
            capo_codebuild.types.project_visibility_type.serialize_cbor(
                value["project_visibility"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateProjectVisibilityOutput:
    out: UpdateProjectVisibilityOutput = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    if data.get("publicProjectAlias") is not None:
        out["public_project_alias"] = data["publicProjectAlias"]
    if data.get("projectVisibility") is not None:
        import capo_codebuild.types.project_visibility_type

        out["project_visibility"] = (
            capo_codebuild.types.project_visibility_type.deserialize_cbor(
                data["projectVisibility"]
            )
        )
    return out
