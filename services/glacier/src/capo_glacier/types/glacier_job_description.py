"""Generated from Smithy shape ``com.amazonaws.glacier#GlacierJobDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.action_code
    import capo_glacier.types.boolean
    import capo_glacier.types.inventory_retrieval_job_description
    import capo_glacier.types.output_location
    import capo_glacier.types.select_parameters
    import capo_glacier.types.size
    import capo_glacier.types.status_code
    import capo_glacier.types.string


class GlacierJobDescription(TypedDict, closed=True):
    job_id: NotRequired["capo_glacier.types.string.string"]
    """<p>An opaque string that identifies an Amazon S3 Glacier job.</p>"""
    job_description: NotRequired["capo_glacier.types.string.string"]
    """<p>The job description provided when initiating the job.</p>"""
    action: NotRequired["capo_glacier.types.action_code.ActionCode"]
    """<p>The job type. This value is either <code>ArchiveRetrieval</code>, <code>InventoryRetrieval</code>, or <code>Select</code>. </p>"""
    archive_id: NotRequired["capo_glacier.types.string.string"]
    """<p>The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.</p>"""
    vault_arn: NotRequired["capo_glacier.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.</p>"""
    creation_date: NotRequired["capo_glacier.types.string.string"]
    """<p>The UTC date when the job was created. This value is a string representation of ISO 8601 date format, for example <code>"2012-03-20T17:03:43.221Z"</code>.</p>"""
    completed: "capo_glacier.types.boolean.boolean"
    """<p>The job status. When a job is completed, you get the job's output using Get Job Output (GET output).</p>"""
    status_code: NotRequired["capo_glacier.types.status_code.StatusCode"]
    """<p>The status code can be <code>InProgress</code>, <code>Succeeded</code>, or <code>Failed</code>, and indicates the status of the job.</p>"""
    status_message: NotRequired["capo_glacier.types.string.string"]
    """<p>A friendly message that describes the job status.</p>"""
    archive_size_in_bytes: NotRequired["capo_glacier.types.size.Size"]
    """<p>For an archive retrieval job, this value is the size in bytes of the archive being requested for download. For an inventory retrieval or select job, this value is null.</p>"""
    inventory_size_in_bytes: NotRequired["capo_glacier.types.size.Size"]
    """<p>For an inventory retrieval job, this value is the size in bytes of the inventory requested for download. For an archive retrieval or select job, this value is null.</p>"""
    sns_topic: NotRequired["capo_glacier.types.string.string"]
    """<p>An Amazon SNS topic that receives notification.</p>"""
    completion_date: NotRequired["capo_glacier.types.string.string"]
    """<p>The UTC time that the job request completed. While the job is in progress, the value is null.</p>"""
    sha256_tree_hash: NotRequired["capo_glacier.types.string.string"]
    """<p>For an archive retrieval job, this value is the checksum of the archive. Otherwise, this value is null.</p> <p>The SHA256 tree hash value for the requested range of an archive. If the <b>InitiateJob</b> request for an archive specified a tree-hash aligned range, then this field returns a value.</p> <p>If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.</p> <p>This field is null for the following:</p> <ul> <li> <p>Archive retrieval jobs that specify a range that is not tree-hash aligned</p> </li> </ul> <ul> <li> <p>Archival jobs that specify a range that is equal to the whole archive, when the job status is <code>InProgress</code> </p> </li> </ul> <ul> <li> <p>Inventory jobs</p> </li> <li> <p>Select jobs</p> </li> </ul>"""
    archive_sha256_tree_hash: NotRequired["capo_glacier.types.string.string"]
    """<p>The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval or select jobs, this field is null.</p>"""
    retrieval_byte_range: NotRequired["capo_glacier.types.string.string"]
    """<p>The retrieved byte range for archive retrieval jobs in the form <i>StartByteValue</i>-<i>EndByteValue</i>. If no range was specified in the archive retrieval, then the whole archive is retrieved. In this case, <i>StartByteValue</i> equals 0 and <i>EndByteValue</i> equals the size of the archive minus 1. For inventory retrieval or select jobs, this field is null. </p>"""
    tier: NotRequired["capo_glacier.types.string.string"]
    """<p>The tier to use for a select or an archive retrieval. Valid values are <code>Expedited</code>, <code>Standard</code>, or <code>Bulk</code>. <code>Standard</code> is the default.</p>"""
    inventory_retrieval_parameters: NotRequired[
        "capo_glacier.types.inventory_retrieval_job_description.InventoryRetrievalJobDescription"
    ]
    """<p>Parameters used for range inventory retrieval.</p>"""
    job_output_path: NotRequired["capo_glacier.types.string.string"]
    """<p>Contains the job output location.</p>"""
    select_parameters: NotRequired[
        "capo_glacier.types.select_parameters.SelectParameters"
    ]
    """<p>Contains the parameters used for a select.</p>"""
    output_location: NotRequired["capo_glacier.types.output_location.OutputLocation"]
    """<p>Contains the location where the data from the select job is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlacierJobDescription) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_description" in value:
        out["JobDescription"] = value["job_description"]
    if "action" in value:
        import capo_glacier.types.action_code

        out["Action"] = capo_glacier.types.action_code.serialize_json(value["action"])
    if "archive_id" in value:
        out["ArchiveId"] = value["archive_id"]
    if "vault_arn" in value:
        out["VaultARN"] = value["vault_arn"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    out["Completed"] = value.get("completed", False)
    if "status_code" in value:
        import capo_glacier.types.status_code

        out["StatusCode"] = capo_glacier.types.status_code.serialize_json(
            value["status_code"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "archive_size_in_bytes" in value:
        out["ArchiveSizeInBytes"] = value["archive_size_in_bytes"]
    if "inventory_size_in_bytes" in value:
        out["InventorySizeInBytes"] = value["inventory_size_in_bytes"]
    if "sns_topic" in value:
        out["SNSTopic"] = value["sns_topic"]
    if "completion_date" in value:
        out["CompletionDate"] = value["completion_date"]
    if "sha256_tree_hash" in value:
        out["SHA256TreeHash"] = value["sha256_tree_hash"]
    if "archive_sha256_tree_hash" in value:
        out["ArchiveSHA256TreeHash"] = value["archive_sha256_tree_hash"]
    if "retrieval_byte_range" in value:
        out["RetrievalByteRange"] = value["retrieval_byte_range"]
    if "tier" in value:
        out["Tier"] = value["tier"]
    if "inventory_retrieval_parameters" in value:
        import capo_glacier.types.inventory_retrieval_job_description

        out["InventoryRetrievalParameters"] = (
            capo_glacier.types.inventory_retrieval_job_description.serialize_json(
                value["inventory_retrieval_parameters"]
            )
        )
    if "job_output_path" in value:
        out["JobOutputPath"] = value["job_output_path"]
    if "select_parameters" in value:
        import capo_glacier.types.select_parameters

        out["SelectParameters"] = capo_glacier.types.select_parameters.serialize_json(
            value["select_parameters"]
        )
    if "output_location" in value:
        import capo_glacier.types.output_location

        out["OutputLocation"] = capo_glacier.types.output_location.serialize_json(
            value["output_location"]
        )
    return out


def deserialize_json(data: dict) -> GlacierJobDescription:
    out: GlacierJobDescription = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobDescription") is not None:
        out["job_description"] = data["JobDescription"]
    if data.get("Action") is not None:
        import capo_glacier.types.action_code

        out["action"] = capo_glacier.types.action_code.deserialize_json(data["Action"])
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    if data.get("VaultARN") is not None:
        out["vault_arn"] = data["VaultARN"]
    if data.get("CreationDate") is not None:
        out["creation_date"] = data["CreationDate"]
    if data.get("Completed") is not None:
        out["completed"] = data["Completed"]
    else:
        out["completed"] = False
    if data.get("StatusCode") is not None:
        import capo_glacier.types.status_code

        out["status_code"] = capo_glacier.types.status_code.deserialize_json(
            data["StatusCode"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("ArchiveSizeInBytes") is not None:
        out["archive_size_in_bytes"] = data["ArchiveSizeInBytes"]
    if data.get("InventorySizeInBytes") is not None:
        out["inventory_size_in_bytes"] = data["InventorySizeInBytes"]
    if data.get("SNSTopic") is not None:
        out["sns_topic"] = data["SNSTopic"]
    if data.get("CompletionDate") is not None:
        out["completion_date"] = data["CompletionDate"]
    if data.get("SHA256TreeHash") is not None:
        out["sha256_tree_hash"] = data["SHA256TreeHash"]
    if data.get("ArchiveSHA256TreeHash") is not None:
        out["archive_sha256_tree_hash"] = data["ArchiveSHA256TreeHash"]
    if data.get("RetrievalByteRange") is not None:
        out["retrieval_byte_range"] = data["RetrievalByteRange"]
    if data.get("Tier") is not None:
        out["tier"] = data["Tier"]
    if data.get("InventoryRetrievalParameters") is not None:
        import capo_glacier.types.inventory_retrieval_job_description

        out["inventory_retrieval_parameters"] = (
            capo_glacier.types.inventory_retrieval_job_description.deserialize_json(
                data["InventoryRetrievalParameters"]
            )
        )
    if data.get("JobOutputPath") is not None:
        out["job_output_path"] = data["JobOutputPath"]
    if data.get("SelectParameters") is not None:
        import capo_glacier.types.select_parameters

        out["select_parameters"] = (
            capo_glacier.types.select_parameters.deserialize_json(
                data["SelectParameters"]
            )
        )
    if data.get("OutputLocation") is not None:
        import capo_glacier.types.output_location

        out["output_location"] = capo_glacier.types.output_location.deserialize_json(
            data["OutputLocation"]
        )
    return out
