"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteBuildBatchOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_ids
    import capo_codebuild.types.builds_not_deleted
    import capo_codebuild.types.string


class DeleteBuildBatchOutput(TypedDict, closed=True):
    status_code: NotRequired["capo_codebuild.types.string.String"]
    """<p>The status code.</p>"""
    builds_deleted: NotRequired["capo_codebuild.types.build_ids.BuildIds"]
    """<p>An array of strings that contain the identifiers of the builds that were deleted.</p>"""
    builds_not_deleted: NotRequired[
        "capo_codebuild.types.builds_not_deleted.BuildsNotDeleted"
    ]
    """<p>An array of <code>BuildNotDeleted</code> objects that specify the builds that could not be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBuildBatchOutput) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "builds_deleted" in value:
        import capo_codebuild.types.build_ids

        out["buildsDeleted"] = capo_codebuild.types.build_ids.serialize_aws_json_1_1(
            value["builds_deleted"]
        )
    if "builds_not_deleted" in value:
        import capo_codebuild.types.builds_not_deleted

        out["buildsNotDeleted"] = (
            capo_codebuild.types.builds_not_deleted.serialize_aws_json_1_1(
                value["builds_not_deleted"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBuildBatchOutput:
    out: DeleteBuildBatchOutput = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    if data.get("buildsDeleted") is not None:
        import capo_codebuild.types.build_ids

        out["builds_deleted"] = capo_codebuild.types.build_ids.deserialize_aws_json_1_1(
            data["buildsDeleted"]
        )
    if data.get("buildsNotDeleted") is not None:
        import capo_codebuild.types.builds_not_deleted

        out["builds_not_deleted"] = (
            capo_codebuild.types.builds_not_deleted.deserialize_aws_json_1_1(
                data["buildsNotDeleted"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteBuildBatchOutput) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "builds_deleted" in value:
        import capo_codebuild.types.build_ids

        out["buildsDeleted"] = capo_codebuild.types.build_ids.serialize_cbor(
            value["builds_deleted"]
        )
    if "builds_not_deleted" in value:
        import capo_codebuild.types.builds_not_deleted

        out["buildsNotDeleted"] = (
            capo_codebuild.types.builds_not_deleted.serialize_cbor(
                value["builds_not_deleted"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeleteBuildBatchOutput:
    out: DeleteBuildBatchOutput = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    if data.get("buildsDeleted") is not None:
        import capo_codebuild.types.build_ids

        out["builds_deleted"] = capo_codebuild.types.build_ids.deserialize_cbor(
            data["buildsDeleted"]
        )
    if data.get("buildsNotDeleted") is not None:
        import capo_codebuild.types.builds_not_deleted

        out["builds_not_deleted"] = (
            capo_codebuild.types.builds_not_deleted.deserialize_cbor(
                data["buildsNotDeleted"]
            )
        )
    return out
