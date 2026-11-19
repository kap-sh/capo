"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateAliasResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.alias_name
    import capo_directory_service.types.directory_id


class CreateAliasResult(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory.</p>"""
    alias: NotRequired["capo_directory_service.types.alias_name.AliasName"]
    """<p>The alias for the directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAliasResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAliasResult:
    out: CreateAliasResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAliasResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    return out


def deserialize_cbor(data: dict) -> CreateAliasResult:
    out: CreateAliasResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    return out
