"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpgradePublishedSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.bool
    import capo_clouddirectory.types.version


class UpgradePublishedSchemaRequest(TypedDict, closed=True):
    development_schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the development schema with the changes used for the upgrade.</p>"""
    published_schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the published schema to be upgraded.</p>"""
    minor_version: "capo_clouddirectory.types.version.Version"
    """<p>Identifies the minor version of the published schema that will be created. This parameter is NOT optional.</p>"""
    dry_run: NotRequired["capo_clouddirectory.types.bool.Bool"]
    """<p>Used for testing whether the Development schema provided is backwards compatible, or not, with the publish schema provided by the user to be upgraded. If schema compatibility fails, an exception would be thrown else the call would succeed. This parameter is optional and defaults to false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradePublishedSchemaRequest) -> dict:
    out: dict = {}
    out["DevelopmentSchemaArn"] = value["development_schema_arn"]
    out["PublishedSchemaArn"] = value["published_schema_arn"]
    out["MinorVersion"] = value["minor_version"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_json(data: dict) -> UpgradePublishedSchemaRequest:
    out: UpgradePublishedSchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("DevelopmentSchemaArn") is not None:
        out["development_schema_arn"] = data["DevelopmentSchemaArn"]
    else:
        raise DeserializationError(
            "UpgradePublishedSchemaRequest.development_schema_arn required"
        )
    if data.get("PublishedSchemaArn") is not None:
        out["published_schema_arn"] = data["PublishedSchemaArn"]
    else:
        raise DeserializationError(
            "UpgradePublishedSchemaRequest.published_schema_arn required"
        )
    if data.get("MinorVersion") is not None:
        out["minor_version"] = data["MinorVersion"]
    else:
        raise DeserializationError(
            "UpgradePublishedSchemaRequest.minor_version required"
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
