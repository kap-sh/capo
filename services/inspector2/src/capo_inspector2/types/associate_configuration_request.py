"""Generated from Smithy shape ``com.amazonaws.inspector2#AssociateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_resource
    import capo_inspector2.types.scan_configuration_arn


class AssociateConfigurationRequest(TypedDict, closed=True):
    scan_configuration_arn: (
        "capo_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the scan configuration.</p>"""
    resource: "capo_inspector2.types.code_security_resource.CodeSecurityResource"


# --- restJson1 ser/de ---
def serialize_json(value: AssociateConfigurationRequest) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    import capo_inspector2.types.code_security_resource

    out["resource"] = capo_inspector2.types.code_security_resource.serialize_json(
        value["resource"]
    )
    return out


def deserialize_json(data: dict) -> AssociateConfigurationRequest:
    out: AssociateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanConfigurationArn") is not None:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        out["scan_configuration_arn"] = ""
    if data.get("resource") is not None:
        import capo_inspector2.types.code_security_resource

        out["resource"] = capo_inspector2.types.code_security_resource.deserialize_json(
            data["resource"]
        )
    else:
        out["resource"] = {"$unknown": {"name": ""}}
    return out
