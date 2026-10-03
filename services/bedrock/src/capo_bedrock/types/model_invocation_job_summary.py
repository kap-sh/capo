"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.message
    import capo_bedrock.types.model_id
    import capo_bedrock.types.model_invocation_idempotency_token
    import capo_bedrock.types.model_invocation_job_arn
    import capo_bedrock.types.model_invocation_job_input_data_config
    import capo_bedrock.types.model_invocation_job_name
    import capo_bedrock.types.model_invocation_job_output_data_config
    import capo_bedrock.types.model_invocation_job_status
    import capo_bedrock.types.model_invocation_job_timeout_duration_in_hours
    import capo_bedrock.types.model_invocation_type
    import capo_bedrock.types.non_negative_long
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.timestamp
    import capo_bedrock.types.vpc_config


class ModelInvocationJobSummary(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.model_invocation_job_arn.ModelInvocationJobArn"
    """<p>The Amazon Resource Name (ARN) of the batch inference job.</p>"""
    job_name: "capo_bedrock.types.model_invocation_job_name.ModelInvocationJobName"
    """<p>The name of the batch inference job.</p>"""
    model_id: "capo_bedrock.types.model_id.ModelId"
    """<p>The unique identifier of the foundation model used for model inference.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.model_invocation_idempotency_token.ModelInvocationIdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    role_arn: "capo_bedrock.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html">Create a service role for batch inference</a>.</p>"""
    status: NotRequired[
        "capo_bedrock.types.model_invocation_job_status.ModelInvocationJobStatus"
    ]
    """<p>The status of the batch inference job.</p> <p>The following statuses are possible:</p> <ul> <li> <p>Submitted – This job has been submitted to a queue for validation.</p> </li> <li> <p>Validating – This job is being validated for the requirements described in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html">Format and upload your batch inference data</a>. The criteria include the following:</p> <ul> <li> <p>Your IAM service role has access to the Amazon S3 buckets containing your files.</p> </li> <li> <p>Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesn't check if the <code>modelInput</code> value matches the request body for the model.</p> </li> <li> <p>Your files fulfill the requirements for file size and number of records. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html">Quotas for Amazon Bedrock</a>.</p> </li> </ul> </li> <li> <p>Scheduled – This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.</p> </li> <li> <p>Expired – This job timed out because it was scheduled but didn't begin before the set timeout duration. Submit a new job request.</p> </li> <li> <p>InProgress – This job has begun. You can start viewing the results in the output S3 location.</p> </li> <li> <p>Completed – This job has successfully completed. View the output files in the output S3 location.</p> </li> <li> <p>PartiallyCompleted – This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.</p> </li> <li> <p>Failed – This job has failed. Check the failure message for any further details. For further assistance, reach out to the <a href="https://console.aws.amazon.com/support/home/">Amazon Web Services Support Center</a>.</p> </li> <li> <p>Stopped – This job was stopped by a user.</p> </li> <li> <p>Stopping – This job is being stopped by a user.</p> </li> </ul>"""
    message: NotRequired["capo_bedrock.types.message.Message"]
    """<p>If the batch inference job failed, this field contains a message describing why the job failed.</p>"""
    submit_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The time at which the batch inference job was submitted.</p>"""
    last_modified_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the batch inference job was last modified.</p>"""
    end_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the batch inference job ended.</p>"""
    input_data_config: "capo_bedrock.types.model_invocation_job_input_data_config.ModelInvocationJobInputDataConfig"
    """<p>Details about the location of the input to the batch inference job.</p>"""
    output_data_config: "capo_bedrock.types.model_invocation_job_output_data_config.ModelInvocationJobOutputDataConfig"
    """<p>Details about the location of the output of the batch inference job.</p>"""
    vpc_config: NotRequired["capo_bedrock.types.vpc_config.VpcConfig"]
    """<p>The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc">Protect batch inference jobs using a VPC</a>.</p>"""
    timeout_duration_in_hours: NotRequired[
        "capo_bedrock.types.model_invocation_job_timeout_duration_in_hours.ModelInvocationJobTimeoutDurationInHours"
    ]
    """<p>The number of hours after which the batch inference job was set to time out.</p>"""
    job_expiration_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the batch inference job times or timed out.</p>"""
    model_invocation_type: NotRequired[
        "capo_bedrock.types.model_invocation_type.ModelInvocationType"
    ]
    """<p>The invocation endpoint for ModelInvocationJob</p>"""
    total_record_count: NotRequired[
        "capo_bedrock.types.non_negative_long.NonNegativeLong"
    ]
    """<p>The total number of records in the batch inference job.</p>"""
    processed_record_count: NotRequired[
        "capo_bedrock.types.non_negative_long.NonNegativeLong"
    ]
    """<p>The number of records that have been processed in the batch inference job.</p>"""
    success_record_count: NotRequired[
        "capo_bedrock.types.non_negative_long.NonNegativeLong"
    ]
    """<p>The number of records that were successfully processed in the batch inference job.</p>"""
    error_record_count: NotRequired[
        "capo_bedrock.types.non_negative_long.NonNegativeLong"
    ]
    """<p>The number of records that failed to process in the batch inference job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    out["modelId"] = value["model_id"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["roleArn"] = value["role_arn"]
    if "status" in value:
        import capo_bedrock.types.model_invocation_job_status

        out["status"] = capo_bedrock.types.model_invocation_job_status.serialize_json(
            value["status"]
        )
    if "message" in value:
        out["message"] = value["message"]
    import capo_bedrock.types.timestamp

    out["submitTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["submit_time"]
    )
    if "last_modified_time" in value:
        import capo_bedrock.types.timestamp

        out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "end_time" in value:
        import capo_bedrock.types.timestamp

        out["endTime"] = capo_bedrock.types.timestamp.serialize_json(value["end_time"])
    import capo_bedrock.types.model_invocation_job_input_data_config

    out["inputDataConfig"] = (
        capo_bedrock.types.model_invocation_job_input_data_config.serialize_json(
            value["input_data_config"]
        )
    )
    import capo_bedrock.types.model_invocation_job_output_data_config

    out["outputDataConfig"] = (
        capo_bedrock.types.model_invocation_job_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    if "vpc_config" in value:
        import capo_bedrock.types.vpc_config

        out["vpcConfig"] = capo_bedrock.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "timeout_duration_in_hours" in value:
        out["timeoutDurationInHours"] = value["timeout_duration_in_hours"]
    if "job_expiration_time" in value:
        import capo_bedrock.types.timestamp

        out["jobExpirationTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["job_expiration_time"]
        )
    if "model_invocation_type" in value:
        import capo_bedrock.types.model_invocation_type

        out["modelInvocationType"] = (
            capo_bedrock.types.model_invocation_type.serialize_json(
                value["model_invocation_type"]
            )
        )
    if "total_record_count" in value:
        out["totalRecordCount"] = value["total_record_count"]
    if "processed_record_count" in value:
        out["processedRecordCount"] = value["processed_record_count"]
    if "success_record_count" in value:
        out["successRecordCount"] = value["success_record_count"]
    if "error_record_count" in value:
        out["errorRecordCount"] = value["error_record_count"]
    return out


def deserialize_json(data: dict) -> ModelInvocationJobSummary:
    out: ModelInvocationJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("ModelInvocationJobSummary.job_arn required")
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("ModelInvocationJobSummary.job_name required")
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("ModelInvocationJobSummary.model_id required")
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ModelInvocationJobSummary.role_arn required")
    if data.get("status") is not None:
        import capo_bedrock.types.model_invocation_job_status

        out["status"] = capo_bedrock.types.model_invocation_job_status.deserialize_json(
            data["status"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("submitTime") is not None:
        import capo_bedrock.types.timestamp

        out["submit_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["submitTime"]
        )
    else:
        raise DeserializationError("ModelInvocationJobSummary.submit_time required")
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if data.get("endTime") is not None:
        import capo_bedrock.types.timestamp

        out["end_time"] = capo_bedrock.types.timestamp.deserialize_json(data["endTime"])
    if data.get("inputDataConfig") is not None:
        import capo_bedrock.types.model_invocation_job_input_data_config

        out["input_data_config"] = (
            capo_bedrock.types.model_invocation_job_input_data_config.deserialize_json(
                data["inputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ModelInvocationJobSummary.input_data_config required"
        )
    if data.get("outputDataConfig") is not None:
        import capo_bedrock.types.model_invocation_job_output_data_config

        out["output_data_config"] = (
            capo_bedrock.types.model_invocation_job_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ModelInvocationJobSummary.output_data_config required"
        )
    if data.get("vpcConfig") is not None:
        import capo_bedrock.types.vpc_config

        out["vpc_config"] = capo_bedrock.types.vpc_config.deserialize_json(
            data["vpcConfig"]
        )
    if data.get("timeoutDurationInHours") is not None:
        out["timeout_duration_in_hours"] = data["timeoutDurationInHours"]
    if data.get("jobExpirationTime") is not None:
        import capo_bedrock.types.timestamp

        out["job_expiration_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["jobExpirationTime"]
        )
    if data.get("modelInvocationType") is not None:
        import capo_bedrock.types.model_invocation_type

        out["model_invocation_type"] = (
            capo_bedrock.types.model_invocation_type.deserialize_json(
                data["modelInvocationType"]
            )
        )
    if data.get("totalRecordCount") is not None:
        out["total_record_count"] = data["totalRecordCount"]
    if data.get("processedRecordCount") is not None:
        out["processed_record_count"] = data["processedRecordCount"]
    if data.get("successRecordCount") is not None:
        out["success_record_count"] = data["successRecordCount"]
    if data.get("errorRecordCount") is not None:
        out["error_record_count"] = data["errorRecordCount"]
    return out
