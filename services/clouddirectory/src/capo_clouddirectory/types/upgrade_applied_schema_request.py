"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpgradeAppliedSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.bool


class UpgradeAppliedSchemaRequest(TypedDict, closed=True):
    published_schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The revision of the published schema to upgrade the directory to.</p>"""
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN for the directory to which the upgraded schema will be applied.</p>"""
    dry_run: NotRequired["capo_clouddirectory.types.bool.Bool"]
    """<p>Used for testing whether the major version schemas are backward compatible or not. If schema compatibility fails, an exception would be thrown else the call would succeed but no changes will be saved. This parameter is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeAppliedSchemaRequest) -> dict:
    out: dict = {}
    out["PublishedSchemaArn"] = value["published_schema_arn"]
    out["DirectoryArn"] = value["directory_arn"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_json(data: dict) -> UpgradeAppliedSchemaRequest:
    out: UpgradeAppliedSchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("PublishedSchemaArn") is not None:
        out["published_schema_arn"] = data["PublishedSchemaArn"]
    else:
        out["published_schema_arn"] = ""
    if data.get("DirectoryArn") is not None:
        out["directory_arn"] = data["DirectoryArn"]
    else:
        out["directory_arn"] = ""
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
