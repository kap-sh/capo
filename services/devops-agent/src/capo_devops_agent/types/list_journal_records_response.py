"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListJournalRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.journal_record_list


class ListJournalRecordsResponse(TypedDict, closed=True):
    records: "capo_devops_agent.types.journal_record_list.JournalRecordList"
    """<p>List of journal records matching the request criteria</p>"""
    next_token: NotRequired["str"]
    """<p>Token for retrieving the next page of results, if more results are available</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJournalRecordsResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.journal_record_list

    out["records"] = capo_devops_agent.types.journal_record_list.serialize_json(
        value["records"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJournalRecordsResponse:
    out: ListJournalRecordsResponse = {}  # type: ignore[typeddict-item]
    if data.get("records") is not None:
        import capo_devops_agent.types.journal_record_list

        out["records"] = capo_devops_agent.types.journal_record_list.deserialize_json(
            data["records"]
        )
    else:
        out["records"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
