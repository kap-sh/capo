"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.inference_output_configuration
    import capo_cleanroomsml.types.logs_status
    import capo_cleanroomsml.types.metrics_status
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.trained_model_inference_job_arn
    import capo_cleanroomsml.types.trained_model_inference_job_status
    import capo_cleanroomsml.types.uuid


class TrainedModelInferenceJobSummary(TypedDict, closed=True):
    trained_model_inference_job_arn: "capo_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn"
    """<p>The Amazon Resource Name (ARN) of the trained model inference job.</p>"""
    configured_model_algorithm_association_arn: NotRequired[
        "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that is used for the trained model inference job.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the trained model inference job.</p>"""
    trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model that is used for the trained model inference job.</p>"""
    trained_model_version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model that was used for inference in this job.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained model inference job.</p>"""
    status: "capo_cleanroomsml.types.trained_model_inference_job_status.TrainedModelInferenceJobStatus"
    """<p>The status of the trained model inference job.</p>"""
    output_configuration: "capo_cleanroomsml.types.inference_output_configuration.InferenceOutputConfiguration"
    """<p>The output configuration information of the trained model job.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model inference job.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model inference job.</p>"""
    metrics_status: NotRequired["capo_cleanroomsml.types.metrics_status.MetricsStatus"]
    """<p>The metric status of the trained model inference job.</p>"""
    metrics_status_details: NotRequired["str"]
    """<p>Details about the metrics status for the trained model inference job.</p>"""
    logs_status: NotRequired["capo_cleanroomsml.types.logs_status.LogsStatus"]
    """<p>The log status of the trained model inference job.</p>"""
    logs_status_details: NotRequired["str"]
    """<p>Details about the log status for the trained model inference job.</p>"""
    ml_model_inference_payer_account_id: NotRequired[
        "capo_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying for model inference costs.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the trained model inference job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the trained model inference job was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelInferenceJobSummary) -> dict:
    out: dict = {}
    out["trainedModelInferenceJobArn"] = value["trained_model_inference_job_arn"]
    if "configured_model_algorithm_association_arn" in value:
        out["configuredModelAlgorithmAssociationArn"] = value[
            "configured_model_algorithm_association_arn"
        ]
    out["membershipIdentifier"] = value["membership_identifier"]
    out["trainedModelArn"] = value["trained_model_arn"]
    if "trained_model_version_identifier" in value:
        out["trainedModelVersionIdentifier"] = value["trained_model_version_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    import capo_cleanroomsml.types.trained_model_inference_job_status

    out["status"] = (
        capo_cleanroomsml.types.trained_model_inference_job_status.serialize_json(
            value["status"]
        )
    )
    import capo_cleanroomsml.types.inference_output_configuration

    out["outputConfiguration"] = (
        capo_cleanroomsml.types.inference_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "metrics_status" in value:
        import capo_cleanroomsml.types.metrics_status

        out["metricsStatus"] = capo_cleanroomsml.types.metrics_status.serialize_json(
            value["metrics_status"]
        )
    if "metrics_status_details" in value:
        out["metricsStatusDetails"] = value["metrics_status_details"]
    if "logs_status" in value:
        import capo_cleanroomsml.types.logs_status

        out["logsStatus"] = capo_cleanroomsml.types.logs_status.serialize_json(
            value["logs_status"]
        )
    if "logs_status_details" in value:
        out["logsStatusDetails"] = value["logs_status_details"]
    if "ml_model_inference_payer_account_id" in value:
        out["mlModelInferencePayerAccountId"] = value[
            "ml_model_inference_payer_account_id"
        ]
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> TrainedModelInferenceJobSummary:
    out: TrainedModelInferenceJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("trainedModelInferenceJobArn") is not None:
        out["trained_model_inference_job_arn"] = data["trainedModelInferenceJobArn"]
    else:
        out["trained_model_inference_job_arn"] = ""
    if data.get("configuredModelAlgorithmAssociationArn") is not None:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    if data.get("membershipIdentifier") is not None:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        out["membership_identifier"] = ""
    if data.get("trainedModelArn") is not None:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        out["trained_model_arn"] = ""
    if data.get("trainedModelVersionIdentifier") is not None:
        out["trained_model_version_identifier"] = data["trainedModelVersionIdentifier"]
    if data.get("collaborationIdentifier") is not None:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        out["collaboration_identifier"] = ""
    if data.get("status") is not None:
        import capo_cleanroomsml.types.trained_model_inference_job_status

        out["status"] = (
            capo_cleanroomsml.types.trained_model_inference_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanroomsml.types.trained_model_inference_job_status.TrainedModelInferenceJobStatus",
            "",
        )
    if data.get("outputConfiguration") is not None:
        import capo_cleanroomsml.types.inference_output_configuration

        out["output_configuration"] = (
            capo_cleanroomsml.types.inference_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "TrainedModelInferenceJobSummary.output_configuration required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("metricsStatus") is not None:
        import capo_cleanroomsml.types.metrics_status

        out["metrics_status"] = capo_cleanroomsml.types.metrics_status.deserialize_json(
            data["metricsStatus"]
        )
    if data.get("metricsStatusDetails") is not None:
        out["metrics_status_details"] = data["metricsStatusDetails"]
    if data.get("logsStatus") is not None:
        import capo_cleanroomsml.types.logs_status

        out["logs_status"] = capo_cleanroomsml.types.logs_status.deserialize_json(
            data["logsStatus"]
        )
    if data.get("logsStatusDetails") is not None:
        out["logs_status_details"] = data["logsStatusDetails"]
    if data.get("mlModelInferencePayerAccountId") is not None:
        out["ml_model_inference_payer_account_id"] = data[
            "mlModelInferencePayerAccountId"
        ]
    if data.get("createTime") is not None:
        import datetime

        out["create_time"] = datetime.datetime.fromisoformat(
            data["createTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
