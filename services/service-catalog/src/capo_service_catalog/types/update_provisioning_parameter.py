"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisioningParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.parameter_key
    import capo_service_catalog.types.parameter_value
    import capo_service_catalog.types.use_previous_value


class UpdateProvisioningParameter(TypedDict, closed=True):
    key: NotRequired["capo_service_catalog.types.parameter_key.ParameterKey"]
    """<p>The parameter key.</p>"""
    value: NotRequired["capo_service_catalog.types.parameter_value.ParameterValue"]
    """<p>The parameter value.</p>"""
    use_previous_value: "capo_service_catalog.types.use_previous_value.UsePreviousValue"
    """<p>If set to true, <code>Value</code> is ignored and the previous parameter value is kept.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisioningParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    out["UsePreviousValue"] = value.get("use_previous_value", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisioningParameter:
    out: UpdateProvisioningParameter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("UsePreviousValue") is not None:
        out["use_previous_value"] = data["UsePreviousValue"]
    else:
        out["use_previous_value"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateProvisioningParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    out["UsePreviousValue"] = value.get("use_previous_value", False)
    return out


def deserialize_cbor(data: dict) -> UpdateProvisioningParameter:
    out: UpdateProvisioningParameter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("UsePreviousValue") is not None:
        out["use_previous_value"] = data["UsePreviousValue"]
    else:
        out["use_previous_value"] = False
    return out
