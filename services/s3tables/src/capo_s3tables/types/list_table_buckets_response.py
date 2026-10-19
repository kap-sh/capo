"""Generated from Smithy shape ``com.amazonaws.s3tables#ListTableBucketsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.next_token
    import capo_s3tables.types.table_bucket_summary_list


class ListTableBucketsResponse(TypedDict, closed=True):
    table_buckets: (
        "capo_s3tables.types.table_bucket_summary_list.TableBucketSummaryList"
    )
    """<p>A list of table buckets.</p>"""
    continuation_token: NotRequired["capo_s3tables.types.next_token.NextToken"]
    """<p>You can use this <code>ContinuationToken</code> for pagination of the list results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTableBucketsResponse) -> dict:
    out: dict = {}
    import capo_s3tables.types.table_bucket_summary_list

    out["tableBuckets"] = capo_s3tables.types.table_bucket_summary_list.serialize_json(
        value["table_buckets"]
    )
    if "continuation_token" in value:
        out["continuationToken"] = value["continuation_token"]
    return out


def deserialize_json(data: dict) -> ListTableBucketsResponse:
    out: ListTableBucketsResponse = {}  # type: ignore[typeddict-item]
    if data.get("tableBuckets") is not None:
        import capo_s3tables.types.table_bucket_summary_list

        out["table_buckets"] = (
            capo_s3tables.types.table_bucket_summary_list.deserialize_json(
                data["tableBuckets"]
            )
        )
    else:
        out["table_buckets"] = []
    if data.get("continuationToken") is not None:
        out["continuation_token"] = data["continuationToken"]
    return out
