"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#MpaTeamAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.association_state
    import capo_payment_cryptography.types.mpa_operation
    import capo_payment_cryptography.types.mpa_status
    import capo_payment_cryptography.types.mpa_team_arn


class MpaTeamAssociation(TypedDict, closed=True):
    action: "capo_payment_cryptography.types.mpa_operation.MpaOperation"
    """<p>The protected operation associated with the MPA team.</p>"""
    mpa_team_arn: "capo_payment_cryptography.types.mpa_team_arn.MpaTeamArn"
    """<p>The ARN of the MPA team.</p>"""
    association_state: (
        "capo_payment_cryptography.types.association_state.AssociationState"
    )
    """<p>The state of the MPA team association.</p>"""
    mpa_status: NotRequired["capo_payment_cryptography.types.mpa_status.MpaStatus"]
    """<p>The MPA session status for the association, if applicable.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MpaTeamAssociation) -> dict:
    out: dict = {}
    out["Action"] = value["action"]
    out["MpaTeamArn"] = value["mpa_team_arn"]
    out["AssociationState"] = value["association_state"]
    if "mpa_status" in value:
        import capo_payment_cryptography.types.mpa_status

        out["MpaStatus"] = (
            capo_payment_cryptography.types.mpa_status.serialize_aws_json_1_0(
                value["mpa_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MpaTeamAssociation:
    out: MpaTeamAssociation = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        out["action"] = ""
    if data.get("MpaTeamArn") is not None:
        out["mpa_team_arn"] = data["MpaTeamArn"]
    else:
        out["mpa_team_arn"] = ""
    if data.get("AssociationState") is not None:
        out["association_state"] = data["AssociationState"]
    else:
        out["association_state"] = ""
    if data.get("MpaStatus") is not None:
        import capo_payment_cryptography.types.mpa_status

        out["mpa_status"] = (
            capo_payment_cryptography.types.mpa_status.deserialize_aws_json_1_0(
                data["MpaStatus"]
            )
        )
    return out
