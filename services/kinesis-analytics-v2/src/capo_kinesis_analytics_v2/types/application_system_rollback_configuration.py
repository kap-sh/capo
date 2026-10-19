"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSystemRollbackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.boolean_object


class ApplicationSystemRollbackConfiguration(TypedDict, closed=True):
    rollback_enabled: "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    """<p>Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSystemRollbackConfiguration) -> dict:
    out: dict = {}
    out["RollbackEnabled"] = value["rollback_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSystemRollbackConfiguration:
    out: ApplicationSystemRollbackConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RollbackEnabled") is not None:
        out["rollback_enabled"] = data["RollbackEnabled"]
    else:
        out["rollback_enabled"] = False
    return out
