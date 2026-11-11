"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database


class GetRelationalDatabaseResult(TypedDict, closed=True):
    relational_database: NotRequired[
        "capo_lightsail.types.relational_database.RelationalDatabase"
    ]
    """<p>An object describing the specified database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseResult) -> dict:
    out: dict = {}
    if "relational_database" in value:
        import capo_lightsail.types.relational_database

        out["relationalDatabase"] = (
            capo_lightsail.types.relational_database.serialize_aws_json_1_1(
                value["relational_database"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseResult:
    out: GetRelationalDatabaseResult = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabase") is not None:
        import capo_lightsail.types.relational_database

        out["relational_database"] = (
            capo_lightsail.types.relational_database.deserialize_aws_json_1_1(
                data["relationalDatabase"]
            )
        )
    return out


def redact_sensitive(value: GetRelationalDatabaseResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "relational_database" in value:
        import capo_lightsail.types.relational_database

        out["relational_database"] = (
            capo_lightsail.types.relational_database.redact_sensitive(
                value["relational_database"]
            )
        )
    return out
