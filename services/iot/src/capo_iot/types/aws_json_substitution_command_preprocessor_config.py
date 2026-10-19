"""Generated from Smithy shape ``com.amazonaws.iot#AwsJsonSubstitutionCommandPreprocessorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.output_format


class AwsJsonSubstitutionCommandPreprocessorConfig(TypedDict, closed=True):
    output_format: "capo_iot.types.output_format.OutputFormat"
    """<p>Converts the command preprocessor result to the format defined by this parameter, before sending it to the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJsonSubstitutionCommandPreprocessorConfig) -> dict:
    out: dict = {}
    import capo_iot.types.output_format

    out["outputFormat"] = capo_iot.types.output_format.serialize_json(
        value["output_format"]
    )
    return out


def deserialize_json(data: dict) -> AwsJsonSubstitutionCommandPreprocessorConfig:
    out: AwsJsonSubstitutionCommandPreprocessorConfig = {}  # type: ignore[typeddict-item]
    if data.get("outputFormat") is not None:
        import capo_iot.types.output_format

        out["output_format"] = capo_iot.types.output_format.deserialize_json(
            data["outputFormat"]
        )
    else:
        import typing

        out["output_format"] = typing.cast(
            "capo_iot.types.output_format.OutputFormat", ""
        )
    return out
