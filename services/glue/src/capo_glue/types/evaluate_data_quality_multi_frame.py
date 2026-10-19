"""Generated from Smithy shape ``com.amazonaws.glue#EvaluateDataQualityMultiFrame``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.dq_additional_options
    import capo_glue.types.dq_results_publishing_options
    import capo_glue.types.dq_stop_job_on_failure_options
    import capo_glue.types.dqdl_aliases
    import capo_glue.types.dqdl_string
    import capo_glue.types.many_inputs
    import capo_glue.types.node_name


class EvaluateDataQualityMultiFrame(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data quality evaluation.</p>"""
    inputs: "capo_glue.types.many_inputs.ManyInputs"
    """<p>The inputs of your data quality evaluation. The first input in this list is the primary data source.</p>"""
    additional_data_sources: NotRequired["capo_glue.types.dqdl_aliases.DQDLAliases"]
    """<p>The aliases of all data sources except primary.</p>"""
    ruleset: "capo_glue.types.dqdl_string.DQDLString"
    """<p>The ruleset for your data quality evaluation.</p>"""
    publishing_options: NotRequired[
        "capo_glue.types.dq_results_publishing_options.DQResultsPublishingOptions"
    ]
    """<p>Options to configure how your results are published.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.dq_additional_options.DQAdditionalOptions"
    ]
    """<p>Options to configure runtime behavior of the transform.</p>"""
    stop_job_on_failure_options: NotRequired[
        "capo_glue.types.dq_stop_job_on_failure_options.DQStopJobOnFailureOptions"
    ]
    """<p>Options to configure how your job will stop if your data quality evaluation fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluateDataQualityMultiFrame) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.many_inputs

    out["Inputs"] = capo_glue.types.many_inputs.serialize_aws_json_1_1(value["inputs"])
    if "additional_data_sources" in value:
        import capo_glue.types.dqdl_aliases

        out["AdditionalDataSources"] = (
            capo_glue.types.dqdl_aliases.serialize_aws_json_1_1(
                value["additional_data_sources"]
            )
        )
    out["Ruleset"] = value["ruleset"]
    if "publishing_options" in value:
        import capo_glue.types.dq_results_publishing_options

        out["PublishingOptions"] = (
            capo_glue.types.dq_results_publishing_options.serialize_aws_json_1_1(
                value["publishing_options"]
            )
        )
    if "additional_options" in value:
        import capo_glue.types.dq_additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.dq_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
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


def deserialize_aws_json_1_1(data: dict) -> EvaluateDataQualityMultiFrame:
    out: EvaluateDataQualityMultiFrame = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.many_inputs

        out["inputs"] = capo_glue.types.many_inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("AdditionalDataSources") is not None:
        import capo_glue.types.dqdl_aliases

        out["additional_data_sources"] = (
            capo_glue.types.dqdl_aliases.deserialize_aws_json_1_1(
                data["AdditionalDataSources"]
            )
        )
    if data.get("Ruleset") is not None:
        out["ruleset"] = data["Ruleset"]
    else:
        out["ruleset"] = ""
    if data.get("PublishingOptions") is not None:
        import capo_glue.types.dq_results_publishing_options

        out["publishing_options"] = (
            capo_glue.types.dq_results_publishing_options.deserialize_aws_json_1_1(
                data["PublishingOptions"]
            )
        )
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.dq_additional_options

        out["additional_options"] = (
            capo_glue.types.dq_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
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
