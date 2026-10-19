"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#RefreshCadence``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.frequency_option


class RefreshCadence(TypedDict, closed=True):
    frequency: "capo_bcm_data_exports.types.frequency_option.FrequencyOption"
    """<p>The frequency that data exports are updated. The export refreshes each time the source data updates, up to three times daily.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshCadence) -> dict:
    out: dict = {}
    import capo_bcm_data_exports.types.frequency_option

    out["Frequency"] = (
        capo_bcm_data_exports.types.frequency_option.serialize_aws_json_1_1(
            value["frequency"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshCadence:
    out: RefreshCadence = {}  # type: ignore[typeddict-item]
    if data.get("Frequency") is not None:
        import capo_bcm_data_exports.types.frequency_option

        out["frequency"] = (
            capo_bcm_data_exports.types.frequency_option.deserialize_aws_json_1_1(
                data["Frequency"]
            )
        )
    else:
        import typing

        out["frequency"] = typing.cast(
            "capo_bcm_data_exports.types.frequency_option.FrequencyOption", ""
        )
    return out
