"""Generated from Smithy shape ``com.amazonaws.glue#GetEntityRecordsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.next_token
    import capo_glue.types.records


class GetEntityRecordsResponse(TypedDict, closed=True):
    records: NotRequired["capo_glue.types.records.Records"]
    """<p>A list of the requested objects.</p>"""
    next_token: NotRequired["capo_glue.types.next_token.NextToken"]
    """<p>A continuation token, present if the current segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntityRecordsResponse) -> dict:
    out: dict = {}
    if "records" in value:
        import capo_glue.types.records

        out["Records"] = capo_glue.types.records.serialize_aws_json_1_1(
            value["records"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntityRecordsResponse:
    out: GetEntityRecordsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Records") is not None:
        import capo_glue.types.records

        out["records"] = capo_glue.types.records.deserialize_aws_json_1_1(
            data["Records"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: GetEntityRecordsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "records" in value:
        out["records"] = "*** Sensitive Data Redacted ***"
    return out
