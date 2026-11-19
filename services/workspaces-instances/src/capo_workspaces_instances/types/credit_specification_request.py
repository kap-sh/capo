"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CreditSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.cpu_credits_enum


class CreditSpecificationRequest(TypedDict, closed=True):
    cpu_credits: NotRequired[
        "capo_workspaces_instances.types.cpu_credits_enum.CpuCreditsEnum"
    ]
    """<p>CPU credit specification mode.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditSpecificationRequest) -> dict:
    out: dict = {}
    if "cpu_credits" in value:
        import capo_workspaces_instances.types.cpu_credits_enum

        out["CpuCredits"] = (
            capo_workspaces_instances.types.cpu_credits_enum.serialize_aws_json_1_0(
                value["cpu_credits"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreditSpecificationRequest:
    out: CreditSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("CpuCredits") is not None:
        import capo_workspaces_instances.types.cpu_credits_enum

        out["cpu_credits"] = (
            capo_workspaces_instances.types.cpu_credits_enum.deserialize_aws_json_1_0(
                data["CpuCredits"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreditSpecificationRequest) -> dict:
    out: dict = {}
    if "cpu_credits" in value:
        import capo_workspaces_instances.types.cpu_credits_enum

        out["CpuCredits"] = (
            capo_workspaces_instances.types.cpu_credits_enum.serialize_cbor(
                value["cpu_credits"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreditSpecificationRequest:
    out: CreditSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("CpuCredits") is not None:
        import capo_workspaces_instances.types.cpu_credits_enum

        out["cpu_credits"] = (
            capo_workspaces_instances.types.cpu_credits_enum.deserialize_cbor(
                data["CpuCredits"]
            )
        )
    return out
