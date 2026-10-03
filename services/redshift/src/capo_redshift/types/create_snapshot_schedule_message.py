"""Generated from Smithy shape ``com.amazonaws.redshift#CreateSnapshotScheduleMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.integer_optional
    import capo_redshift.types.schedule_definition_list
    import capo_redshift.types.string
    import capo_redshift.types.tag_list


class CreateSnapshotScheduleMessage(TypedDict, closed=True):
    schedule_definitions: NotRequired[
        "capo_redshift.types.schedule_definition_list.ScheduleDefinitionList"
    ]
    """<p>The definition of the snapshot schedule. The definition is made up of schedule expressions, for example "cron(30 12 *)" or "rate(12 hours)". </p>"""
    schedule_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier for a snapshot schedule. Only alphanumeric characters are allowed for the identifier.</p>"""
    schedule_description: NotRequired["capo_redshift.types.string.String"]
    """<p>The description of the snapshot schedule.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>An optional set of tags you can use to search for the schedule.</p>"""
    dry_run: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p></p>"""
    next_invocations: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateSnapshotScheduleMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "schedule_definitions" in value:
        import capo_redshift.types.schedule_definition_list

        capo_redshift.types.schedule_definition_list.serialize_query(
            value["schedule_definitions"], pairs, f"{key_prefix}ScheduleDefinitions"
        )
    if "schedule_identifier" in value:
        pairs.append(
            (f"{key_prefix}ScheduleIdentifier", str(value["schedule_identifier"]))
        )
    if "schedule_description" in value:
        pairs.append(
            (f"{key_prefix}ScheduleDescription", str(value["schedule_description"]))
        )
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "next_invocations" in value:
        pairs.append((f"{key_prefix}NextInvocations", str(value["next_invocations"])))


def deserialize_query(el: Element) -> CreateSnapshotScheduleMessage:
    out: CreateSnapshotScheduleMessage = {}  # type: ignore[typeddict-item]
    child_schedule_definitions = el.find("ScheduleDefinitions")
    if child_schedule_definitions is not None:
        import capo_redshift.types.schedule_definition_list

        out["schedule_definitions"] = (
            capo_redshift.types.schedule_definition_list.deserialize_query(
                child_schedule_definitions
            )
        )
    child_schedule_identifier = el.find("ScheduleIdentifier")
    if child_schedule_identifier is not None:
        out["schedule_identifier"] = str(child_schedule_identifier.text or "")
    child_schedule_description = el.find("ScheduleDescription")
    if child_schedule_description is not None:
        out["schedule_description"] = str(child_schedule_description.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_next_invocations = el.find("NextInvocations")
    if child_next_invocations is not None:
        out["next_invocations"] = int(child_next_invocations.text or "")
    return out
