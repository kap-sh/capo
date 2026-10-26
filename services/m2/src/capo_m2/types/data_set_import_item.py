"""Generated from Smithy shape ``com.amazonaws.m2#DataSetImportItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.data_set
    import capo_m2.types.external_location


class DataSetImportItem(TypedDict, closed=True):
    data_set: "capo_m2.types.data_set.DataSet"
    """<p>The data set.</p>"""
    external_location: "capo_m2.types.external_location.ExternalLocation"
    """<p>The location of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportItem) -> dict:
    out: dict = {}
    import capo_m2.types.data_set

    out["dataSet"] = capo_m2.types.data_set.serialize_json(value["data_set"])
    import capo_m2.types.external_location

    out["externalLocation"] = capo_m2.types.external_location.serialize_json(
        value["external_location"]
    )
    return out


def deserialize_json(data: dict) -> DataSetImportItem:
    out: DataSetImportItem = {}  # type: ignore[typeddict-item]
    if data.get("dataSet") is not None:
        import capo_m2.types.data_set

        out["data_set"] = capo_m2.types.data_set.deserialize_json(data["dataSet"])
    else:
        raise DeserializationError("DataSetImportItem.data_set required")
    if data.get("externalLocation") is not None:
        import capo_m2.types.external_location

        out["external_location"] = capo_m2.types.external_location.deserialize_json(
            data["externalLocation"]
        )
    else:
        out["external_location"] = {"$unknown": {"name": ""}}
    return out
