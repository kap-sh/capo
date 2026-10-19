"""Generated from Smithy shape ``com.amazonaws.textract#QueriesConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.queries


class QueriesConfig(TypedDict, closed=True):
    queries: "capo_textract.types.queries.Queries"
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueriesConfig) -> dict:
    out: dict = {}
    import capo_textract.types.queries

    out["Queries"] = capo_textract.types.queries.serialize_aws_json_1_1(
        value["queries"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueriesConfig:
    out: QueriesConfig = {}  # type: ignore[typeddict-item]
    if data.get("Queries") is not None:
        import capo_textract.types.queries

        out["queries"] = capo_textract.types.queries.deserialize_aws_json_1_1(
            data["Queries"]
        )
    else:
        out["queries"] = []
    return out
