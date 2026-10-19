"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SyntheticDataColumnProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.synthetic_data_column_name
    import capo_cleanrooms.types.synthetic_data_column_type


class SyntheticDataColumnProperties(TypedDict, closed=True):
    column_name: (
        "capo_cleanrooms.types.synthetic_data_column_name.SyntheticDataColumnName"
    )
    """<p>The name of the data column as it appears in the dataset.</p>"""
    column_type: (
        "capo_cleanrooms.types.synthetic_data_column_type.SyntheticDataColumnType"
    )
    """<p>The data type of the column, which determines how the synthetic data generation algorithm processes and synthesizes values for this column.</p>"""
    is_predictive_value: "bool"
    """<p>Indicates if this column contains predictive values that should be treated as target variables in machine learning models. This affects how the synthetic data generation preserves statistical relationships.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyntheticDataColumnProperties) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    import capo_cleanrooms.types.synthetic_data_column_type

    out["columnType"] = capo_cleanrooms.types.synthetic_data_column_type.serialize_json(
        value["column_type"]
    )
    out["isPredictiveValue"] = value["is_predictive_value"]
    return out


def deserialize_json(data: dict) -> SyntheticDataColumnProperties:
    out: SyntheticDataColumnProperties = {}  # type: ignore[typeddict-item]
    if data.get("columnName") is not None:
        out["column_name"] = data["columnName"]
    else:
        out["column_name"] = ""
    if data.get("columnType") is not None:
        import capo_cleanrooms.types.synthetic_data_column_type

        out["column_type"] = (
            capo_cleanrooms.types.synthetic_data_column_type.deserialize_json(
                data["columnType"]
            )
        )
    else:
        import typing

        out["column_type"] = typing.cast(
            "capo_cleanrooms.types.synthetic_data_column_type.SyntheticDataColumnType",
            "",
        )
    if data.get("isPredictiveValue") is not None:
        out["is_predictive_value"] = data["isPredictiveValue"]
    else:
        out["is_predictive_value"] = False
    return out
