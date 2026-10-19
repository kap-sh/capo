"""Generated from Smithy shape ``com.amazonaws.quicksight#MappedDataSetParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_identifier
    import capo_quicksight.types.parameter_name


class MappedDataSetParameter(TypedDict, closed=True):
    data_set_identifier: "capo_quicksight.types.data_set_identifier.DataSetIdentifier"
    """<p>A unique name that identifies a dataset within the analysis or dashboard.</p>"""
    data_set_parameter_name: "capo_quicksight.types.parameter_name.ParameterName"
    """<p>The name of the dataset parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MappedDataSetParameter) -> dict:
    out: dict = {}
    out["DataSetIdentifier"] = value["data_set_identifier"]
    out["DataSetParameterName"] = value["data_set_parameter_name"]
    return out


def deserialize_json(data: dict) -> MappedDataSetParameter:
    out: MappedDataSetParameter = {}  # type: ignore[typeddict-item]
    if data.get("DataSetIdentifier") is not None:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        out["data_set_identifier"] = ""
    if data.get("DataSetParameterName") is not None:
        out["data_set_parameter_name"] = data["DataSetParameterName"]
    else:
        out["data_set_parameter_name"] = ""
    return out
