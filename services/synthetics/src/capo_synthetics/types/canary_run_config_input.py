"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.environment_variables_map
    import capo_synthetics.types.ephemeral_storage_size
    import capo_synthetics.types.max_fifteen_minutes_in_seconds
    import capo_synthetics.types.max_size3008
    import capo_synthetics.types.nullable_boolean


class CanaryRunConfigInput(TypedDict, closed=True):
    timeout_in_seconds: NotRequired[
        "capo_synthetics.types.max_fifteen_minutes_in_seconds.MaxFifteenMinutesInSeconds"
    ]
    """<p>How long the canary is allowed to run before it must stop. You can't set this time to be longer than the frequency of the runs of this canary.</p> <p>If you omit this field, the frequency of the canary is used as this value, up to a maximum of 14 minutes.</p>"""
    memory_in_mb: NotRequired["capo_synthetics.types.max_size3008.MaxSize3008"]
    """<p>The maximum amount of memory available to the canary while it is running, in MB. This value must be a multiple of 64.</p>"""
    active_tracing: NotRequired[
        "capo_synthetics.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether this canary is to use active X-Ray tracing when it runs. Active tracing enables this canary run to be displayed in the ServiceLens and X-Ray service maps even if the canary does not hit an endpoint that has X-Ray tracing enabled. Using X-Ray tracing incurs charges. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html"> Canaries and X-Ray tracing</a>.</p> <p>You can enable active tracing only for canaries that use version <code>syn-nodejs-2.0</code> or later for their canary runtime.</p>"""
    environment_variables: NotRequired[
        "capo_synthetics.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Specifies the keys and values to use for any environment variables used in the canary script. Use the following format:</p> <p>{ "key1" : "value1", "key2" : "value2", ...}</p> <p>Keys must start with a letter and be at least two characters. The total size of your environment variables cannot exceed 4 KB. You can't specify any Lambda reserved environment variables as the keys for your environment variables. For more information about reserved keys, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime"> Runtime environment variables</a>.</p> <important> <p>Environment variable keys and values are encrypted at rest using Amazon Web Services owned KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.</p> </important>"""
    ephemeral_storage: NotRequired[
        "capo_synthetics.types.ephemeral_storage_size.EphemeralStorageSize"
    ]
    """<p>Specifies the amount of ephemeral storage (in MB) to allocate for the canary run during execution. This temporary storage is used for storing canary run artifacts (which are uploaded to an Amazon S3 bucket at the end of the run), and any canary browser operations. This temporary storage is cleared after the run is completed. Default storage value is 1024 MB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRunConfigInput) -> dict:
    out: dict = {}
    if "timeout_in_seconds" in value:
        out["TimeoutInSeconds"] = value["timeout_in_seconds"]
    if "memory_in_mb" in value:
        out["MemoryInMB"] = value["memory_in_mb"]
    if "active_tracing" in value:
        out["ActiveTracing"] = value["active_tracing"]
    if "environment_variables" in value:
        import capo_synthetics.types.environment_variables_map

        out["EnvironmentVariables"] = (
            capo_synthetics.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
    if "ephemeral_storage" in value:
        out["EphemeralStorage"] = value["ephemeral_storage"]
    return out


def deserialize_json(data: dict) -> CanaryRunConfigInput:
    out: CanaryRunConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("TimeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["TimeoutInSeconds"]
    if data.get("MemoryInMB") is not None:
        out["memory_in_mb"] = data["MemoryInMB"]
    if data.get("ActiveTracing") is not None:
        out["active_tracing"] = data["ActiveTracing"]
    if data.get("EnvironmentVariables") is not None:
        import capo_synthetics.types.environment_variables_map

        out["environment_variables"] = (
            capo_synthetics.types.environment_variables_map.deserialize_json(
                data["EnvironmentVariables"]
            )
        )
    if data.get("EphemeralStorage") is not None:
        out["ephemeral_storage"] = data["EphemeralStorage"]
    return out
