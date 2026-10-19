"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchDisassociateCodeSecurityScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.disassociate_configuration_request_list


class BatchDisassociateCodeSecurityScanConfigurationRequest(TypedDict, closed=True):
    disassociate_configuration_requests: "capo_inspector2.types.disassociate_configuration_request_list.DisassociateConfigurationRequestList"
    """<p>A list of code repositories to disassociate from the specified scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: BatchDisassociateCodeSecurityScanConfigurationRequest,
) -> dict:
    out: dict = {}
    import capo_inspector2.types.disassociate_configuration_request_list

    out["disassociateConfigurationRequests"] = (
        capo_inspector2.types.disassociate_configuration_request_list.serialize_json(
            value["disassociate_configuration_requests"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> BatchDisassociateCodeSecurityScanConfigurationRequest:
    out: BatchDisassociateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("disassociateConfigurationRequests") is not None:
        import capo_inspector2.types.disassociate_configuration_request_list

        out["disassociate_configuration_requests"] = (
            capo_inspector2.types.disassociate_configuration_request_list.deserialize_json(
                data["disassociateConfigurationRequests"]
            )
        )
    else:
        out["disassociate_configuration_requests"] = []
    return out
