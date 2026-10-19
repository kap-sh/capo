"""Generated from Smithy shape ``com.amazonaws.backupsearch#GetSearchJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backupsearch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_backupsearch.types.current_search_progress
    import capo_backupsearch.types.encryption_key_arn
    import capo_backupsearch.types.generic_id
    import capo_backupsearch.types.item_filters
    import capo_backupsearch.types.search_job_arn
    import capo_backupsearch.types.search_job_state
    import capo_backupsearch.types.search_scope
    import capo_backupsearch.types.search_scope_summary


class GetSearchJobOutput(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>Returned name of the specified search job.</p>"""
    search_scope_summary: NotRequired[
        "capo_backupsearch.types.search_scope_summary.SearchScopeSummary"
    ]
    """<p>Returned summary of the specified search job scope, including: </p> <ul> <li> <p>TotalBackupsToScanCount, the number of recovery points returned by the search.</p> </li> <li> <p>TotalItemsToScanCount, the number of items returned by the search.</p> </li> </ul>"""
    current_search_progress: NotRequired[
        "capo_backupsearch.types.current_search_progress.CurrentSearchProgress"
    ]
    """<p>Returns numbers representing BackupsScannedCount, ItemsScanned, and ItemsMatched.</p>"""
    status_message: NotRequired["str"]
    """<p>A status message will be returned for either a earch job with a status of <code>ERRORED</code> or a status of <code>COMPLETED</code> jobs with issues.</p> <p>For example, a message may say that a search contained recovery points unable to be scanned because of a permissions issue.</p>"""
    encryption_key_arn: NotRequired[
        "capo_backupsearch.types.encryption_key_arn.EncryptionKeyArn"
    ]
    """<p>The encryption key for the specified search job.</p> <p>Example: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>The date and time that a search job completed, in Unix format and Coordinated Universal Time (UTC). The value of <code>CompletionTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    status: "capo_backupsearch.types.search_job_state.SearchJobState"
    """<p>The current status of the specified search job.</p> <p>A search job may have one of the following statuses: <code>RUNNING</code>; <code>COMPLETED</code>; <code>STOPPED</code>; <code>FAILED</code>; <code>TIMED_OUT</code>; or <code>EXPIRED</code> .</p>"""
    search_scope: "capo_backupsearch.types.search_scope.SearchScope"
    """<p>The search scope is all backup properties input into a search.</p>"""
    item_filters: "capo_backupsearch.types.item_filters.ItemFilters"
    """<p>Item Filters represent all input item properties specified when the search was created.</p>"""
    creation_time: "datetime.datetime"
    """<p>The date and time that a search job was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CompletionTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    search_job_identifier: "capo_backupsearch.types.generic_id.GenericId"
    """<p>The unique string that identifies the specified search job.</p>"""
    search_job_arn: "capo_backupsearch.types.search_job_arn.SearchJobArn"
    """<p>The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSearchJobOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "search_scope_summary" in value:
        import capo_backupsearch.types.search_scope_summary

        out["SearchScopeSummary"] = (
            capo_backupsearch.types.search_scope_summary.serialize_json(
                value["search_scope_summary"]
            )
        )
    if "current_search_progress" in value:
        import capo_backupsearch.types.current_search_progress

        out["CurrentSearchProgress"] = (
            capo_backupsearch.types.current_search_progress.serialize_json(
                value["current_search_progress"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "completion_time" in value:
        import capo_backupsearch.types._prelude.timestamp

        out["CompletionTime"] = (
            capo_backupsearch.types._prelude.timestamp.serialize_json(
                value["completion_time"]
            )
        )
    import capo_backupsearch.types.search_job_state

    out["Status"] = capo_backupsearch.types.search_job_state.serialize_json(
        value["status"]
    )
    import capo_backupsearch.types.search_scope

    out["SearchScope"] = capo_backupsearch.types.search_scope.serialize_json(
        value["search_scope"]
    )
    import capo_backupsearch.types.item_filters

    out["ItemFilters"] = capo_backupsearch.types.item_filters.serialize_json(
        value["item_filters"]
    )
    import capo_backupsearch.types._prelude.timestamp

    out["CreationTime"] = capo_backupsearch.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["SearchJobIdentifier"] = value["search_job_identifier"]
    out["SearchJobArn"] = value["search_job_arn"]
    return out


def deserialize_json(data: dict) -> GetSearchJobOutput:
    out: GetSearchJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SearchScopeSummary") is not None:
        import capo_backupsearch.types.search_scope_summary

        out["search_scope_summary"] = (
            capo_backupsearch.types.search_scope_summary.deserialize_json(
                data["SearchScopeSummary"]
            )
        )
    if data.get("CurrentSearchProgress") is not None:
        import capo_backupsearch.types.current_search_progress

        out["current_search_progress"] = (
            capo_backupsearch.types.current_search_progress.deserialize_json(
                data["CurrentSearchProgress"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("CompletionTime") is not None:
        import capo_backupsearch.types._prelude.timestamp

        out["completion_time"] = (
            capo_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CompletionTime"]
            )
        )
    if data.get("Status") is not None:
        import capo_backupsearch.types.search_job_state

        out["status"] = capo_backupsearch.types.search_job_state.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_backupsearch.types.search_job_state.SearchJobState", ""
        )
    if data.get("SearchScope") is not None:
        import capo_backupsearch.types.search_scope

        out["search_scope"] = capo_backupsearch.types.search_scope.deserialize_json(
            data["SearchScope"]
        )
    else:
        raise DeserializationError("GetSearchJobOutput.search_scope required")
    if data.get("ItemFilters") is not None:
        import capo_backupsearch.types.item_filters

        out["item_filters"] = capo_backupsearch.types.item_filters.deserialize_json(
            data["ItemFilters"]
        )
    else:
        raise DeserializationError("GetSearchJobOutput.item_filters required")
    if data.get("CreationTime") is not None:
        import capo_backupsearch.types._prelude.timestamp

        out["creation_time"] = (
            capo_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("SearchJobIdentifier") is not None:
        out["search_job_identifier"] = data["SearchJobIdentifier"]
    else:
        out["search_job_identifier"] = ""
    if data.get("SearchJobArn") is not None:
        out["search_job_arn"] = data["SearchJobArn"]
    else:
        out["search_job_arn"] = ""
    return out
