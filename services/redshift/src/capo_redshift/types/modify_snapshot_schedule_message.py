"""Generated from Smithy shape ``com.amazonaws.redshift#ModifySnapshotScheduleMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.schedule_definition_list
    import capo_redshift.types.string


class ModifySnapshotScheduleMessage(TypedDict, closed=True):
    schedule_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique alphanumeric identifier of the schedule to modify.</p>"""
    schedule_definitions: NotRequired[
        "capo_redshift.types.schedule_definition_list.ScheduleDefinitionList"
    ]
    """<p>An updated list of schedule definitions. A schedule definition is made up of schedule expressions, for example, "cron(30 12 *)" or "rate(12 hours)".</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifySnapshotScheduleMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "schedule_identifier" in value:
        pairs.append(
            (f"{key_prefix}ScheduleIdentifier", str(value["schedule_identifier"]))
        )
    if "schedule_definitions" in value:
        import capo_redshift.types.schedule_definition_list

        capo_redshift.types.schedule_definition_list.serialize_query(
            value["schedule_definitions"], pairs, f"{key_prefix}ScheduleDefinitions"
        )


def deserialize_query(el: Element) -> ModifySnapshotScheduleMessage:
    out: ModifySnapshotScheduleMessage = {}  # type: ignore[typeddict-item]
    child_schedule_identifier = el.find("ScheduleIdentifier")
    if child_schedule_identifier is not None:
        out["schedule_identifier"] = str(child_schedule_identifier.text or "")
    child_schedule_definitions = el.find("ScheduleDefinitions")
    if child_schedule_definitions is not None:
        import capo_redshift.types.schedule_definition_list

        out["schedule_definitions"] = (
            capo_redshift.types.schedule_definition_list.deserialize_query(
                child_schedule_definitions
            )
        )
    return out
