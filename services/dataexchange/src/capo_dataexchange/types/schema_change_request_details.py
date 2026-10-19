"""Generated from Smithy shape ``com.amazonaws.dataexchange#SchemaChangeRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.list_of_schema_change_details
    import capo_dataexchange.types.timestamp


class SchemaChangeRequestDetails(TypedDict, closed=True):
    changes: NotRequired[
        "capo_dataexchange.types.list_of_schema_change_details.ListOfSchemaChangeDetails"
    ]
    """<p>List of schema changes happening in the scope of this notification. This can have up to 100 entries.</p>"""
    schema_change_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>A date in the future when the schema change is taking effect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaChangeRequestDetails) -> dict:
    out: dict = {}
    if "changes" in value:
        import capo_dataexchange.types.list_of_schema_change_details

        out["Changes"] = (
            capo_dataexchange.types.list_of_schema_change_details.serialize_json(
                value["changes"]
            )
        )
    import capo_dataexchange.types.timestamp

    out["SchemaChangeAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["schema_change_at"]
    )
    return out


def deserialize_json(data: dict) -> SchemaChangeRequestDetails:
    out: SchemaChangeRequestDetails = {}  # type: ignore[typeddict-item]
    if data.get("Changes") is not None:
        import capo_dataexchange.types.list_of_schema_change_details

        out["changes"] = (
            capo_dataexchange.types.list_of_schema_change_details.deserialize_json(
                data["Changes"]
            )
        )
    if data.get("SchemaChangeAt") is not None:
        import capo_dataexchange.types.timestamp

        out["schema_change_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["SchemaChangeAt"]
        )
    else:
        import datetime

        out["schema_change_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
