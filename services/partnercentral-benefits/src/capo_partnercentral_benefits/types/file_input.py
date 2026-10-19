"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.file_uri


class FileInput(TypedDict, closed=True):
    file_uri: "capo_partnercentral_benefits.types.file_uri.FileURI"
    """<p>The URI or location where the file should be stored or has been uploaded.</p>"""
    business_use_case: NotRequired["str"]
    """<p>The business purpose or use case that this file supports in the benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FileInput) -> dict:
    out: dict = {}
    out["FileURI"] = value["file_uri"]
    if "business_use_case" in value:
        out["BusinessUseCase"] = value["business_use_case"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FileInput:
    out: FileInput = {}  # type: ignore[typeddict-item]
    if data.get("FileURI") is not None:
        out["file_uri"] = data["FileURI"]
    else:
        out["file_uri"] = ""
    if data.get("BusinessUseCase") is not None:
        out["business_use_case"] = data["BusinessUseCase"]
    return out
