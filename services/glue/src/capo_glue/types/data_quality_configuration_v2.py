"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityConfigurationV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.observation_configuration
    import capo_glue.types.observation_mode


class DataQualityConfigurationV2(TypedDict, closed=True):
    observations_enabled: NotRequired[
        "capo_glue.types.observation_configuration.ObservationConfiguration"
    ]
    """<p>Whether observations are enabled for the run. Valid values are:</p> <ul> <li> <p> <code>ALL</code> </p> </li> <li> <p> <code>NONE</code> </p> </li> </ul>"""
    observation_mode: NotRequired["capo_glue.types.observation_mode.ObservationMode"]
    """<p>The observation mode for the run. Valid values are:</p> <ul> <li> <p> <code>SCHEDULED</code> </p> </li> <li> <p> <code>FIXED</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityConfigurationV2) -> dict:
    out: dict = {}
    if "observations_enabled" in value:
        import capo_glue.types.observation_configuration

        out["ObservationsEnabled"] = (
            capo_glue.types.observation_configuration.serialize_aws_json_1_1(
                value["observations_enabled"]
            )
        )
    if "observation_mode" in value:
        import capo_glue.types.observation_mode

        out["ObservationMode"] = (
            capo_glue.types.observation_mode.serialize_aws_json_1_1(
                value["observation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityConfigurationV2:
    out: DataQualityConfigurationV2 = {}  # type: ignore[typeddict-item]
    if data.get("ObservationsEnabled") is not None:
        import capo_glue.types.observation_configuration

        out["observations_enabled"] = (
            capo_glue.types.observation_configuration.deserialize_aws_json_1_1(
                data["ObservationsEnabled"]
            )
        )
    if data.get("ObservationMode") is not None:
        import capo_glue.types.observation_mode

        out["observation_mode"] = (
            capo_glue.types.observation_mode.deserialize_aws_json_1_1(
                data["ObservationMode"]
            )
        )
    return out
