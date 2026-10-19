"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListAddressListImportJobsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.import_jobs
    import capo_mailmanager.types.pagination_token


class ListAddressListImportJobsResponse(TypedDict, closed=True):
    import_jobs: "capo_mailmanager.types.import_jobs.ImportJobs"
    """<p>The list of import jobs.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAddressListImportJobsResponse) -> dict:
    out: dict = {}
    import capo_mailmanager.types.import_jobs

    out["ImportJobs"] = capo_mailmanager.types.import_jobs.serialize_aws_json_1_0(
        value["import_jobs"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAddressListImportJobsResponse:
    out: ListAddressListImportJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ImportJobs") is not None:
        import capo_mailmanager.types.import_jobs

        out["import_jobs"] = (
            capo_mailmanager.types.import_jobs.deserialize_aws_json_1_0(
                data["ImportJobs"]
            )
        )
    else:
        out["import_jobs"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAddressListImportJobsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "import_jobs" in value:
        import capo_mailmanager.types.import_jobs

        out["import_jobs"] = capo_mailmanager.types.import_jobs.redact_sensitive(
            value["import_jobs"]
        )
    return out
