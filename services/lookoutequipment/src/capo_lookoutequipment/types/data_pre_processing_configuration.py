"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DataPreProcessingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.target_sampling_rate


class DataPreProcessingConfiguration(TypedDict, closed=True):
    target_sampling_rate: NotRequired[
        "capo_lookoutequipment.types.target_sampling_rate.TargetSamplingRate"
    ]
    """<p>The sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the <code>TargetSamplingRate</code> is 1 minute.</p> <p>When providing a value for the <code>TargetSamplingRate</code>, you must attach the prefix "PT" to the rate you want. The value for a 1 second rate is therefore <i>PT1S</i>, the value for a 15 minute rate is <i>PT15M</i>, and the value for a 1 hour rate is <i>PT1H</i> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataPreProcessingConfiguration) -> dict:
    out: dict = {}
    if "target_sampling_rate" in value:
        import capo_lookoutequipment.types.target_sampling_rate

        out["TargetSamplingRate"] = (
            capo_lookoutequipment.types.target_sampling_rate.serialize_aws_json_1_0(
                value["target_sampling_rate"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DataPreProcessingConfiguration:
    out: DataPreProcessingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TargetSamplingRate") is not None:
        import capo_lookoutequipment.types.target_sampling_rate

        out["target_sampling_rate"] = (
            capo_lookoutequipment.types.target_sampling_rate.deserialize_aws_json_1_0(
                data["TargetSamplingRate"]
            )
        )
    return out
