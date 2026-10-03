"""Generated from Smithy shape ``com.amazonaws.comprehend#StartEventsDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.input_data_config
    import capo_comprehend.types.job_name
    import capo_comprehend.types.language_code
    import capo_comprehend.types.output_data_config
    import capo_comprehend.types.tag_list
    import capo_comprehend.types.target_event_types


class StartEventsDetectionJobRequest(TypedDict, closed=True):
    input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig"
    """<p>Specifies the format and location of the input data for the job.</p>"""
    output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig"
    """<p>Specifies where to send the output files.</p>"""
    data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    job_name: NotRequired["capo_comprehend.types.job_name.JobName"]
    """<p>The identifier of the events detection job.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p>The language code of the input documents.</p>"""
    client_request_token: NotRequired[
        "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>An unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    target_event_types: "capo_comprehend.types.target_event_types.TargetEventTypes"
    """<p>The types of events to detect in the input documents.</p>"""
    tags: NotRequired["capo_comprehend.types.tag_list.TagList"]
    """<p>Tags to associate with the events detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartEventsDetectionJobRequest) -> dict:
    out: dict = {}
    import capo_comprehend.types.input_data_config

    out["InputDataConfig"] = (
        capo_comprehend.types.input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    import capo_comprehend.types.output_data_config

    out["OutputDataConfig"] = (
        capo_comprehend.types.output_data_config.serialize_aws_json_1_1(
            value["output_data_config"]
        )
    )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    import capo_comprehend.types.target_event_types

    out["TargetEventTypes"] = (
        capo_comprehend.types.target_event_types.serialize_aws_json_1_1(
            value["target_event_types"]
        )
    )
    if "tags" in value:
        import capo_comprehend.types.tag_list

        out["Tags"] = capo_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartEventsDetectionJobRequest:
    out: StartEventsDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("InputDataConfig") is not None:
        import capo_comprehend.types.input_data_config

        out["input_data_config"] = (
            capo_comprehend.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartEventsDetectionJobRequest.input_data_config required"
        )
    if data.get("OutputDataConfig") is not None:
        import capo_comprehend.types.output_data_config

        out["output_data_config"] = (
            capo_comprehend.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartEventsDetectionJobRequest.output_data_config required"
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartEventsDetectionJobRequest.data_access_role_arn required"
        )
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "StartEventsDetectionJobRequest.language_code required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("TargetEventTypes") is not None:
        import capo_comprehend.types.target_event_types

        out["target_event_types"] = (
            capo_comprehend.types.target_event_types.deserialize_aws_json_1_1(
                data["TargetEventTypes"]
            )
        )
    else:
        raise DeserializationError(
            "StartEventsDetectionJobRequest.target_event_types required"
        )
    if data.get("Tags") is not None:
        import capo_comprehend.types.tag_list

        out["tags"] = capo_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
