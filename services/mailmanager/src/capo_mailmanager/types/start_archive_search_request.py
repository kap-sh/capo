"""Generated from Smithy shape ``com.amazonaws.mailmanager#StartArchiveSearchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.archive_filters
    import capo_mailmanager.types.archive_id
    import capo_mailmanager.types.search_max_results


class StartArchiveSearchRequest(TypedDict, closed=True):
    archive_id: "capo_mailmanager.types.archive_id.ArchiveId"
    """<p>The identifier of the archive to search emails in.</p>"""
    filters: NotRequired["capo_mailmanager.types.archive_filters.ArchiveFilters"]
    """<p>Criteria to filter which emails are included in the search results.</p>"""
    from_timestamp: "datetime.datetime"
    """<p>The start timestamp of the range to search emails from.</p>"""
    to_timestamp: "datetime.datetime"
    """<p>The end timestamp of the range to search emails from.</p>"""
    max_results: "capo_mailmanager.types.search_max_results.SearchMaxResults"
    """<p>The maximum number of search results to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartArchiveSearchRequest) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    if "filters" in value:
        import capo_mailmanager.types.archive_filters

        out["Filters"] = capo_mailmanager.types.archive_filters.serialize_aws_json_1_0(
            value["filters"]
        )
    import capo_mailmanager.types._prelude.timestamp

    out["FromTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["from_timestamp"]
        )
    )
    import capo_mailmanager.types._prelude.timestamp

    out["ToTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["to_timestamp"]
        )
    )
    out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartArchiveSearchRequest:
    out: StartArchiveSearchRequest = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    else:
        out["archive_id"] = ""
    if data.get("Filters") is not None:
        import capo_mailmanager.types.archive_filters

        out["filters"] = (
            capo_mailmanager.types.archive_filters.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if data.get("FromTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["from_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["FromTimestamp"]
            )
        )
    else:
        import datetime

        out["from_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ToTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["to_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ToTimestamp"]
            )
        )
    else:
        import datetime

        out["to_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    return out
