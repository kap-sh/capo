"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.any_length_string
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.flywheel_iteration_id
    import capo_comprehend.types.flywheel_status
    import capo_comprehend.types.model_type
    import capo_comprehend.types.s3_uri
    import capo_comprehend.types.timestamp


class FlywheelSummary(TypedDict, closed=True):
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel</p>"""
    active_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>ARN of the active model version for the flywheel.</p>"""
    data_lake_s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>Amazon S3 URI of the data lake location. </p>"""
    status: NotRequired["capo_comprehend.types.flywheel_status.FlywheelStatus"]
    """<p>The status of the flywheel.</p>"""
    model_type: NotRequired["capo_comprehend.types.model_type.ModelType"]
    """<p>Model type of the flywheel's model.</p>"""
    message: NotRequired["capo_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of the flywheel.</p>"""
    creation_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Creation time of the flywheel.</p>"""
    last_modified_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Last modified time for the flywheel.</p>"""
    latest_flywheel_iteration: NotRequired[
        "capo_comprehend.types.flywheel_iteration_id.FlywheelIterationId"
    ]
    """<p>The most recent flywheel iteration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelSummary) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "active_model_arn" in value:
        out["ActiveModelArn"] = value["active_model_arn"]
    if "data_lake_s3_uri" in value:
        out["DataLakeS3Uri"] = value["data_lake_s3_uri"]
    if "status" in value:
        import capo_comprehend.types.flywheel_status

        out["Status"] = capo_comprehend.types.flywheel_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "model_type" in value:
        import capo_comprehend.types.model_type

        out["ModelType"] = capo_comprehend.types.model_type.serialize_aws_json_1_1(
            value["model_type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_comprehend.types.timestamp

        out["LastModifiedTime"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "latest_flywheel_iteration" in value:
        out["LatestFlywheelIteration"] = value["latest_flywheel_iteration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlywheelSummary:
    out: FlywheelSummary = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("ActiveModelArn") is not None:
        out["active_model_arn"] = data["ActiveModelArn"]
    if data.get("DataLakeS3Uri") is not None:
        out["data_lake_s3_uri"] = data["DataLakeS3Uri"]
    if data.get("Status") is not None:
        import capo_comprehend.types.flywheel_status

        out["status"] = capo_comprehend.types.flywheel_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("ModelType") is not None:
        import capo_comprehend.types.model_type

        out["model_type"] = capo_comprehend.types.model_type.deserialize_aws_json_1_1(
            data["ModelType"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_comprehend.types.timestamp

        out["last_modified_time"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("LatestFlywheelIteration") is not None:
        out["latest_flywheel_iteration"] = data["LatestFlywheelIteration"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlywheelSummary) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "active_model_arn" in value:
        out["ActiveModelArn"] = value["active_model_arn"]
    if "data_lake_s3_uri" in value:
        out["DataLakeS3Uri"] = value["data_lake_s3_uri"]
    if "status" in value:
        import capo_comprehend.types.flywheel_status

        out["Status"] = capo_comprehend.types.flywheel_status.serialize_cbor(
            value["status"]
        )
    if "model_type" in value:
        import capo_comprehend.types.model_type

        out["ModelType"] = capo_comprehend.types.model_type.serialize_cbor(
            value["model_type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_comprehend.types.timestamp

        out["LastModifiedTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["last_modified_time"]
        )
    if "latest_flywheel_iteration" in value:
        out["LatestFlywheelIteration"] = value["latest_flywheel_iteration"]
    return out


def deserialize_cbor(data: dict) -> FlywheelSummary:
    out: FlywheelSummary = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("ActiveModelArn") is not None:
        out["active_model_arn"] = data["ActiveModelArn"]
    if data.get("DataLakeS3Uri") is not None:
        out["data_lake_s3_uri"] = data["DataLakeS3Uri"]
    if data.get("Status") is not None:
        import capo_comprehend.types.flywheel_status

        out["status"] = capo_comprehend.types.flywheel_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("ModelType") is not None:
        import capo_comprehend.types.model_type

        out["model_type"] = capo_comprehend.types.model_type.deserialize_cbor(
            data["ModelType"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_comprehend.types.timestamp

        out["last_modified_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["LastModifiedTime"]
        )
    if data.get("LatestFlywheelIteration") is not None:
        out["latest_flywheel_iteration"] = data["LatestFlywheelIteration"]
    return out
