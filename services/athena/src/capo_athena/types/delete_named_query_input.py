"""Generated from Smithy shape ``com.amazonaws.athena#DeleteNamedQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.named_query_id


class DeleteNamedQueryInput(TypedDict, closed=True):
    named_query_id: "capo_athena.types.named_query_id.NamedQueryId"
    """<p>The unique ID of the query to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNamedQueryInput) -> dict:
    out: dict = {}
    out["NamedQueryId"] = value["named_query_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNamedQueryInput:
    out: DeleteNamedQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("NamedQueryId") is not None:
        out["named_query_id"] = data["NamedQueryId"]
    else:
        out["named_query_id"] = ""
    return out
