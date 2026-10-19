"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchAssociateCodeSecurityScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.associate_configuration_request_list


class BatchAssociateCodeSecurityScanConfigurationRequest(TypedDict, closed=True):
    associate_configuration_requests: "capo_inspector2.types.associate_configuration_request_list.AssociateConfigurationRequestList"
    """<p>A list of code repositories to associate with the specified scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateCodeSecurityScanConfigurationRequest) -> dict:
    out: dict = {}
    import capo_inspector2.types.associate_configuration_request_list

    out["associateConfigurationRequests"] = (
        capo_inspector2.types.associate_configuration_request_list.serialize_json(
            value["associate_configuration_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchAssociateCodeSecurityScanConfigurationRequest:
    out: BatchAssociateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("associateConfigurationRequests") is not None:
        import capo_inspector2.types.associate_configuration_request_list

        out["associate_configuration_requests"] = (
            capo_inspector2.types.associate_configuration_request_list.deserialize_json(
                data["associateConfigurationRequests"]
            )
        )
    else:
        out["associate_configuration_requests"] = []
    return out
