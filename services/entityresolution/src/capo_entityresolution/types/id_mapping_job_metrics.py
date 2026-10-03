"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingJobMetrics``."""

from typing_extensions import NotRequired, TypedDict


class IdMappingJobMetrics(TypedDict, closed=True):
    input_records: NotRequired["int"]
    """<p>The total number of records that were input for processing.</p>"""
    total_records_processed: NotRequired["int"]
    """<p>The total number of records that were processed.</p>"""
    records_not_processed: NotRequired["int"]
    """<p>The total number of records that did not get processed.</p>"""
    delete_records_processed: NotRequired["int"]
    """<p>The number of records processed that were marked for deletion in the input file using the DELETE schema mapping field. These are the records to be removed from the ID mapping table.</p>"""
    total_mapped_records: NotRequired["int"]
    """<p> The total number of records that were mapped.</p>"""
    total_mapped_source_records: NotRequired["int"]
    """<p> The total number of mapped source records.</p>"""
    total_mapped_target_records: NotRequired["int"]
    """<p> The total number of distinct mapped target records.</p>"""
    unique_records_loaded: NotRequired["int"]
    """<p>The number of de-duplicated processed records across all runs, excluding deletion-related records. Duplicates are determined by the field marked as UNIQUE_ID in your schema mapping. Records sharing the same value in this field are considered duplicates. For example, if you specified "customer_id" as a UNIQUE_ID field and had three records with the same customer_id value, they would count as one unique record in this metric. </p>"""
    new_mapped_records: NotRequired["int"]
    """<p> The number of new mapped records.</p>"""
    new_mapped_source_records: NotRequired["int"]
    """<p> The number of new source records mapped.</p>"""
    new_mapped_target_records: NotRequired["int"]
    """<p> The number of new mapped target records.</p>"""
    new_unique_records_loaded: NotRequired["int"]
    """<p>The number of new unique records processed in the current job run, after removing duplicates. This metric excludes deletion-related records. Duplicates are determined by the field marked as UNIQUE_ID in your schema mapping. Records sharing the same value in this field are considered duplicates. For example, if your current run processes five new records with the same UNIQUE_ID value, they would count as one new unique record in this metric.</p>"""
    mapped_records_removed: NotRequired["int"]
    """<p> The number of mapped records removed.</p>"""
    mapped_source_records_removed: NotRequired["int"]
    """<p> The number of source records removed due to ID mapping.</p>"""
    mapped_target_records_removed: NotRequired["int"]
    """<p> The number of mapped target records removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingJobMetrics) -> dict:
    out: dict = {}
    if "input_records" in value:
        out["inputRecords"] = value["input_records"]
    if "total_records_processed" in value:
        out["totalRecordsProcessed"] = value["total_records_processed"]
    if "records_not_processed" in value:
        out["recordsNotProcessed"] = value["records_not_processed"]
    if "delete_records_processed" in value:
        out["deleteRecordsProcessed"] = value["delete_records_processed"]
    if "total_mapped_records" in value:
        out["totalMappedRecords"] = value["total_mapped_records"]
    if "total_mapped_source_records" in value:
        out["totalMappedSourceRecords"] = value["total_mapped_source_records"]
    if "total_mapped_target_records" in value:
        out["totalMappedTargetRecords"] = value["total_mapped_target_records"]
    if "unique_records_loaded" in value:
        out["uniqueRecordsLoaded"] = value["unique_records_loaded"]
    if "new_mapped_records" in value:
        out["newMappedRecords"] = value["new_mapped_records"]
    if "new_mapped_source_records" in value:
        out["newMappedSourceRecords"] = value["new_mapped_source_records"]
    if "new_mapped_target_records" in value:
        out["newMappedTargetRecords"] = value["new_mapped_target_records"]
    if "new_unique_records_loaded" in value:
        out["newUniqueRecordsLoaded"] = value["new_unique_records_loaded"]
    if "mapped_records_removed" in value:
        out["mappedRecordsRemoved"] = value["mapped_records_removed"]
    if "mapped_source_records_removed" in value:
        out["mappedSourceRecordsRemoved"] = value["mapped_source_records_removed"]
    if "mapped_target_records_removed" in value:
        out["mappedTargetRecordsRemoved"] = value["mapped_target_records_removed"]
    return out


def deserialize_json(data: dict) -> IdMappingJobMetrics:
    out: IdMappingJobMetrics = {}  # type: ignore[typeddict-item]
    if data.get("inputRecords") is not None:
        out["input_records"] = data["inputRecords"]
    if data.get("totalRecordsProcessed") is not None:
        out["total_records_processed"] = data["totalRecordsProcessed"]
    if data.get("recordsNotProcessed") is not None:
        out["records_not_processed"] = data["recordsNotProcessed"]
    if data.get("deleteRecordsProcessed") is not None:
        out["delete_records_processed"] = data["deleteRecordsProcessed"]
    if data.get("totalMappedRecords") is not None:
        out["total_mapped_records"] = data["totalMappedRecords"]
    if data.get("totalMappedSourceRecords") is not None:
        out["total_mapped_source_records"] = data["totalMappedSourceRecords"]
    if data.get("totalMappedTargetRecords") is not None:
        out["total_mapped_target_records"] = data["totalMappedTargetRecords"]
    if data.get("uniqueRecordsLoaded") is not None:
        out["unique_records_loaded"] = data["uniqueRecordsLoaded"]
    if data.get("newMappedRecords") is not None:
        out["new_mapped_records"] = data["newMappedRecords"]
    if data.get("newMappedSourceRecords") is not None:
        out["new_mapped_source_records"] = data["newMappedSourceRecords"]
    if data.get("newMappedTargetRecords") is not None:
        out["new_mapped_target_records"] = data["newMappedTargetRecords"]
    if data.get("newUniqueRecordsLoaded") is not None:
        out["new_unique_records_loaded"] = data["newUniqueRecordsLoaded"]
    if data.get("mappedRecordsRemoved") is not None:
        out["mapped_records_removed"] = data["mappedRecordsRemoved"]
    if data.get("mappedSourceRecordsRemoved") is not None:
        out["mapped_source_records_removed"] = data["mappedSourceRecordsRemoved"]
    if data.get("mappedTargetRecordsRemoved") is not None:
        out["mapped_target_records_removed"] = data["mappedTargetRecordsRemoved"]
    return out
