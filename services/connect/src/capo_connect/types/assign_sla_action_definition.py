"""Generated from Smithy shape ``com.amazonaws.connect#AssignSlaActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.case_sla_configuration
    import capo_connect.types.sla_assignment_type


class AssignSlaActionDefinition(TypedDict, closed=True):
    sla_assignment_type: "capo_connect.types.sla_assignment_type.SlaAssignmentType"
    """<p>Type of SLA assignment.</p>"""
    case_sla_configuration: NotRequired[
        "capo_connect.types.case_sla_configuration.CaseSlaConfiguration"
    ]
    """<p>The SLA configuration for Case SLA Assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssignSlaActionDefinition) -> dict:
    out: dict = {}
    import capo_connect.types.sla_assignment_type

    out["SlaAssignmentType"] = capo_connect.types.sla_assignment_type.serialize_json(
        value["sla_assignment_type"]
    )
    if "case_sla_configuration" in value:
        import capo_connect.types.case_sla_configuration

        out["CaseSlaConfiguration"] = (
            capo_connect.types.case_sla_configuration.serialize_json(
                value["case_sla_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssignSlaActionDefinition:
    out: AssignSlaActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("SlaAssignmentType") is not None:
        import capo_connect.types.sla_assignment_type

        out["sla_assignment_type"] = (
            capo_connect.types.sla_assignment_type.deserialize_json(
                data["SlaAssignmentType"]
            )
        )
    else:
        import typing

        out["sla_assignment_type"] = typing.cast(
            "capo_connect.types.sla_assignment_type.SlaAssignmentType", ""
        )
    if data.get("CaseSlaConfiguration") is not None:
        import capo_connect.types.case_sla_configuration

        out["case_sla_configuration"] = (
            capo_connect.types.case_sla_configuration.deserialize_json(
                data["CaseSlaConfiguration"]
            )
        )
    return out
