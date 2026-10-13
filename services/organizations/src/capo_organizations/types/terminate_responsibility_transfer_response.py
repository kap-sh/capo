"""Generated from Smithy shape ``com.amazonaws.organizations#TerminateResponsibilityTransferResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.responsibility_transfer


class TerminateResponsibilityTransferResponse(TypedDict, closed=True):
    responsibility_transfer: NotRequired[
        "capo_organizations.types.responsibility_transfer.ResponsibilityTransfer"
    ]
    """<p>A <code>ResponsibilityTransfer</code> object. Contains details for a transfer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateResponsibilityTransferResponse) -> dict:
    out: dict = {}
    if "responsibility_transfer" in value:
        import capo_organizations.types.responsibility_transfer

        out["ResponsibilityTransfer"] = (
            capo_organizations.types.responsibility_transfer.serialize_aws_json_1_1(
                value["responsibility_transfer"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateResponsibilityTransferResponse:
    out: TerminateResponsibilityTransferResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResponsibilityTransfer") is not None:
        import capo_organizations.types.responsibility_transfer

        out["responsibility_transfer"] = (
            capo_organizations.types.responsibility_transfer.deserialize_aws_json_1_1(
                data["ResponsibilityTransfer"]
            )
        )
    return out


def redact_sensitive(value: TerminateResponsibilityTransferResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "responsibility_transfer" in value:
        import capo_organizations.types.responsibility_transfer

        out["responsibility_transfer"] = (
            capo_organizations.types.responsibility_transfer.redact_sensitive(
                value["responsibility_transfer"]
            )
        )
    return out
