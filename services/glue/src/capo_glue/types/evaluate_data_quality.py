"""Generated from Smithy shape ``com.amazonaws.glue#EvaluateDataQuality``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.dq_results_publishing_options
    import capo_glue.types.dq_stop_job_on_failure_options
    import capo_glue.types.dq_transform_output
    import capo_glue.types.dqdl_string
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class EvaluateDataQuality(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data quality evaluation.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The inputs of your data quality evaluation.</p>"""
    ruleset: "capo_glue.types.dqdl_string.DQDLString"
    """<p>The ruleset for your data quality evaluation.</p>"""
    output: NotRequired["capo_glue.types.dq_transform_output.DQTransformOutput"]
    """<p>The output of your data quality evaluation.</p>"""
    publishing_options: NotRequired[
        "capo_glue.types.dq_results_publishing_options.DQResultsPublishingOptions"
    ]
    """<p>Options to configure how your results are published.</p>"""
    stop_job_on_failure_options: NotRequired[
        "capo_glue.types.dq_stop_job_on_failure_options.DQStopJobOnFailureOptions"
    ]
    """<p>Options to configure how your job will stop if your data quality evaluation fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluateDataQuality) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Ruleset"] = value["ruleset"]
    if "output" in value:
        import capo_glue.types.dq_transform_output

        out["Output"] = capo_glue.types.dq_transform_output.serialize_aws_json_1_1(
            value["output"]
        )
    if "publishing_options" in value:
        import capo_glue.types.dq_results_publishing_options

        out["PublishingOptions"] = (
            capo_glue.types.dq_results_publishing_options.serialize_aws_json_1_1(
                value["publishing_options"]
            )
        )
    if "stop_job_on_failure_options" in value:
        import capo_glue.types.dq_stop_job_on_failure_options

        out["StopJobOnFailureOptions"] = (
            capo_glue.types.dq_stop_job_on_failure_options.serialize_aws_json_1_1(
                value["stop_job_on_failure_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluateDataQuality:
    out: EvaluateDataQuality = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("Ruleset") is not None:
        out["ruleset"] = data["Ruleset"]
    else:
        out["ruleset"] = ""
    if data.get("Output") is not None:
        import capo_glue.types.dq_transform_output

        out["output"] = capo_glue.types.dq_transform_output.deserialize_aws_json_1_1(
            data["Output"]
        )
    if data.get("PublishingOptions") is not None:
        import capo_glue.types.dq_results_publishing_options

        out["publishing_options"] = (
            capo_glue.types.dq_results_publishing_options.deserialize_aws_json_1_1(
                data["PublishingOptions"]
            )
        )
    if data.get("StopJobOnFailureOptions") is not None:
        import capo_glue.types.dq_stop_job_on_failure_options

        out["stop_job_on_failure_options"] = (
            capo_glue.types.dq_stop_job_on_failure_options.deserialize_aws_json_1_1(
                data["StopJobOnFailureOptions"]
            )
        )
    return out
