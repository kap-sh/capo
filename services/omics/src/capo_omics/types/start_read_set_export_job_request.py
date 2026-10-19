"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.client_token
    import capo_omics.types.export_read_set_list
    import capo_omics.types.role_arn
    import capo_omics.types.s3_destination
    import capo_omics.types.sequence_store_id


class StartReadSetExportJobRequest(TypedDict, closed=True):
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    destination: "capo_omics.types.s3_destination.S3Destination"
    """<p>A location for exported files in Amazon S3.</p>"""
    role_arn: "capo_omics.types.role_arn.RoleArn"
    """<p>A service role for the job.</p>"""
    client_token: NotRequired["capo_omics.types.client_token.ClientToken"]
    """<p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>"""
    sources: "capo_omics.types.export_read_set_list.ExportReadSetList"
    """<p>The job's source files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetExportJobRequest) -> dict:
    out: dict = {}
    out["destination"] = value["destination"]
    out["roleArn"] = value["role_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_omics.types.export_read_set_list

    out["sources"] = capo_omics.types.export_read_set_list.serialize_json(
        value["sources"]
    )
    return out


def deserialize_json(data: dict) -> StartReadSetExportJobRequest:
    out: StartReadSetExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("destination") is not None:
        out["destination"] = data["destination"]
    else:
        out["destination"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("sources") is not None:
        import capo_omics.types.export_read_set_list

        out["sources"] = capo_omics.types.export_read_set_list.deserialize_json(
            data["sources"]
        )
    else:
        out["sources"] = []
    return out
