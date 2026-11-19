"""Generated from Smithy shape ``com.amazonaws.fms#PossibleRemediationActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string
    import capo_fms.types.possible_remediation_action_list


class PossibleRemediationActions(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>A description of the possible remediation actions list.</p>"""
    actions: NotRequired[
        "capo_fms.types.possible_remediation_action_list.PossibleRemediationActionList"
    ]
    """<p>Information about the actions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PossibleRemediationActions) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "actions" in value:
        import capo_fms.types.possible_remediation_action_list

        out["Actions"] = (
            capo_fms.types.possible_remediation_action_list.serialize_aws_json_1_1(
                value["actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PossibleRemediationActions:
    out: PossibleRemediationActions = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Actions") is not None:
        import capo_fms.types.possible_remediation_action_list

        out["actions"] = (
            capo_fms.types.possible_remediation_action_list.deserialize_aws_json_1_1(
                data["Actions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PossibleRemediationActions) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "actions" in value:
        import capo_fms.types.possible_remediation_action_list

        out["Actions"] = capo_fms.types.possible_remediation_action_list.serialize_cbor(
            value["actions"]
        )
    return out


def deserialize_cbor(data: dict) -> PossibleRemediationActions:
    out: PossibleRemediationActions = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Actions") is not None:
        import capo_fms.types.possible_remediation_action_list

        out["actions"] = (
            capo_fms.types.possible_remediation_action_list.deserialize_cbor(
                data["Actions"]
            )
        )
    return out
