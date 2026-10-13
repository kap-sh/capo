"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetDatabaseOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.database
    import capo_ssm_sap.types.tag_map


class GetDatabaseOutput(TypedDict, closed=True):
    database: NotRequired["capo_ssm_sap.types.database.Database"]
    """<p>The SAP HANA database of an application registered with AWS Systems Manager for SAP.</p>"""
    tags: NotRequired["capo_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags of a database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatabaseOutput) -> dict:
    out: dict = {}
    if "database" in value:
        import capo_ssm_sap.types.database

        out["Database"] = capo_ssm_sap.types.database.serialize_json(value["database"])
    if "tags" in value:
        import capo_ssm_sap.types.tag_map

        out["Tags"] = capo_ssm_sap.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetDatabaseOutput:
    out: GetDatabaseOutput = {}  # type: ignore[typeddict-item]
    if data.get("Database") is not None:
        import capo_ssm_sap.types.database

        out["database"] = capo_ssm_sap.types.database.deserialize_json(data["Database"])
    if data.get("Tags") is not None:
        import capo_ssm_sap.types.tag_map

        out["tags"] = capo_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: GetDatabaseOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "database" in value:
        import capo_ssm_sap.types.database

        out["database"] = capo_ssm_sap.types.database.redact_sensitive(
            value["database"]
        )
    return out
