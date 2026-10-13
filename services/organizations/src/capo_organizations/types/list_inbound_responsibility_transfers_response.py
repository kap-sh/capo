"""Generated from Smithy shape ``com.amazonaws.organizations#ListInboundResponsibilityTransfersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.next_token
    import capo_organizations.types.responsibility_transfers


class ListInboundResponsibilityTransfersResponse(TypedDict, closed=True):
    responsibility_transfers: NotRequired[
        "capo_organizations.types.responsibility_transfers.ResponsibilityTransfers"
    ]
    """<p>A <code>ResponsibilityTransfers</code> object. Contains details for a transfer.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInboundResponsibilityTransfersResponse) -> dict:
    out: dict = {}
    if "responsibility_transfers" in value:
        import capo_organizations.types.responsibility_transfers

        out["ResponsibilityTransfers"] = (
            capo_organizations.types.responsibility_transfers.serialize_aws_json_1_1(
                value["responsibility_transfers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInboundResponsibilityTransfersResponse:
    out: ListInboundResponsibilityTransfersResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResponsibilityTransfers") is not None:
        import capo_organizations.types.responsibility_transfers

        out["responsibility_transfers"] = (
            capo_organizations.types.responsibility_transfers.deserialize_aws_json_1_1(
                data["ResponsibilityTransfers"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: ListInboundResponsibilityTransfersResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "responsibility_transfers" in value:
        import capo_organizations.types.responsibility_transfers

        out["responsibility_transfers"] = (
            capo_organizations.types.responsibility_transfers.redact_sensitive(
                value["responsibility_transfers"]
            )
        )
    return out
