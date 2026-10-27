"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListAttachmentNatConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_nat_configuration_list
    import capo_networkmanager.types.next_token


class ListAttachmentNatConfigurationsResponse(TypedDict, closed=True):
    attachment_nat_configurations: "capo_networkmanager.types.attachment_nat_configuration_list.AttachmentNatConfigurationList"
    """<p>The NAT configurations of the attachments.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentNatConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_networkmanager.types.attachment_nat_configuration_list

    out["AttachmentNatConfigurations"] = (
        capo_networkmanager.types.attachment_nat_configuration_list.serialize_json(
            value["attachment_nat_configurations"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachmentNatConfigurationsResponse:
    out: ListAttachmentNatConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AttachmentNatConfigurations") is not None:
        import capo_networkmanager.types.attachment_nat_configuration_list

        out["attachment_nat_configurations"] = (
            capo_networkmanager.types.attachment_nat_configuration_list.deserialize_json(
                data["AttachmentNatConfigurations"]
            )
        )
    else:
        out["attachment_nat_configurations"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
