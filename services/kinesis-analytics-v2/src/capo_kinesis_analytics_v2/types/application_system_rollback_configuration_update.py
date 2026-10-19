"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSystemRollbackConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.boolean_object


class ApplicationSystemRollbackConfigurationUpdate(TypedDict, closed=True):
    rollback_enabled_update: (
        "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    )
    """<p>Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSystemRollbackConfigurationUpdate) -> dict:
    out: dict = {}
    out["RollbackEnabledUpdate"] = value["rollback_enabled_update"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ApplicationSystemRollbackConfigurationUpdate:
    out: ApplicationSystemRollbackConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("RollbackEnabledUpdate") is not None:
        out["rollback_enabled_update"] = data["RollbackEnabledUpdate"]
    else:
        out["rollback_enabled_update"] = False
    return out
