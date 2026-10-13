"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpdateDataAutomationLibraryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.data_automation_library_arn
    import capo_bedrock_data_automation.types.data_automation_library_description


class UpdateDataAutomationLibraryRequest(TypedDict, closed=True):
    library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    """ARN generated at the server side when a DataAutomationLibrary is created"""
    library_description: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
    ]
    client_token: NotRequired[
        "capo_bedrock_data_automation.types.client_token.ClientToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataAutomationLibraryRequest) -> dict:
    out: dict = {}
    if "library_description" in value:
        out["libraryDescription"] = value["library_description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateDataAutomationLibraryRequest:
    out: UpdateDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
    if data.get("libraryDescription") is not None:
        out["library_description"] = data["libraryDescription"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: UpdateDataAutomationLibraryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "library_description" in value:
        out["library_description"] = "*** Sensitive Data Redacted ***"
    return out
