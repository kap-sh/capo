"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProfilerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.disable_profiler
    import capo_sagemaker.types.profiling_interval_in_milliseconds
    import capo_sagemaker.types.profiling_parameters
    import capo_sagemaker.types.s3_uri


class ProfilerConfig(TypedDict, closed=True):
    s3_output_path: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>Path to Amazon S3 storage location for system and framework metrics.</p>"""
    profiling_interval_in_milliseconds: NotRequired[
        "capo_sagemaker.types.profiling_interval_in_milliseconds.ProfilingIntervalInMilliseconds"
    ]
    """<p>A time interval for capturing system metrics in milliseconds. Available values are 100, 200, 500, 1000 (1 second), 5000 (5 seconds), and 60000 (1 minute) milliseconds. The default value is 500 milliseconds.</p>"""
    profiling_parameters: NotRequired[
        "capo_sagemaker.types.profiling_parameters.ProfilingParameters"
    ]
    """<p>Configuration information for capturing framework metrics. Available key strings for different profiling options are <code>DetailedProfilingConfig</code>, <code>PythonProfilingConfig</code>, and <code>DataLoaderProfilingConfig</code>. The following codes are configuration structures for the <code>ProfilingParameters</code> parameter. To learn more about how to configure the <code>ProfilingParameters</code> parameter, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html">Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job</a>. </p>"""
    disable_profiler: NotRequired[
        "capo_sagemaker.types.disable_profiler.DisableProfiler"
    ]
    """<p>Configuration to turn off Amazon SageMaker Debugger's system monitoring and profiling functionality. To turn it off, set to <code>True</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfilerConfig) -> dict:
    out: dict = {}
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "profiling_interval_in_milliseconds" in value:
        out["ProfilingIntervalInMilliseconds"] = value[
            "profiling_interval_in_milliseconds"
        ]
    if "profiling_parameters" in value:
        import capo_sagemaker.types.profiling_parameters

        out["ProfilingParameters"] = (
            capo_sagemaker.types.profiling_parameters.serialize_aws_json_1_1(
                value["profiling_parameters"]
            )
        )
    if "disable_profiler" in value:
        out["DisableProfiler"] = value["disable_profiler"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProfilerConfig:
    out: ProfilerConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3OutputPath") is not None:
        out["s3_output_path"] = data["S3OutputPath"]
    if data.get("ProfilingIntervalInMilliseconds") is not None:
        out["profiling_interval_in_milliseconds"] = data[
            "ProfilingIntervalInMilliseconds"
        ]
    if data.get("ProfilingParameters") is not None:
        import capo_sagemaker.types.profiling_parameters

        out["profiling_parameters"] = (
            capo_sagemaker.types.profiling_parameters.deserialize_aws_json_1_1(
                data["ProfilingParameters"]
            )
        )
    if data.get("DisableProfiler") is not None:
        out["disable_profiler"] = data["DisableProfiler"]
    return out
