"""Generated from Smithy shape ``com.amazonaws.dataexchange#ExportRevisionsToS3RequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.export_server_side_encryption
    import capo_dataexchange.types.id
    import capo_dataexchange.types.list_of_revision_destination_entry


class ExportRevisionsToS3RequestDetails(TypedDict, closed=True):
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this export job.</p>"""
    encryption: NotRequired[
        "capo_dataexchange.types.export_server_side_encryption.ExportServerSideEncryption"
    ]
    """<p>Encryption configuration for the export job.</p>"""
    revision_destinations: "capo_dataexchange.types.list_of_revision_destination_entry.ListOfRevisionDestinationEntry"
    """<p>The destination for the revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportRevisionsToS3RequestDetails) -> dict:
    out: dict = {}
    out["DataSetId"] = value["data_set_id"]
    if "encryption" in value:
        import capo_dataexchange.types.export_server_side_encryption

        out["Encryption"] = (
            capo_dataexchange.types.export_server_side_encryption.serialize_json(
                value["encryption"]
            )
        )
    import capo_dataexchange.types.list_of_revision_destination_entry

    out["RevisionDestinations"] = (
        capo_dataexchange.types.list_of_revision_destination_entry.serialize_json(
            value["revision_destinations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExportRevisionsToS3RequestDetails:
    out: ExportRevisionsToS3RequestDetails = {}  # type: ignore[typeddict-item]
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("Encryption") is not None:
        import capo_dataexchange.types.export_server_side_encryption

        out["encryption"] = (
            capo_dataexchange.types.export_server_side_encryption.deserialize_json(
                data["Encryption"]
            )
        )
    if data.get("RevisionDestinations") is not None:
        import capo_dataexchange.types.list_of_revision_destination_entry

        out["revision_destinations"] = (
            capo_dataexchange.types.list_of_revision_destination_entry.deserialize_json(
                data["RevisionDestinations"]
            )
        )
    else:
        out["revision_destinations"] = []
    return out
