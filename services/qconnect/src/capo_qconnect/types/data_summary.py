"""Generated from Smithy shape ``com.amazonaws.qconnect#DataSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.data_details
    import capo_qconnect.types.data_reference


class DataSummary(TypedDict, closed=True):
    reference: "capo_qconnect.types.data_reference.DataReference"
    """<p>Reference information about the content.</p>"""
    details: "capo_qconnect.types.data_details.DataDetails"
    """<p>Details about the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSummary) -> dict:
    out: dict = {}
    import capo_qconnect.types.data_reference

    out["reference"] = capo_qconnect.types.data_reference.serialize_json(
        value["reference"]
    )
    import capo_qconnect.types.data_details

    out["details"] = capo_qconnect.types.data_details.serialize_json(value["details"])
    return out


def deserialize_json(data: dict) -> DataSummary:
    out: DataSummary = {}  # type: ignore[typeddict-item]
    if data.get("reference") is not None:
        import capo_qconnect.types.data_reference

        out["reference"] = capo_qconnect.types.data_reference.deserialize_json(
            data["reference"]
        )
    else:
        out["reference"] = {"$unknown": {"name": ""}}
    if data.get("details") is not None:
        import capo_qconnect.types.data_details

        out["details"] = capo_qconnect.types.data_details.deserialize_json(
            data["details"]
        )
    else:
        out["details"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: DataSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "details" in value:
        import capo_qconnect.types.data_details

        out["details"] = capo_qconnect.types.data_details.redact_sensitive(
            value["details"]
        )
    return out
