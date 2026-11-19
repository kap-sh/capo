"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeConditionalForwardersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.conditional_forwarders


class DescribeConditionalForwardersResult(TypedDict, closed=True):
    conditional_forwarders: NotRequired[
        "capo_directory_service.types.conditional_forwarders.ConditionalForwarders"
    ]
    """<p>The list of conditional forwarders that have been created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConditionalForwardersResult) -> dict:
    out: dict = {}
    if "conditional_forwarders" in value:
        import capo_directory_service.types.conditional_forwarders

        out["ConditionalForwarders"] = (
            capo_directory_service.types.conditional_forwarders.serialize_aws_json_1_1(
                value["conditional_forwarders"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConditionalForwardersResult:
    out: DescribeConditionalForwardersResult = {}  # type: ignore[typeddict-item]
    if data.get("ConditionalForwarders") is not None:
        import capo_directory_service.types.conditional_forwarders

        out["conditional_forwarders"] = (
            capo_directory_service.types.conditional_forwarders.deserialize_aws_json_1_1(
                data["ConditionalForwarders"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeConditionalForwardersResult) -> dict:
    out: dict = {}
    if "conditional_forwarders" in value:
        import capo_directory_service.types.conditional_forwarders

        out["ConditionalForwarders"] = (
            capo_directory_service.types.conditional_forwarders.serialize_cbor(
                value["conditional_forwarders"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeConditionalForwardersResult:
    out: DescribeConditionalForwardersResult = {}  # type: ignore[typeddict-item]
    if data.get("ConditionalForwarders") is not None:
        import capo_directory_service.types.conditional_forwarders

        out["conditional_forwarders"] = (
            capo_directory_service.types.conditional_forwarders.deserialize_cbor(
                data["ConditionalForwarders"]
            )
        )
    return out
