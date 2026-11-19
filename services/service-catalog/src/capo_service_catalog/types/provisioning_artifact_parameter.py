"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.default_value
    import capo_service_catalog.types.description
    import capo_service_catalog.types.no_echo
    import capo_service_catalog.types.parameter_constraints
    import capo_service_catalog.types.parameter_key
    import capo_service_catalog.types.parameter_type


class ProvisioningArtifactParameter(TypedDict, closed=True):
    parameter_key: NotRequired["capo_service_catalog.types.parameter_key.ParameterKey"]
    """<p>The parameter key.</p>"""
    default_value: NotRequired["capo_service_catalog.types.default_value.DefaultValue"]
    """<p>The default value.</p>"""
    parameter_type: NotRequired[
        "capo_service_catalog.types.parameter_type.ParameterType"
    ]
    """<p>The parameter type.</p>"""
    is_no_echo: "capo_service_catalog.types.no_echo.NoEcho"
    """<p>If this value is true, the value for this parameter is obfuscated from view when the parameter is retrieved. This parameter is used to hide sensitive information.</p>"""
    description: NotRequired["capo_service_catalog.types.description.Description"]
    """<p>The description of the parameter.</p>"""
    parameter_constraints: NotRequired[
        "capo_service_catalog.types.parameter_constraints.ParameterConstraints"
    ]
    """<p>Constraints that the administrator has put on a parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactParameter) -> dict:
    out: dict = {}
    if "parameter_key" in value:
        out["ParameterKey"] = value["parameter_key"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "parameter_type" in value:
        out["ParameterType"] = value["parameter_type"]
    out["IsNoEcho"] = value.get("is_no_echo", False)
    if "description" in value:
        out["Description"] = value["description"]
    if "parameter_constraints" in value:
        import capo_service_catalog.types.parameter_constraints

        out["ParameterConstraints"] = (
            capo_service_catalog.types.parameter_constraints.serialize_aws_json_1_1(
                value["parameter_constraints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactParameter:
    out: ProvisioningArtifactParameter = {}  # type: ignore[typeddict-item]
    if data.get("ParameterKey") is not None:
        out["parameter_key"] = data["ParameterKey"]
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    if data.get("ParameterType") is not None:
        out["parameter_type"] = data["ParameterType"]
    if data.get("IsNoEcho") is not None:
        out["is_no_echo"] = data["IsNoEcho"]
    else:
        out["is_no_echo"] = False
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ParameterConstraints") is not None:
        import capo_service_catalog.types.parameter_constraints

        out["parameter_constraints"] = (
            capo_service_catalog.types.parameter_constraints.deserialize_aws_json_1_1(
                data["ParameterConstraints"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactParameter) -> dict:
    out: dict = {}
    if "parameter_key" in value:
        out["ParameterKey"] = value["parameter_key"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "parameter_type" in value:
        out["ParameterType"] = value["parameter_type"]
    out["IsNoEcho"] = value.get("is_no_echo", False)
    if "description" in value:
        out["Description"] = value["description"]
    if "parameter_constraints" in value:
        import capo_service_catalog.types.parameter_constraints

        out["ParameterConstraints"] = (
            capo_service_catalog.types.parameter_constraints.serialize_cbor(
                value["parameter_constraints"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ProvisioningArtifactParameter:
    out: ProvisioningArtifactParameter = {}  # type: ignore[typeddict-item]
    if data.get("ParameterKey") is not None:
        out["parameter_key"] = data["ParameterKey"]
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    if data.get("ParameterType") is not None:
        out["parameter_type"] = data["ParameterType"]
    if data.get("IsNoEcho") is not None:
        out["is_no_echo"] = data["IsNoEcho"]
    else:
        out["is_no_echo"] = False
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ParameterConstraints") is not None:
        import capo_service_catalog.types.parameter_constraints

        out["parameter_constraints"] = (
            capo_service_catalog.types.parameter_constraints.deserialize_cbor(
                data["ParameterConstraints"]
            )
        )
    return out
