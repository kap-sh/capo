"""Generated from Smithy shape ``com.amazonaws.finspacedata#UpdateChangesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_finspace_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace_data.types.changeset_id
    import capo_finspace_data.types.client_token
    import capo_finspace_data.types.dataset_id
    import capo_finspace_data.types.format_params
    import capo_finspace_data.types.source_params


class UpdateChangesetRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    dataset_id: "capo_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier for the FinSpace Dataset in which the Changeset is created.</p>"""
    changeset_id: "capo_finspace_data.types.changeset_id.ChangesetId"
    """<p>The unique identifier for the Changeset to update.</p>"""
    source_params: "capo_finspace_data.types.source_params.SourceParams"
    """<p>Options that define the location of the data being ingested (<code>s3SourcePath</code>) and the source of the changeset (<code>sourceType</code>).</p> <p>Both <code>s3SourcePath</code> and <code>sourceType</code> are required attributes.</p> <p>Here is an example of how you could specify the <code>sourceParams</code>:</p> <p> <code> "sourceParams": { "s3SourcePath": "s3://finspace-landing-us-east-2-bk7gcfvitndqa6ebnvys4d/scratch/wr5hh8pwkpqqkxa4sxrmcw/ingestion/equity.csv", "sourceType": "S3" } </code> </p> <p>The S3 path that you specify must allow the FinSpace role access. To do that, you first need to configure the IAM policy on S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html#access-s3-buckets">Loading data from an Amazon S3 Bucket using the FinSpace API</a>section.</p>"""
    format_params: "capo_finspace_data.types.format_params.FormatParams"
    """<p>Options that define the structure of the source file(s) including the format type (<code>formatType</code>), header row (<code>withHeader</code>), data separation character (<code>separator</code>) and the type of compression (<code>compression</code>). </p> <p> <code>formatType</code> is a required attribute and can have the following values: </p> <ul> <li> <p> <code>PARQUET</code> – Parquet source file format.</p> </li> <li> <p> <code>CSV</code> – CSV source file format.</p> </li> <li> <p> <code>JSON</code> – JSON source file format.</p> </li> <li> <p> <code>XML</code> – XML source file format.</p> </li> </ul> <p>Here is an example of how you could specify the <code>formatParams</code>:</p> <p> <code> "formatParams": { "formatType": "CSV", "withHeader": "true", "separator": ",", "compression":"None" } </code> </p> <p>Note that if you only provide <code>formatType</code> as <code>CSV</code>, the rest of the attributes will automatically default to CSV values as following:</p> <p> <code> { "withHeader": "true", "separator": "," } </code> </p> <p> For more information about supported file formats, see <a href="https://docs.aws.amazon.com/finspace/latest/userguide/supported-data-types.html">Supported Data Types and File Formats</a> in the FinSpace User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChangesetRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_finspace_data.types.source_params

    out["sourceParams"] = capo_finspace_data.types.source_params.serialize_json(
        value["source_params"]
    )
    import capo_finspace_data.types.format_params

    out["formatParams"] = capo_finspace_data.types.format_params.serialize_json(
        value["format_params"]
    )
    return out


def deserialize_json(data: dict) -> UpdateChangesetRequest:
    out: UpdateChangesetRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("sourceParams") is not None:
        import capo_finspace_data.types.source_params

        out["source_params"] = capo_finspace_data.types.source_params.deserialize_json(
            data["sourceParams"]
        )
    else:
        raise DeserializationError("UpdateChangesetRequest.source_params required")
    if data.get("formatParams") is not None:
        import capo_finspace_data.types.format_params

        out["format_params"] = capo_finspace_data.types.format_params.deserialize_json(
            data["formatParams"]
        )
    else:
        raise DeserializationError("UpdateChangesetRequest.format_params required")
    return out
