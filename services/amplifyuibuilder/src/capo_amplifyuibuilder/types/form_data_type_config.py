"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormDataTypeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form_data_source_type


class FormDataTypeConfig(TypedDict, closed=True):
    data_source_type: (
        "capo_amplifyuibuilder.types.form_data_source_type.FormDataSourceType"
    )
    """<p>The data source type, either an Amplify DataStore model or a custom data type.</p>"""
    data_type_name: "str"
    """<p>The unique name of the data type you are using as the data source for the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormDataTypeConfig) -> dict:
    out: dict = {}
    out["dataSourceType"] = value["data_source_type"]
    out["dataTypeName"] = value["data_type_name"]
    return out


def deserialize_json(data: dict) -> FormDataTypeConfig:
    out: FormDataTypeConfig = {}  # type: ignore[typeddict-item]
    if data.get("dataSourceType") is not None:
        out["data_source_type"] = data["dataSourceType"]
    else:
        out["data_source_type"] = ""
    if data.get("dataTypeName") is not None:
        out["data_type_name"] = data["dataTypeName"]
    else:
        out["data_type_name"] = ""
    return out
