"""Generated from Smithy shape ``com.amazonaws.guardduty#CountermeasureAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.action_priority
    import capo_guardduty.types.cli_commands
    import capo_guardduty.types.disposition
    import capo_guardduty.types.integer
    import capo_guardduty.types.mitre_technique_ids
    import capo_guardduty.types.remediation_affected_resources
    import capo_guardduty.types.string


class CountermeasureAction(TypedDict, closed=True):
    title: NotRequired["capo_guardduty.types.string.String"]
    """<p>A short title for the action.</p>"""
    description: NotRequired["capo_guardduty.types.string.String"]
    """<p>A description of the action.</p>"""
    priority: NotRequired["capo_guardduty.types.action_priority.ActionPriority"]
    """<p>The priority of the action. Possible values are <code>IMMEDIATE</code>, <code>SHORT_TERM</code>, and <code>STRATEGIC</code>.</p>"""
    defense_technique: NotRequired["capo_guardduty.types.string.String"]
    """<p>The defensive technique that the action applies.</p>"""
    mitigates: NotRequired["capo_guardduty.types.mitre_technique_ids.MitreTechniqueIds"]
    """<p>The MITRE ATT&amp;CK technique IDs that the action mitigates, such as <code>T1059.004</code>.</p>"""
    cli_commands: NotRequired["capo_guardduty.types.cli_commands.CliCommands"]
    """<p>CLI commands that you can run to carry out the action.</p>"""
    disposition_id: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The numeric identifier of the action's disposition.</p>"""
    disposition: NotRequired["capo_guardduty.types.disposition.Disposition"]
    """<p>The outcome of the action. Possible values are <code>Isolated</code>, <code>Blocked</code>, <code>Deleted</code>, <code>Access Revoked</code>, and <code>Logged</code>.</p>"""
    affected_resources: NotRequired[
        "capo_guardduty.types.remediation_affected_resources.RemediationAffectedResources"
    ]
    """<p>The resources that the action applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CountermeasureAction) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "priority" in value:
        import capo_guardduty.types.action_priority

        out["priority"] = capo_guardduty.types.action_priority.serialize_json(
            value["priority"]
        )
    if "defense_technique" in value:
        out["defenseTechnique"] = value["defense_technique"]
    if "mitigates" in value:
        import capo_guardduty.types.mitre_technique_ids

        out["mitigates"] = capo_guardduty.types.mitre_technique_ids.serialize_json(
            value["mitigates"]
        )
    if "cli_commands" in value:
        import capo_guardduty.types.cli_commands

        out["cliCommands"] = capo_guardduty.types.cli_commands.serialize_json(
            value["cli_commands"]
        )
    if "disposition_id" in value:
        out["dispositionId"] = value["disposition_id"]
    if "disposition" in value:
        import capo_guardduty.types.disposition

        out["disposition"] = capo_guardduty.types.disposition.serialize_json(
            value["disposition"]
        )
    if "affected_resources" in value:
        import capo_guardduty.types.remediation_affected_resources

        out["affectedResources"] = (
            capo_guardduty.types.remediation_affected_resources.serialize_json(
                value["affected_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> CountermeasureAction:
    out: CountermeasureAction = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("priority") is not None:
        import capo_guardduty.types.action_priority

        out["priority"] = capo_guardduty.types.action_priority.deserialize_json(
            data["priority"]
        )
    if data.get("defenseTechnique") is not None:
        out["defense_technique"] = data["defenseTechnique"]
    if data.get("mitigates") is not None:
        import capo_guardduty.types.mitre_technique_ids

        out["mitigates"] = capo_guardduty.types.mitre_technique_ids.deserialize_json(
            data["mitigates"]
        )
    if data.get("cliCommands") is not None:
        import capo_guardduty.types.cli_commands

        out["cli_commands"] = capo_guardduty.types.cli_commands.deserialize_json(
            data["cliCommands"]
        )
    if data.get("dispositionId") is not None:
        out["disposition_id"] = data["dispositionId"]
    if data.get("disposition") is not None:
        import capo_guardduty.types.disposition

        out["disposition"] = capo_guardduty.types.disposition.deserialize_json(
            data["disposition"]
        )
    if data.get("affectedResources") is not None:
        import capo_guardduty.types.remediation_affected_resources

        out["affected_resources"] = (
            capo_guardduty.types.remediation_affected_resources.deserialize_json(
                data["affectedResources"]
            )
        )
    return out
