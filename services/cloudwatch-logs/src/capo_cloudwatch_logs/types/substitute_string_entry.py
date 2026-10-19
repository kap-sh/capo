"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SubstituteStringEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.from_key
    import capo_cloudwatch_logs.types.source
    import capo_cloudwatch_logs.types.to_key

SubstituteStringEntry = TypedDict(
    "SubstituteStringEntry",
    {
        "source": "capo_cloudwatch_logs.types.source.Source",
        "from": "capo_cloudwatch_logs.types.from_key.FromKey",
        "to": "capo_cloudwatch_logs.types.to_key.ToKey",
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubstituteStringEntry) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["from"] = value["from"]
    out["to"] = value["to"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubstituteStringEntry:
    out: SubstituteStringEntry = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("from") is not None:
        out["from"] = data["from"]
    else:
        out["from"] = ""
    if data.get("to") is not None:
        out["to"] = data["to"]
    else:
        out["to"] = ""
    return out
