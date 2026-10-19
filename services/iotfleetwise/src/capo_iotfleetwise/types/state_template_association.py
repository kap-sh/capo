"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.resource_identifier
    import capo_iotfleetwise.types.state_template_update_strategy


class StateTemplateAssociation(TypedDict, closed=True):
    identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier"
    """<p>The unique ID of the state template.</p>"""
    state_template_update_strategy: "capo_iotfleetwise.types.state_template_update_strategy.StateTemplateUpdateStrategy"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateAssociation) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    import capo_iotfleetwise.types.state_template_update_strategy

    out["stateTemplateUpdateStrategy"] = (
        capo_iotfleetwise.types.state_template_update_strategy.serialize_aws_json_1_0(
            value["state_template_update_strategy"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StateTemplateAssociation:
    out: StateTemplateAssociation = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("stateTemplateUpdateStrategy") is not None:
        import capo_iotfleetwise.types.state_template_update_strategy

        out["state_template_update_strategy"] = (
            capo_iotfleetwise.types.state_template_update_strategy.deserialize_aws_json_1_0(
                data["stateTemplateUpdateStrategy"]
            )
        )
    else:
        import capo_iotfleetwise.types._unknown

        out["state_template_update_strategy"] = (
            capo_iotfleetwise.types._unknown.UnknownUnionMember("")
        )
    return out
