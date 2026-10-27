"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationBackfillResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier
    import capo_ecr.types.replication_backfill_result_status
    import capo_ecr.types.replication_error
    import capo_ecr.types.replication_error_list
    import capo_ecr.types.repository_name


class ReplicationBackfillResult(TypedDict, closed=True):
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the image.</p>"""
    image_id: "capo_ecr.types.image_identifier.ImageIdentifier"
    """<p>An object with identifying information for the image.</p>"""
    status: "capo_ecr.types.replication_backfill_result_status.ReplicationBackfillResultStatus"
    """<p>The replication status of the image.</p>"""
    failure_code: NotRequired["capo_ecr.types.replication_error.ReplicationError"]
    """<p>The failure code for a replication that has failed.</p>"""
    sub_image_failure_codes: NotRequired[
        "capo_ecr.types.replication_error_list.ReplicationErrorList"
    ]
    """<p>The distinct failure codes for the images referenced by a manifest list that failed to replicate. Each failure code appears at most once, regardless of how many referenced images failed with that code. This field is present only when the image is a manifest list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationBackfillResult) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    import capo_ecr.types.image_identifier

    out["imageId"] = capo_ecr.types.image_identifier.serialize_aws_json_1_1(
        value["image_id"]
    )
    import capo_ecr.types.replication_backfill_result_status

    out["status"] = (
        capo_ecr.types.replication_backfill_result_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "sub_image_failure_codes" in value:
        import capo_ecr.types.replication_error_list

        out["subImageFailureCodes"] = (
            capo_ecr.types.replication_error_list.serialize_aws_json_1_1(
                value["sub_image_failure_codes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationBackfillResult:
    out: ReplicationBackfillResult = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("imageId") is not None:
        import capo_ecr.types.image_identifier

        out["image_id"] = capo_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    else:
        raise DeserializationError("ReplicationBackfillResult.image_id required")
    if data.get("status") is not None:
        import capo_ecr.types.replication_backfill_result_status

        out["status"] = (
            capo_ecr.types.replication_backfill_result_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_ecr.types.replication_backfill_result_status.ReplicationBackfillResultStatus",
            "",
        )
    if data.get("failureCode") is not None:
        out["failure_code"] = data["failureCode"]
    if data.get("subImageFailureCodes") is not None:
        import capo_ecr.types.replication_error_list

        out["sub_image_failure_codes"] = (
            capo_ecr.types.replication_error_list.deserialize_aws_json_1_1(
                data["subImageFailureCodes"]
            )
        )
    return out
