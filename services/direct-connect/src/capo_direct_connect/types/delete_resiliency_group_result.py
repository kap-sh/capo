"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteResiliencyGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.resiliency_group


class DeleteResiliencyGroupResult(TypedDict, closed=True):
    resiliency_group: NotRequired[
        "capo_direct_connect.types.resiliency_group.ResiliencyGroup"
    ]
    """<p>Information about the resiliency group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResiliencyGroupResult) -> dict:
    out: dict = {}
    if "resiliency_group" in value:
        import capo_direct_connect.types.resiliency_group

        out["resiliencyGroup"] = (
            capo_direct_connect.types.resiliency_group.serialize_aws_json_1_1(
                value["resiliency_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResiliencyGroupResult:
    out: DeleteResiliencyGroupResult = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroup") is not None:
        import capo_direct_connect.types.resiliency_group

        out["resiliency_group"] = (
            capo_direct_connect.types.resiliency_group.deserialize_aws_json_1_1(
                data["resiliencyGroup"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteResiliencyGroupResult) -> dict:
    out: dict = {}
    if "resiliency_group" in value:
        import capo_direct_connect.types.resiliency_group

        out["resiliencyGroup"] = (
            capo_direct_connect.types.resiliency_group.serialize_cbor(
                value["resiliency_group"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeleteResiliencyGroupResult:
    out: DeleteResiliencyGroupResult = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroup") is not None:
        import capo_direct_connect.types.resiliency_group

        out["resiliency_group"] = (
            capo_direct_connect.types.resiliency_group.deserialize_cbor(
                data["resiliencyGroup"]
            )
        )
    return out
