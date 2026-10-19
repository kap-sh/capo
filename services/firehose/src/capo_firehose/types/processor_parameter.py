"""Generated from Smithy shape ``com.amazonaws.firehose#ProcessorParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.processor_parameter_name
    import capo_firehose.types.processor_parameter_value


class ProcessorParameter(TypedDict, closed=True):
    parameter_name: (
        "capo_firehose.types.processor_parameter_name.ProcessorParameterName"
    )
    """<p>The name of the parameter. Currently the following default values are supported: 3 for <code>NumberOfRetries</code> and 60 for the <code>BufferIntervalInSeconds</code>. The <code>BufferSizeInMBs</code> ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB. </p>"""
    parameter_value: (
        "capo_firehose.types.processor_parameter_value.ProcessorParameterValue"
    )
    """<p>The parameter value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessorParameter) -> dict:
    out: dict = {}
    import capo_firehose.types.processor_parameter_name

    out["ParameterName"] = (
        capo_firehose.types.processor_parameter_name.serialize_aws_json_1_1(
            value["parameter_name"]
        )
    )
    out["ParameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessorParameter:
    out: ProcessorParameter = {}  # type: ignore[typeddict-item]
    if data.get("ParameterName") is not None:
        import capo_firehose.types.processor_parameter_name

        out["parameter_name"] = (
            capo_firehose.types.processor_parameter_name.deserialize_aws_json_1_1(
                data["ParameterName"]
            )
        )
    else:
        import typing

        out["parameter_name"] = typing.cast(
            "capo_firehose.types.processor_parameter_name.ProcessorParameterName", ""
        )
    if data.get("ParameterValue") is not None:
        out["parameter_value"] = data["ParameterValue"]
    else:
        out["parameter_value"] = ""
    return out
