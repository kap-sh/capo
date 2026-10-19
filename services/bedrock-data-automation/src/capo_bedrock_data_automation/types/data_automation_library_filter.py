"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_arn


class DataAutomationLibraryFilter(TypedDict, closed=True):
    library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryFilter) -> dict:
    out: dict = {}
    out["libraryArn"] = value["library_arn"]
    return out


def deserialize_json(data: dict) -> DataAutomationLibraryFilter:
    out: DataAutomationLibraryFilter = {}  # type: ignore[typeddict-item]
    if data.get("libraryArn") is not None:
        out["library_arn"] = data["libraryArn"]
    else:
        out["library_arn"] = ""
    return out
