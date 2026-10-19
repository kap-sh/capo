"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionDestinationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.arn


class IngestionDestinationSummary(TypedDict, closed=True):
    arn: "capo_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the ingestion destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionDestinationSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> IngestionDestinationSummary:
    out: IngestionDestinationSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
