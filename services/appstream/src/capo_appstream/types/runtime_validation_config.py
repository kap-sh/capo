"""Generated from Smithy shape ``com.amazonaws.appstream#RuntimeValidationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.instance_type


class RuntimeValidationConfig(TypedDict, closed=True):
    intended_instance_type: NotRequired[
        "capo_appstream.types.instance_type.InstanceType"
    ]
    """<p>The instance type to use for runtime validation testing. It's recommended to use the same instance type you plan to use for your fleet to ensure accurate validation results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuntimeValidationConfig) -> dict:
    out: dict = {}
    if "intended_instance_type" in value:
        out["IntendedInstanceType"] = value["intended_instance_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuntimeValidationConfig:
    out: RuntimeValidationConfig = {}  # type: ignore[typeddict-item]
    if data.get("IntendedInstanceType") is not None:
        out["intended_instance_type"] = data["IntendedInstanceType"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuntimeValidationConfig) -> dict:
    out: dict = {}
    if "intended_instance_type" in value:
        out["IntendedInstanceType"] = value["intended_instance_type"]
    return out


def deserialize_cbor(data: dict) -> RuntimeValidationConfig:
    out: RuntimeValidationConfig = {}  # type: ignore[typeddict-item]
    if data.get("IntendedInstanceType") is not None:
        out["intended_instance_type"] = data["IntendedInstanceType"]
    return out
