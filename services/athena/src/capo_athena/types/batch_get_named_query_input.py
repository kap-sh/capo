"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetNamedQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.named_query_id_list


class BatchGetNamedQueryInput(TypedDict, closed=True):
    named_query_ids: "capo_athena.types.named_query_id_list.NamedQueryIdList"
    """<p>An array of query IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetNamedQueryInput) -> dict:
    out: dict = {}
    import capo_athena.types.named_query_id_list

    out["NamedQueryIds"] = capo_athena.types.named_query_id_list.serialize_aws_json_1_1(
        value["named_query_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetNamedQueryInput:
    out: BatchGetNamedQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("NamedQueryIds") is not None:
        import capo_athena.types.named_query_id_list

        out["named_query_ids"] = (
            capo_athena.types.named_query_id_list.deserialize_aws_json_1_1(
                data["NamedQueryIds"]
            )
        )
    else:
        out["named_query_ids"] = []
    return out
