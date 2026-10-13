"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringFilterValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_string_filter_static_value


class DataSetStringFilterValue(TypedDict, closed=True):
    static_value: NotRequired[
        "capo_quicksight.types.data_set_string_filter_static_value.DataSetStringFilterStaticValue"
    ]
    """<p>A static string value used for filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringFilterValue) -> dict:
    out: dict = {}
    if "static_value" in value:
        out["StaticValue"] = value["static_value"]
    return out


def deserialize_json(data: dict) -> DataSetStringFilterValue:
    out: DataSetStringFilterValue = {}  # type: ignore[typeddict-item]
    if data.get("StaticValue") is not None:
        out["static_value"] = data["StaticValue"]
    return out


def redact_sensitive(value: DataSetStringFilterValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "static_value" in value:
        out["static_value"] = "*** Sensitive Data Redacted ***"
    return out
