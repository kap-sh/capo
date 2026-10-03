"""Generated from Smithy shape ``com.amazonaws.location#StartJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.client_token
    import capo_location.types.iam_role_arn
    import capo_location.types.job_action
    import capo_location.types.job_action_options
    import capo_location.types.job_input_options
    import capo_location.types.job_output_options
    import capo_location.types.resource_name
    import capo_location.types.tag_map


class StartJobRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_location.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency.</p>"""
    action: "capo_location.types.job_action.JobAction"
    """<p>The action to perform on the input data.</p>"""
    action_options: NotRequired[
        "capo_location.types.job_action_options.JobActionOptions"
    ]
    """<p>Additional parameters that can be requested for each result.</p>"""
    execution_role_arn: "capo_location.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon Location Service assumes during job processing. Amazon Location Service uses this role to access the input and output locations specified for the job.</p> <note> <p>The IAM role must be created in the same Amazon Web Services account where you plan to run your job.</p> </note> <p>For more information about configuring IAM roles for Amazon Location jobs, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/configure-iam-role-policy-credentials.html">Configure IAM permissions</a> in the <i>Amazon Location Service Developer Guide</i>.</p>"""
    input_options: "capo_location.types.job_input_options.JobInputOptions"
    """<p>Configuration for input data location and format.</p> <note> <p>Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.</p> </note>"""
    name: NotRequired["capo_location.types.resource_name.ResourceName"]
    """<p>An optional name for the job resource.</p>"""
    output_options: "capo_location.types.job_output_options.JobOutputOptions"
    """<p>Configuration for output data location and format.</p>"""
    tags: NotRequired["capo_location.types.tag_map.TagMap"]
    """<p>Tags and corresponding values to be associated with the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Action"] = value["action"]
    if "action_options" in value:
        import capo_location.types.job_action_options

        out["ActionOptions"] = capo_location.types.job_action_options.serialize_json(
            value["action_options"]
        )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    import capo_location.types.job_input_options

    out["InputOptions"] = capo_location.types.job_input_options.serialize_json(
        value["input_options"]
    )
    if "name" in value:
        out["Name"] = value["name"]
    import capo_location.types.job_output_options

    out["OutputOptions"] = capo_location.types.job_output_options.serialize_json(
        value["output_options"]
    )
    if "tags" in value:
        import capo_location.types.tag_map

        out["Tags"] = capo_location.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartJobRequest:
    out: StartJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        raise DeserializationError("StartJobRequest.action required")
    if data.get("ActionOptions") is not None:
        import capo_location.types.job_action_options

        out["action_options"] = capo_location.types.job_action_options.deserialize_json(
            data["ActionOptions"]
        )
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError("StartJobRequest.execution_role_arn required")
    if data.get("InputOptions") is not None:
        import capo_location.types.job_input_options

        out["input_options"] = capo_location.types.job_input_options.deserialize_json(
            data["InputOptions"]
        )
    else:
        raise DeserializationError("StartJobRequest.input_options required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("OutputOptions") is not None:
        import capo_location.types.job_output_options

        out["output_options"] = capo_location.types.job_output_options.deserialize_json(
            data["OutputOptions"]
        )
    else:
        raise DeserializationError("StartJobRequest.output_options required")
    if data.get("Tags") is not None:
        import capo_location.types.tag_map

        out["tags"] = capo_location.types.tag_map.deserialize_json(data["Tags"])
    return out
