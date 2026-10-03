"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#RollbackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__integer
    import capo_serverlessapplicationrepository.types.__list_of_rollback_trigger


class RollbackConfiguration(TypedDict, closed=True):
    monitoring_time_in_minutes: NotRequired[
        "capo_serverlessapplicationrepository.types.__integer.__integer"
    ]
    """<p>This property corresponds to the content of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration">RollbackConfiguration</a> </i> Data Type.</p>"""
    rollback_triggers: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of_rollback_trigger.__listOfRollbackTrigger"
    ]
    """<p>This property corresponds to the content of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration">RollbackConfiguration</a> </i> Data Type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackConfiguration) -> dict:
    out: dict = {}
    if "monitoring_time_in_minutes" in value:
        out["monitoringTimeInMinutes"] = value["monitoring_time_in_minutes"]
    if "rollback_triggers" in value:
        import capo_serverlessapplicationrepository.types.__list_of_rollback_trigger

        out["rollbackTriggers"] = (
            capo_serverlessapplicationrepository.types.__list_of_rollback_trigger.serialize_json(
                value["rollback_triggers"]
            )
        )
    return out


def deserialize_json(data: dict) -> RollbackConfiguration:
    out: RollbackConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("monitoringTimeInMinutes") is not None:
        out["monitoring_time_in_minutes"] = data["monitoringTimeInMinutes"]
    if data.get("rollbackTriggers") is not None:
        import capo_serverlessapplicationrepository.types.__list_of_rollback_trigger

        out["rollback_triggers"] = (
            capo_serverlessapplicationrepository.types.__list_of_rollback_trigger.deserialize_json(
                data["rollbackTriggers"]
            )
        )
    return out
