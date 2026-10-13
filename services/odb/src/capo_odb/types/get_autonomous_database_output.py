"""Generated from Smithy shape ``com.amazonaws.odb#GetAutonomousDatabaseOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database


class GetAutonomousDatabaseOutput(TypedDict, closed=True):
    autonomous_database: "capo_odb.types.autonomous_database.AutonomousDatabase"
    """<p>The details of the requested Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutonomousDatabaseOutput) -> dict:
    out: dict = {}
    import capo_odb.types.autonomous_database

    out["autonomousDatabase"] = (
        capo_odb.types.autonomous_database.serialize_aws_json_1_0(
            value["autonomous_database"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutonomousDatabaseOutput:
    out: GetAutonomousDatabaseOutput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabase") is not None:
        import capo_odb.types.autonomous_database

        out["autonomous_database"] = (
            capo_odb.types.autonomous_database.deserialize_aws_json_1_0(
                data["autonomousDatabase"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutonomousDatabaseOutput.autonomous_database required"
        )
    return out


def redact_sensitive(value: GetAutonomousDatabaseOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "autonomous_database" in value:
        import capo_odb.types.autonomous_database

        out["autonomous_database"] = (
            capo_odb.types.autonomous_database.redact_sensitive(
                value["autonomous_database"]
            )
        )
    return out
