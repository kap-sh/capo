"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StatementProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class StatementProperties(TypedDict, closed=True):
    definition: "capo_database_migration_service.types.string.String"
    """<p>The SQL text of the statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatementProperties) -> dict:
    out: dict = {}
    out["Definition"] = value["definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StatementProperties:
    out: StatementProperties = {}  # type: ignore[typeddict-item]
    if data.get("Definition") is not None:
        out["definition"] = data["Definition"]
    else:
        out["definition"] = ""
    return out
