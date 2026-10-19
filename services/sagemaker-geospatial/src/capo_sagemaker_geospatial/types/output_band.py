"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#OutputBand``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.output_type


class OutputBand(TypedDict, closed=True):
    band_name: "str"
    """<p>The name of the band.</p>"""
    output_data_type: "capo_sagemaker_geospatial.types.output_type.OutputType"
    """<p>The datatype of the output band.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputBand) -> dict:
    out: dict = {}
    out["BandName"] = value["band_name"]
    out["OutputDataType"] = value["output_data_type"]
    return out


def deserialize_json(data: dict) -> OutputBand:
    out: OutputBand = {}  # type: ignore[typeddict-item]
    if data.get("BandName") is not None:
        out["band_name"] = data["BandName"]
    else:
        out["band_name"] = ""
    if data.get("OutputDataType") is not None:
        out["output_data_type"] = data["OutputDataType"]
    else:
        out["output_data_type"] = ""
    return out
